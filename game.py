#import gui
import ui as gui
import player
import random
import cards

def selectGame(root):
    # Which games do we want to make available to the user?
    # Eventually, maybe we create a new intro screen with all the games available?
    # If we do that, we could create classes for each game with specific needs of that game.
    gameOptions = ["Game 1"]

    # Create list for all available players - this is specific to Game 1, but should be conditional at some point
    # Add all players we want to make available to the players list.
    # This also creates each player so the name and image are available
    players = [player.Harry(), player.Hermione(), player.Neville(), player.Ron()]

    # First step is to set up the intro screen that allows the user to pick players and game
    # Create a new instance of Board and store as mainBoard
    # We pass the main screen, the players we want them to select from, and the available games
    gui.StartingScreen(root, players, gameOptions)


def startGame(root, game, players):

    # Checks on the game selected and starts the right game
    if game == "Game 1":
        # Create a new instance of the game with the base screen and players selected.  The game knows the rest
        my_game = Game(root, players)
        # This line could be in the init, but I wanted to separate it for troubleshooting purposes.
        my_game.load_data()

class Game:
    # This section is for hard-coded variables or text strings that will never change and relate to all games.
    name = "Hogwart's Battle"
    creator = "Allison Johanson"
    supporter = "Matt Johanson"
    designer = "Michelle Johanson"
    tester = "Brian Johanson"
    detractor = "Izzy Johanson"
    mother = "Mary Johanson"

    def __init__(self, root, players):
        self.root = root
        # Player list is a key list that is managed by the game object
        self.players = players
        # ap is the active player.  All activity is with the active player.
        self.ap = players[0]
        self.cardDeck = self.getCardDeck()

        # self.villains = Villains()
        # self.locations = Locations()
        # self.darkArts = DarkArts()

        # One attribute of the game is the gameboard object.  All screen changes go through this gameboard.
        self.gb = gui.GameBoard(self)

        # Bind the enter key to the next turn function
        self.root.bind('<Return>', self.enterNext)


    def load_data(self):
        # Loads all data on the screen
        self.gb.location.loadContent()
        self.gb.darkArts.loadContent()
        self.gb.villains.loadContent()
        self.gb.cardStore.loadContent()
        self.gb.playerList.loadContent()
        self.gb.activePlayer.loadContent()

    def getCardDeck(self):
        # Set up cards available in the store
        cardDeck = []
        for i in range(0,6):
            cardDeck.append(cards.Alohamora())
            cardDeck.append(cards.Incendio())
        random.shuffle(cardDeck)
        return cardDeck

    def enterNext(self, e):
        # This is the function from the enter key to change turns
        self.nextTurn()

    def nextTurn(self):
        # change person's turn
        self.ap = self.players[(self.players.index(self.ap)+1) % len(self.players)]
        self.gb.activePlayer.loadContent()
        self.gb.playerList.loadContent()
