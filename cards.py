from PIL import Image
import random

import gui


class HogwartsCard:

    def __init__(self):

        self.cost = 0
        self.inStore = False
        self.available = True

    def buy_card(self, player):
        player.remove_coin(self.cost)
        self.inStore = False
        self.available = False

# These are specific sub-classes to the player class
class Alohamora(HogwartsCard):
    name = "Alohamora"
    imageFile = Image.open('images/cards/alohamora.jpg')
    description = "Gain 1 Coin."

    def __init__(self):
        super().__init__()
        self.cost = 0

    def use(self, game):
        if game.ap.can_get_coins:
            game.ap.give_coin(1)

class Incendio(HogwartsCard):
    name = "Incendio"
    imageFile = Image.open('images/cards/incendio.jpg')
    description = "Gain 1 Zip-zap.  Draw a card."

    def __init__(self):
        super().__init__()
        self.cost = 4

    def use(self, game):
        if game.ap.can_get_zips:
            game.ap.give_zip(1)
        if game.ap.can_draw_cards:
            game.ap.draw_card()

class Reparo(HogwartsCard):
    name = "Reparo"
    imageFile = Image.open('images/cards/reparo.jpg')
    description = "Choose one: Gain 2 Coins; or draw a card."

    def __init__(self):
        super().__init__()
        self.cost = 3

    def use(self, game):
        choice = gui.PU_Reparo(game)
        choice.show()

class Lumos(HogwartsCard):
    name = "Lumos"
    imageFile = Image.open('images/cards/lumos.jpg')
    description = "All Heroes draw a card."

    def __init__(self):
        super().__init__()
        self.cost = 4

    def use(self, game):
        for i in game.players:
            i.draw_card()

class InvisibilityCloak(HogwartsCard):
    name = "Invisibility Cloak"
    imageFile = Image.open('images/players/harry/invisibility cloak.jpg')

    def __init__(self):
        super().__init__()
        self.cost = 0

    def use(self, game):
        if game.ap.can_get_coins:
            game.ap.give_coin(1)
        game.ap.invCloak = False

class SortingHat(HogwartsCard):
    name = "Sorting Hat"
    imageFile = Image.open('images/cards/sorting hat.jpg')
    description = "Gain 2. You may put Allies you acquire on top of your deck instead of in your discard pile."

    def __init__(self):
        super().__init__()
        self.cost = 4

    def use(self, game):
        if game.ap.can_get_coins:
            game.ap.give_coin(2)

class Hagrid(HogwartsCard):
    name = "Rubeus Hagrid"
    imageFile = Image.open('images/cards/hagrid.jpg')
    description = "Gain 1 Zip-zap.  ALL Heroes gain 1 Heart."

    def __init__(self):
        super().__init__()
        self.cost = 4

    def use(self, game):
        if game.ap.can_get_zips:
            game.ap.give_zip(1)
        for i in game.players:
            if i.can_heal:
                i.heal(1)

class Dittany(HogwartsCard):
    name = "Essence of Dittany"
    imageFile = Image.open('images/cards/essance of dittany.jpg')
    description = "Any one Hero gains 2 Hearts."

    def __init__(self):
        super().__init__()
        self.cost = 2

    def use(self, game):
        choice = gui.PU_Dittany(game)
        choice.show()

class QuidditchGear(HogwartsCard):
    name = "Quidditch Gear"
    imageFile = Image.open('images/cards/quidditch gear.jpg')
    description = "Gain 1 Zip-zap and 1 Heart."

    def __init__(self):
        super().__init__()
        self.cost = 3

    def use(self, game):
        if game.ap.can_get_zips:
            game.ap.give_zip(1)
        if game.ap.can_heal:
            game.ap.heal(1)



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

class Hwmnbn(DarkArtsCard):
    name = "He-Who-Must-Not-Be-Named"
    imageFile = Image.open('images/dark arts/hewhomustnotbenamed.png')
    description = "Add 1 to Location."

    def __init__(self):
        None

    def use(self, game):
        None

class Petrification(DarkArtsCard):
    name = "Petrification"
    imageFile = Image.open('images/dark arts/petrification.png')
    description = "ALL Heroes lose 1 Heart and cannot draw extra cards this turn."

    def __init__(self):
        None

    def use(self, game):
        for p in game.players:
            p.can_draw_cards = False
            p.damage(1)