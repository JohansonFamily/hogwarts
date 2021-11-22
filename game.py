import gui
import player
from tkinter import messagebox

def selectGame(root):
    # Which games do we want to make available to the user?
    # Eventually, maybe we create a new intro screen with all the games available?
    # If we do that, we could create subclasses for each game with specific needs of that game.
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

    if game == "Game 1":
        my_game = Game(root, players)
        my_game.startGame()


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
        self.players = players
        # self.cards = Cards()
        # self.villains = Villains()
        # self.locations = Locations()
        # self.darkArts = DarkArts()
        self.gb = gui.GameBoard(self.root)


    def startGame(self):
        self.gb.location.loadContent()
        self.gb.darkArts.loadContent()
        self.gb.villains.loadContent()
        self.gb.cardStore.loadContent()
        self.gb.playerList.loadContent()
        self.gb.activePlayer.loadContent()
        #messagebox.showinfo("showinfo", "Information")
        # for i in range(len(self.players)):
        #    Label(self.root, text=self.players[i].name).grid(row=i)
        # What logic needs to happen here to ensure the game starts?  

        # Call the ui subclass for the gui and the active player section
