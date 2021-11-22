from PIL import Image
import random


class Card:

    def __init__(self):

        self.cost = 0
        self.inStore = False
        self.available = True

    def buyCard(self, player):
        player.removeCoin(self.cost)
        self.inStore = False
        self.available = False

# These are specific sub-classes to the player class
class Alohamora(Card):
    # Since this is a hard-coded string and will not change, it can be outside of the init.
    # It does not hurt to move it inside, but this can be here.
    name = "Alohamora"
    imageFile = Image.open('images/cards/card_back.jpg')

    def __init__(self):
        super().__init__()
        self.cost = 0

    def use(self, player):
        if player.can_get_coins:
            player.giveCoin(1)
