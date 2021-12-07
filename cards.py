from PIL import Image
import random


class HogwartsCard:

    def __init__(self):

        self.cost = 0
        self.inStore = False
        self.available = True

    def buyCard(self, player):
        player.remove_coin(self.cost)
        self.inStore = False
        self.available = False

# These are specific sub-classes to the player class
class Alohamora(HogwartsCard):
    name = "Alohamora"
    imageFile = Image.open('images/cards/alohamora.jpg')

    def __init__(self):
        super().__init__()
        self.cost = 0

    def use(self, player):
        if player.can_get_coins:
            player.give_coin(1)

class Incendio(HogwartsCard):
    name = "Incendio"
    imageFile = Image.open('images/cards/incendio.jpg')

    def __init__(self):
        super().__init__()
        self.cost = 4

    def use(self, player):
        if player.can_get_zips:
            player.give_zip(1)
        if player.can_draw_cards:
            player.draw_card()

class InvisibilityCloak(HogwartsCard):
    name = "Invisibility Cloak"
    imageFile = Image.open('images/players/harry/invisibility cloak.jpg')

    def __init__(self):
        super().__init__()
        self.cost = 0

    def use(self, player):
        if player.can_get_coins:
            player.give_coin(1)
        player.invCloak = False


class VillainCard:
    def __init__(self):
        None

class CrabbeAndGoyle(VillainCard):
    name = "Crabbe and Goyle"
    imageFile = Image.open('images/villians/crabbe and goyle.png')
    description = "Each time a Dark Arts event or villain causes a Hero to discard a card, that Hero loses 1 Heart."
    reward = "All Heroes draw a card."

    def __init__(self):
        None

    def trigger(self):
        # How do we know if this triggers
        # determine then return whether or not it was triggered
        return True

    def use(self, player):
        player.damage(1)

    def reward(self, player):
        player.draw_card()
        # Need to do this for all players???


class DarkArtsCard:
    def __init__(self):
        None

class Expulso(DarkArtsCard):
    name = "Expulso"
    imageFile = Image.open('images/dark arts/expulso.png')
    description = "Active Hero loses 2 Hearts."

    def __init__(self):
        None

    def use(self, game):
        game.ap.damage(2)

class Flipendo(DarkArtsCard):
    name = "Flipendo"
    imageFile = Image.open('images/dark arts/flipendo.png')
    description = "Active Hero loses 1 Heart and discards a card."

    def __init__(self):
        None

    def use(self, game):
        game.ap.damage(1)

