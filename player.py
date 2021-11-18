 
from PIL import Image
#import cards
import random

class Player():

    # This section is for hard-coded variables or text strings that will never change and relate to all players.  I can't think of anything right now that would go here.
    
    def __init__(self):

        # Setup all attributes that can be different between players here, but not attributes unique to a specific player.  Here are some examples.
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

    # In this section, we setup actions that all players can do

    # Called whenever someone is allowed to draw a card
    def draw_card(self):
        # Copied this from the OG game.
        if self.can_draw_cards == True:
            if len(self.deck) == 0:
                self.deck = self.discard_pile
                self.discard_pile.empty()
                random.shuffle(self.deck)
            self.hand.append(self.deck[0])
            self.deck.remove(self.deck[0])
        else:
            # Handle unable to draw cards gui
            None

    # Called whenever someone is damaged.  Pass in the amount of damage.
    ### CHILD CLASS for HARRY exists ###
    def damage(self, nbr):
        if self.life<= nbr: 
            self.life=0
            self.stun()
        else:
            self.life -= nbr

    # Add more player functions here:
    def heal(self, nbr):
        # This can be filled out later - just want to get the actions out
        None

    def stun(self):
        # What else needs to happen when someone is stunned?
        self.stunned=True

    def giveZip(self, nbr):
        None

    def removeZip(self, nbr):
        None

    def giveCoin(self, nbr):
        None

    def removeCoin(self, nbr):
        None

    def endTurn(self, nbr):
        None

    def playCard(self, card):
        None


# These are specific sub-classes to the player class
class Harry(Player):
    # Since this is a hard-coded string and will not change, it can be outside of the init.  It does not hurt to move it inside, but this can be here.
    name = "Harry Potter"
    imageFile = Image.open('images/harry.jpg')
    
    # All classes need their own init
    def __init__(self):
        # The super() function pulls in all the attributes of the parent class as well as all the function of the parent class. 
        super().__init__()
        # Here we can continue to add sub-class specific attributes that do not apply to other players
        self.invCloak = True

    # Redefinig the same function as the parent over-rides the parent function.  All other players will use the parent fuction
    ####  BE CAREFUL NOT TO CHANGE ONE AND NOT THE OTHER ###
    def damage(self, nbr):
        if self.invCloak: nbr=1
        if self.life<= nbr: 
            self.life=0
            self.stun()
        else:
            self.life -= nbr

class Hermione(Player):
    # Since this is a hard-coded string and will not change, it can be outside of the init.  It does not hurt to move it inside, but this can be here.
    name = "Hermione Granger"
    imageFile = Image.open('images/hermione.jpg')
    
    def __init__(self):
        # The super() function pulls in all the attributes of the parent class as well as all the function of the parent class. 
        super().__init__()

class Neville(Player):
    # Since this is a hard-coded string and will not change, it can be outside of the init.  It does not hurt to move it inside, but this can be here.
    name = "Neville Longbottom"
    imageFile = Image.open('images/neville.jpg')
    
    def __init__(self):
        # The super() function pulls in all the attributes of the parent class as well as all the function of the parent class. 
        super().__init__()

class Ron(Player):
    # Since this is a hard-coded string and will not change, it can be outside of the init.  It does not hurt to move it inside, but this can be here.
    name = "Ron Weasly"
    imageFile = Image.open('images/ron.jpg')
    
    def __init__(self):
        # The super() function pulls in all the attributes of the parent class as well as all the function of the parent class. 
        super().__init__()

 