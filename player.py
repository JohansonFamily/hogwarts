 
from PIL import Image
import random


class Player:

    # This section is for hard-coded variables or text strings that will never change and relate to all players.
    # I can't think of anything right now that would go here.
    
    def __init__(self):

        # Setup all attributes that can be different between players here
        # Do not add attributes unique to a specific player.
        # Here are some examples.
        self.active = False
        self.stunned = False
        self.life = 10
        self.zips = 0
        self.coins = 0
        self.deck = []
        self.hand = []
        self.discard_pile = []
        self.can_draw_cards = True
        self.can_heal = True
        self.can_get_coins = True
        self.can_get_zips = True

    # In this section, we setup actions that all players can do

    # Called whenever someone is allowed to draw a card
    def draw_card(self):
        # Copied this from the OG game.
        if self.can_draw_cards:
            if len(self.deck) == 0:
                self.deck = self.discard_pile
                self.discard_pile.clear()
                random.shuffle(self.deck)
            self.hand.append(self.deck[0])
            self.deck.remove(self.deck[0])
        else:
            # Handle unable to draw cards gui
            None

    # Called whenever someone is damaged.  Pass in the amount of damage.
    ### CHILD CLASS for HARRY exists ###
    def damage(self, nbr):
        if self.life <= nbr:
            self.life = 0
            self.stun()
        else:
            self.life -= nbr

    # Add more player functions here:
    def heal(self, nbr):
        # What else needs to happen when someone is stunned?
        self.life += nbr
        if self.life > 10:
            self.life = 10


    def stun(self):
        # What else needs to happen when someone is stunned?
        self.stunned = True

    def give_zip(self, nbr):
        self.zips +=1

    def take_zip(self, nbr):
        None

    def give_coin(self, nbr):
        self.coins += 1

    def remove_coin(self, nbr):
        None

    def end_turn(self, nbr):
        None

    def play_card(self, card):
        card.use(self)


# These are specific sub-classes to the player class
class Harry(Player):
    # Since this is a hard-coded string and will not change, it can be outside of the init.
    # It does not hurt to move it inside, but this can be here.
    name = "Harry Potter"
    imageFile = Image.open('images/players/harry/harry.jpg')
    
    # All classes need their own init
    def __init__(self):
        # The super() function pulls in all the attributes of the parent class.
        # It also pull in all the functions of the parent class.
        super().__init__()
        # Here we can continue to add sub-class specific attributes that do not apply to other players
        self.invCloak = True

    # Redefining the same function as the parent over-rides the parent function.
    # All other players will use the parent function
    ####  BE CAREFUL NOT TO CHANGE ONE AND NOT THE OTHER ###
    def damage(self, nbr):
        if self.invCloak:
            nbr = 1
        if self.life <= nbr:
            self.life = 0
            self.stun()
        else:
            self.life -= nbr


class Hermione(Player):
    # Since this is a hard-coded string and will not change, it can be outside of the init.
    # It does not hurt to move it inside, but this can be here.
    name = "Hermione Granger"
    imageFile = Image.open('images/players/hermione/hermione.jpg')
    
    def __init__(self):
        # The super() function pulls in all the attributes and functions of the parent class.
        super().__init__()


class Neville(Player):
    # Since this is a hard-coded string and will not change, it can be outside of the init.
    # It does not hurt to move it inside, but this can be here.
    name = "Neville Longbottom"
    imageFile = Image.open('images/players/neville/neville.jpg')
    
    def __init__(self):
        # The super() function pulls in all the attributes and functions of the parent class.
        super().__init__()


class Ron(Player):
    # Since this is a hard-coded string and will not change, it can be outside of the init.
    # It does not hurt to move it inside, but this can be here.
    name = "Ron Weasly"
    imageFile = Image.open('images/players/ron/ron.jpg')
    
    def __init__(self):
        # The super() function pulls in all the attributes and functions of the parent class.
        super().__init__()

 