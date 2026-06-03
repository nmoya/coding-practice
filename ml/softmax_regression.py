from torch import nn
from torch.nn import functional as F

from ml.utilities import Classifier, FashionMNIST, Trainer


class SoftmaxRegression(Classifier):
    def __init__(self, num_outputs, lr):
        super().__init__()
        self.num_outputs = num_outputs
        self.lr = lr
        self.net = nn.Sequential(nn.Flatten(), nn.LazyLinear(num_outputs))

    def forward(self, X):
        return self.net(X)

    def loss(self, Y_hat, Y, averaged=True):
        Y_hat = Y_hat.reshape((-1, Y_hat.shape[-1]))
        Y = Y.reshape((-1,))
        return F.cross_entropy(Y_hat, Y, reduction="mean" if averaged else "none")


if __name__ == "__main__":
    data = FashionMNIST(batch_size=256)
    model = SoftmaxRegression(num_outputs=10, lr=0.1)
    trainer = Trainer(max_epochs=10)
    trainer.fit(model, data)
