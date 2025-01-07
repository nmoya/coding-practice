import random

import torch

import ml.utilities as utils


class SyntheticRegressionData(utils.DataModule):
    def __init__(self, w, b, noise=0.01, num_train=1000, num_val=1000, batch_size=32):
        super().__init__()
        self.w = w
        self.b = b
        self.noise = noise
        self.num_train = num_train
        self.num_val = num_val
        self.batch_size = batch_size

        n = num_train + num_val
        self.X = torch.randn(n, len(w))
        noise = torch.randn(n, 1) * noise
        self.y = torch.matmul(self.X, w.reshape((-1, 1))) + b + noise

    def get_dataloader(self, train):
        i = slice(0, self.num_train) if train else slice(self.num_train, None)
        return self.get_tensorloader((self.X, self.y), train, i)

    def get_tensorloader(self, tensors, train, indices=slice(0, None)):
        tensors = tuple(a[indices] for a in tensors)
        dataset = torch.utils.data.TensorDataset(*tensors)
        return torch.utils.data.DataLoader(dataset, self.batch_size, shuffle=train)


class SGD:
    """Minibatch stochastic gradient descent."""

    def __init__(self, params, lr: float):
        self.params = list(params)
        self.lr = lr

    def step(self):
        for param in self.params:
            param -= self.lr * param.grad

    def zero_grad(self):
        for param in self.params:
            if param.grad is not None:
                param.grad.zero_()


class LinearRegressionScratch(utils.Module):
    def __init__(self, num_inputs, lr, sigma=0.01, **kwargs):
        kwargs = kwargs or {}
        super().__init__(**kwargs)
        self.num_inputs = num_inputs
        self.lr = lr
        self.sigma = sigma
        self.w = torch.normal(0, sigma, (num_inputs, 1), requires_grad=True)
        self.b = torch.zeros(1, requires_grad=True)

    def forward(self, X):
        return torch.matmul(X, self.w) + self.b

    def loss(self, y_hat, y):
        # Loss of the entire batch
        loss = (y_hat - y) ** 2 / 2

        # Returns the average loss of the batch
        return loss.mean()

    def configure_optimizers(self):
        return SGD([self.w, self.b], self.lr)


class WeightDecayScratch(LinearRegressionScratch):
    def __init__(self, num_inputs, lambd, lr, sigma=0.01):
        super().__init__(num_inputs, lr, sigma)
        self.lambd = lambd

    def l2_penalty(self):
        return torch.sum(self.w**2) / 2

    def loss(self, y_hat, y):
        return super().loss(y_hat, y) + self.lambd * self.l2_penalty()


if __name__ == "__main__":

    def train_without_regularization():
        model = LinearRegressionScratch(2, lr=0.03, sigma=0.01)
        data = SyntheticRegressionData(w=torch.tensor([2, -3.4]), b=4.2)
        trainer = utils.Trainer(max_epochs=25)
        trainer.fit(model, data)
        with torch.no_grad():
            print(f"error in estimating w: {data.w - model.w.reshape(data.w.shape)}")
            print(f"error in estimating b: {data.b - model.b}")

    def train_with_l2_regularization():
        class Data(utils.DataModule):
            def __init__(self, num_train, num_val, num_inputs, batch_size):
                self.batch_size = batch_size
                self.num_train = num_train
                self.num_val = num_val
                self.num_inputs = num_inputs
                n = num_train + num_val
                self.X = torch.randn(n, num_inputs)
                noise = torch.randn(n, 1) * 0.01
                w, b = torch.ones((num_inputs, 1)) * 0.01, 0.05
                self.y = torch.matmul(self.X, w) + b + noise

            def get_dataloader(self, train):
                i = slice(0, self.num_train) if train else slice(self.num_train, None)
                return self.get_tensorloader([self.X, self.y], train, i)

            def get_tensorloader(self, tensors, train, indices=slice(0, None)):
                tensors = tuple(a[indices] for a in tensors)
                dataset = torch.utils.data.TensorDataset(*tensors)
                return torch.utils.data.DataLoader(dataset, self.batch_size, shuffle=train)

        data = Data(num_train=20, num_val=100, num_inputs=200, batch_size=5)
        trainer = utils.Trainer(max_epochs=10)

        model = WeightDecayScratch(num_inputs=200, lambd=0, lr=0.01)
        model.board.yscale = "log"
        model.plot_name = "regularization_lambda_0.png"
        trainer.fit(model, data)
        print("L2 norm of w:", float(model.l2_penalty()))

        model = WeightDecayScratch(num_inputs=200, lambd=3, lr=0.01)
        model.board.yscale = "log"
        model.plot_name = "regularization_lambda_3.png"
        trainer.fit(model, data)
        print("L2 norm of w:", float(model.l2_penalty()))

        model = WeightDecayScratch(num_inputs=200, lambd=15, lr=0.01)
        model.board.yscale = "log"
        model.plot_name = "regularization_lambda_15.png"
        trainer.fit(model, data)
        print("L2 norm of w:", float(model.l2_penalty()))

    train_with_l2_regularization()
