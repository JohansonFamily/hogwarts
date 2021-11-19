from tkinter import *
import gui
import player
# from PIL import Image,ImageTk


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
    my_game = Game(root, game, players)

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

    def __init__(self, root, game, players):
        self.root = root
        self.game = game
        self.players = players
        self.startGame()


    def startGame(self):
        Label(self.root, text=self.players[1].name).grid(row=0)
        # What logic needs to happen here to ensure the game starts?  

        # Call the ui subclass for the main board and the active player section        
