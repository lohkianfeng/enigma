class Plugboard:
    def_config = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

    def __init__(self, config) -> None:
        self.config = config

    def forward(self, nbr) -> int:
        alpha = self.def_config[nbr]
        nbr = self.config.find(alpha)
        return nbr

    def backward(self, nbr) -> int:
        alpha = self.config[nbr]
        nbr = self.def_config.find(alpha)
        return nbr
