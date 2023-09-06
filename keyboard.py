class Keyboard:
    def __init__(self, config) -> None:
        self.config = config

    def forward(self, alpha) -> int:
        nbr = self.config.find(alpha)
        return nbr

    def backward(self, nbr) -> str:
        alpha = self.config[nbr]
        return alpha
