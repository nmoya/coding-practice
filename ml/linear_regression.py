import torch
from torch import nn

from ml.linear_regression_scratch import SyntheticRegressionData
from ml.utilities import Module, Trainer


class LinearRegression(Module):
    def __init__(self, wd, lr):
        super().__init__(plot_name="linear_regression.png")
        self.lr = lr
        self.wd = wd
        self.net = nn.LazyLinear(1)
        self.net.weight.data.normal_(0, 0.01)
        self.net.bias.data.fill_(0)

    def forward(self, X):
        return self.net(X)

    def loss(self, y_hat, y):
        fn = nn.MSELoss()
        return fn(y_hat, y)

    def configure_optimizers(self):
        return torch.optim.SGD(
            [
                {"params": self.net.weight, "weight_decay": self.wd},
                {"params": self.net.bias},
            ],
            lr=self.lr,
        )

    def get_w_b(self):
        return (self.net.weight.data, self.net.bias.data)


if __name__ == "__main__":
    model = LinearRegression(wd=3, lr=0.01)
    data = SyntheticRegressionData(w=torch.tensor([2, -3.4]), b=4.2)
    trainer = Trainer(max_epochs=10)
    trainer.fit(model, data)
    w, b = model.get_w_b()

    print(f"error in estimating w: {data.w - w.reshape(data.w.shape)}")
    print(f"error in estimating b: {data.b - b}")
