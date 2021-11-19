from tkinter import *
import gui
import player
# from PIL import Image,ImageTk


def createGame(root):
    Game(root)


def startGame(root, players):
    my_game = Game(root)

    my_game.startGame(players)


class Game:
    # This section is for hard-coded variables or text strings that will never change and relate to all games.
    name = "Hogwart's Battle"
    creator = "Allison Johanson"
    supporter = "Matt Johanson"
    designer = "Michelle Johanson"
    tester = "Brian Johanson"
    detractor = "Izzy Johanson"
    mother = "Mary Johanson"

    def __init__(self, root):
        self.root = root
        self.selectGame()
        # self.startGame()

    def selectGame(self):

        self.root.quit()  # Not sure why this doesn't work.  Should delete at some point

        # When debugging the front end, use this function to wait for you to perform the action
        '''
        def waitHere(t):
            var = IntVar()
            self.root.after(t, var.set, 1)
            print("waiting...")
            self.root.wait_variable(var)
        '''
        
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
        gui.StartingScreen(self.root, players, gameOptions)

        # The board should draw the main screen and allow the user to select players and the game
        # These print statements ensure the selection is stored as attributes of the class board
        # Comment out or delete these print statements once they work correctly
        
        try: 
            None
            # print(players)
            # print(main_board.gameSelection.get())
        except Exception as e: 
            print("ERROR: " + str(e))
            
    def startGame(self, players):
        Label(self.root, text=players[1].name).grid(row=0)
        # What logic needs to happen here to ensure the game starts?  

        # Call the ui subclass for the main board and the active player section        
