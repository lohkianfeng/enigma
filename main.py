"""
Rotor	ABCDEFGHIJKLMNOPQRSTUVWXYZ
ETW	    ABCDEFGHIJKLMNOPQRSTUVWXYZ
I	    EKMFLGDQVZNTOWYHXUSPAIBRCJ
II	    AJDKSIRUXBLHWTMCQGZNPYFVOE
III	    BDFHJLCPRTXVZNYEIWGAKMUSQO
IV	    ESOVPZJAYQUIRHXLNFTGKDCMWB
V	    VZBRGITYUPSDNHLXAWMJQOFECK
UKW-A	EJMZALYXVBWFCRQUONTSPIKHGD
UKW-B	YRUHQSLDPXNGOKMIEBFZCWVJAT
UKW-C	FVPJIAOYEDRZXWGCTKUQSBNMHL

AR GK OX
"""

from keyboard import Keyboard
from plugboard import Plugboard
from rotor import Rotor


class Enigma:
    keyboard = Keyboard("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
    plugboard = Plugboard("RBCDEFKHIJGLMNXPQASTUVWOYZ")
    right = Rotor("BDFHJLCPRTXVZNYEIWGAKMUSQO")
    middle = Rotor("AJDKSIRUXBLHWTMCQGZNPYFVOE")
    left = Rotor("EKMFLGDQVZNTOWYHXUSPAIBRCJ")
    reflector = Rotor("EJMZALYXVBWFCRQUONTSPIKHGD")

    def output(self, alpha) -> str:
        print(alpha)
        nbr = self.keyboard.forward(alpha)
        nbr = self.plugboard.forward(nbr)
        nbr = self.right.forward(nbr)
        nbr = self.middle.forward(nbr)
        nbr = self.left.forward(nbr)
        nbr = self.reflector.forward(nbr)
        nbr = self.left.backward(nbr)
        nbr = self.middle.backward(nbr)
        nbr = self.right.backward(nbr)
        nbr = self.plugboard.backward(nbr)
        alpha = self.keyboard.backward(nbr)
        print(alpha)


enigma = Enigma()
enigma.output("A")
