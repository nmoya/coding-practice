import collections
from dataclasses import dataclass, field
from typing import List

import torch
from matplotlib import pyplot as plt
from torch import nn
from tqdm import tqdm


def cpu():
    """Get the CPU device.

    Defined in :numref:`sec_use_gpu`"""
    return torch.device("cpu")


def gpu(i=0):
    """Get a GPU device.

    Defined in :numref:`sec_use_gpu`"""
    return torch.device(f"cuda:{i}")


def num_gpus():
    """Get the number of available GPUs.

    Defined in :numref:`sec_use_gpu`"""
    return torch.cuda.device_count()


def try_gpu(i=0):
    """Return gpu(i) if exists, otherwise return cpu().

    Defined in :numref:`sec_use_gpu`"""
    if num_gpus() >= i + 1:
        return gpu(i)
    return cpu()


def try_all_gpus():
    """Return all available GPUs, or [cpu(),] if no GPU exists.

    Defined in :numref:`sec_use_gpu`"""
    return [gpu(i) for i in range(num_gpus())]


@dataclass
class ProgressBoard:
    raw_points: dict = field(default_factory=dict)
    data: dict = field(default_factory=dict)
    xlabel: str = None
    ylabel: str = None
    xlim: List | None = None
    ylim: List | None = None
    xscale: str = "linear"
    yscale: str = "linear"
    ls: List = field(default_factory=lambda: ["-", "--", "-.", ":"])
    colors: List = field(default_factory=lambda: ["C0", "C1", "C2", "C3"])
    fig: object | None = None
    axes: object | None = None
    figsize: tuple = (3.5, 2.5)
    display: bool = True

    def draw(self, x, y, label, every_n=1, filename="debug.png"):
        """Defined in :numref:`sec_utils`"""

        def mean(x):
            return sum(x) / len(x)

        Point = collections.namedtuple("Point", ["x", "y"])
        if label not in self.raw_points:
            self.raw_points[label] = []
            self.data[label] = []
        points = self.raw_points[label]
        line = self.data[label]
        points.append(Point(x, y))
        if len(points) != every_n:
            return

        line.append(Point(mean([p.x for p in points]), mean([p.y for p in points])))
        points.clear()
        if not self.display:
            return
        if self.fig is None:
            self.fig = plt.figure(figsize=self.figsize)
        plt_lines, labels = [], []
        for (k, v), ls, color in zip(self.data.items(), self.ls, self.colors):
            plt_lines.append(plt.plot([p.x for p in v], [p.y for p in v], linestyle=ls, color=color)[0])
            labels.append(k)
        axes = self.axes if self.axes else plt.gca()
        if self.xlim:
            axes.set_xlim(self.xlim)
        if self.ylim:
            axes.set_ylim(self.ylim)
        if not self.xlabel:
            self.xlabel = self.x
        axes.set_xlabel(self.xlabel)
        axes.set_ylabel(self.ylabel)
        axes.set_xscale(self.xscale)
        axes.set_yscale(self.yscale)
        axes.legend(plt_lines, labels)
        plt.savefig(f"./ml/{filename}")


class DataModule:
    def __init__(self, root="../data", num_workers=4):
        self.root = root
        self.num_workers = num_workers

    def get_dataloader(self, train: bool):
        raise NotImplementedError

    def train_dataloader(self):
        return self.get_dataloader(train=True)

    def val_dataloader(self):
        return self.get_dataloader(train=False)


class Module(nn.Module):
    """The base class of models."""

    def __init__(self, plot_train_per_epoch=2, plot_valid_per_epoch=1, plot_name: str = "debug.png"):
        super().__init__()
        self.plot_train_per_epoch = plot_train_per_epoch
        self.plot_valid_per_epoch = plot_valid_per_epoch
        self.plot_name = plot_name
        self.board = ProgressBoard()

    def loss(self, y_hat, y):
        raise NotImplementedError

    def forward(self, X):
        assert hasattr(self, "net"), "Neural network is defined"
        return self.net(X)

    def plot(self, key, value, train):
        """Plot a point in animation."""
        assert hasattr(self, "trainer"), "Trainer is not inited"
        self.board.xlabel = "epoch"
        if train:
            x = self.trainer.train_batch_idx / self.trainer.num_train_batches
            n = self.trainer.num_train_batches / self.plot_train_per_epoch
        else:
            x = self.trainer.epoch + 1
            n = self.trainer.num_val_batches / self.plot_valid_per_epoch
        self.board.draw(
            x,
            value.to(cpu()).detach().numpy(),
            ("train_" if train else "val_") + key,
            every_n=int(n),
            filename=self.plot_name,
        )

    def training_step(self, batch):
        loss = self.loss(self(*batch[:-1]), batch[-1])
        self.plot("loss", loss, train=True)
        return loss

    def validation_step(self, batch):
        loss = self.loss(self(*batch[:-1]), batch[-1])
        self.plot("loss", loss, train=False)

    def configure_optimizers(self):
        raise NotImplementedError


class Trainer:
    """The base class for training models with data."""

    def __init__(self, max_epochs, num_gpus=0, gradient_clip_val=0):
        self.max_epochs = max_epochs
        self.num_gpus = num_gpus
        self.gradient_clip_val = gradient_clip_val
        self.model = None
        self.optim = None
        self.train_dataloader = None
        self.val_dataloader = None
        self.num_train_batches = 0
        self.num_val_batches = 0
        self.epoch = 0
        self.train_batch_idx = 0
        self.val_batch_idx = 0

    def prepare_data(self, data):
        self.train_dataloader = data.train_dataloader()
        self.val_dataloader = data.val_dataloader()
        self.num_train_batches = len(self.train_dataloader)
        self.num_val_batches = len(self.val_dataloader) if self.val_dataloader is not None else 0

    def prepare_model(self, model):
        model.trainer = self
        model.board.xlim = [0, self.max_epochs]
        self.model = model

    def fit(self, model, data):
        self.prepare_data(data)
        self.prepare_model(model)
        self.optim = model.configure_optimizers()
        self.epoch = 0
        self.train_batch_idx = 0
        self.val_batch_idx = 0
        for self.epoch in tqdm(range(self.max_epochs)):
            self.fit_epoch()

    def prepare_batch(self, batch):
        return batch

    def fit_epoch(self):
        self.model.train()
        for batch in self.train_dataloader:
            loss = self.model.training_step(self.prepare_batch(batch))
            self.optim.zero_grad()
            with torch.no_grad():
                loss.backward()
                if self.gradient_clip_val > 0:  # To be discussed later
                    self.clip_gradients(self.gradient_clip_val, self.model)
                self.optim.step()
            self.train_batch_idx += 1
        if self.val_dataloader is None:
            return
        self.model.eval()
        for batch in self.val_dataloader:
            with torch.no_grad():
                self.model.validation_step(self.prepare_batch(batch))
            self.val_batch_idx += 1
