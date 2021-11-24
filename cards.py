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
    name = "Alohamora"
    imageFile = Image.open('images/cards/alohamora.jpg')

    def __init__(self):
        super().__init__()
        self.cost = 0

    def use(self, player):
        if player.can_get_coins:
            player.give_coin(1)


class Incendio(Card):
    name = "Incendio"
    imageFile = Image.open('images/cards/incendio.jpg')

    def __init__(self):
        super().__init__()
        self.cost = 0

    def use(self, player):
        if player.can_get_zips:
            player.give_zip(1)
        if player.can_draw_cards:
            None
            # player.draw_card()
