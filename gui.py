from tkinter import *
from PIL import ImageTk  # , Image
import game

class StartingScreen:
    ### CONSTANTS ###
    txtWelcome = "Welcome to the world of Hogwart's Battle!"
    txtHowManyPlayers = "Which brave heroes will be joining us?"
    txtWhichGame = "Which game do you want to play?"
    WIDTH = 1500
    HEIGHT = 1000

    def __init__(self, root, players, gameOptions):

        self.root = root
        self.parentFrame = Frame(self.root, width=self.WIDTH, height=self.HEIGHT)
        self.parentFrame.grid(row=0)
        self.players = players
        self.gameOptions = gameOptions
        self.arrayImageList = []
        self.arrayPlayerSelection = []
        self.gameSelection = IntVar()
        self.start_top = Frame(self.parentFrame, width=self.WIDTH, height=600)
        self.start_bottom = Frame(self.parentFrame, width=self.WIDTH, height=400)
        self.setupTop()
        self.setupBottom()

    def close(self):
        self.parentFrame.destroy()

    def setupTop(self):

        # Setup frames for starting screen
        self.start_top.grid(row=0, column=0)
        self.start_top.grid_columnconfigure(0, weight=4)
        self.start_top.grid_columnconfigure(1, weight=1)
        self.start_top.grid_columnconfigure(2, weight=3)

        # Create widgets for top frame

        ## LABELS ##
        lblWelcome = Label(self.start_top, text=self.txtWelcome, font="Arial 46")
        lblHowManyPlayers = Label(self.start_top, text=self.txtHowManyPlayers, font="Arial 24")
        lblWhichGame = Label(self.start_top, text=self.txtWhichGame, font="Arial 18")
        lblWelcome.grid(columnspan=3, row=0, padx=0, pady=10, sticky=S)
        lblHowManyPlayers.grid(columnspan=3, row=1, pady=20)
        lblWhichGame.grid(columnspan=3, row=7, pady=10)

        ## CHECKBOXES ##
        for i in range(len(self.players)):
            self.arrayPlayerSelection.append(IntVar())

        '''

        # TODO
        for i in range(len(self.players)):
            ckbx = Checkbutton(self.start_top, text=self.players[i].name, padx = 20, pady=0, 
                                        variable=self.arrayPlayerSelection[i], command=lambda: self.showPlayerPics(i))
            ckbx.grid(column=1,row=i+3,sticky=W)
            print(i)
        '''

        # I don't know why this works, but the above code does not work,
        # but this should be something that we should figure out
        # and put into the above format so it can be dynamic with player changes.
        ckbx = Checkbutton(self.start_top, text=self.players[0].name, padx=20, pady=0,
                           variable=self.arrayPlayerSelection[0], command=lambda: self.showPlayerPics(0))
        ckbx.grid(column=1, row=0 + 3, sticky=W)
        ckbx = Checkbutton(self.start_top, text=self.players[1].name, padx=20, pady=0,
                           variable=self.arrayPlayerSelection[1], command=lambda: self.showPlayerPics(1))
        ckbx.grid(column=1, row=1 + 3, sticky=W)
        ckbx = Checkbutton(self.start_top, text=self.players[2].name, padx=20, pady=0,
                           variable=self.arrayPlayerSelection[2], command=lambda: self.showPlayerPics(2))
        ckbx.grid(column=1, row=2 + 3, sticky=W)
        ckbx = Checkbutton(self.start_top, text=self.players[3].name, padx=20, pady=0,
                           variable=self.arrayPlayerSelection[3], command=lambda: self.showPlayerPics(3))
        ckbx.grid(column=1, row=3 + 3, sticky=W)

        ## GAME SELECTION ##
        frame_game_selection = Frame(self.start_top)
        frame_game_selection.grid(columnspan=3, row=8)
        for i in range(0, len(self.gameOptions)):
            Radiobutton(frame_game_selection, text=self.gameOptions[i], variable=self.gameSelection, value=i + 1).pack(
                side=LEFT)

        ## START and QUIT ##
        Button(self.start_top, text="Start Game", command=lambda: self.startGame()).grid(columnspan=3,
                                                                                         row=9, pady=(30, 5))
        self.root.bind('<Return>', self.startEnter)
        Button(self.start_top, text="Quit", command=self.root.quit).grid(columnspan=3, row=10, column=0)

        # Set defaults
        self.gameSelection.set(1)

    def setupBottom(self):

        arrayImageFiles = []

        # Setup frames for pics
        self.start_bottom.grid(row=1, column=0)

        for i in range(len(self.players)):
            # Load picture files using pillow
            arrayImageFiles.append(ImageTk.PhotoImage(self.players[i].imageFile))

            # Create places for images to present
            self.arrayImageList.append(Label(self.start_bottom, image=arrayImageFiles[i]))
            self.arrayImageList[i].image = arrayImageFiles[i]

            # Set defaults
            self.arrayPlayerSelection[i].set(1)
            self.arrayImageList[i].grid(row=0, column=i, pady=20)

    def showPlayerPics(self, col):
        # Use this if you want a consistent order
        if self.arrayPlayerSelection[col].get() == 1:
            self.arrayImageList[col].grid(row=0, column=col)
        else:
            self.arrayImageList[col].grid_remove()

    def startEnter(self, e):
        # Capture event and call startGame
        self.startGame()

    def startGame(self):
        self.start_top.destroy()
        self.start_bottom.destroy()

        # Establish final list of players
        for i in reversed(range(len(self.players))):
            if self.arrayPlayerSelection[i].get() == 0:
                del self.players[i]

        game.startGame(self.root, self.gameOptions[self.gameSelection.get()-1], self.players)


class GameBoard:

    WIDTH = 1500
    HEIGHT = 1000

    def __init__(self, root):

        self.root = root
        self.parentFrame = Frame(self.root, width=self.WIDTH, height=self.HEIGHT)
        self.parentFrame.grid_propagate(0)

        self.locationFrame = Frame(self.parentFrame)
        self.darkArtsFrame = Frame(self.parentFrame)

        self.location = Location(self.locationFrame)
        self.darkArts = DarkArts(self.darkArtsFrame)

        self.setupGameBoard()
        # self.cardStore = CardStoreFrame(self.parentFrame)
        # self.villians = VillainFrame(self.parentFrame)
        # self.playersframe = PlayersFrame(self.parentFrame)
        # self.activeplayer = ActivePlayerFrame(self.parentFrame)

    def setupGameBoard(self):
        self.parentFrame.grid(row=0)
        self.parentFrame.grid_rowconfigure(0, weight=1)
        self.parentFrame.grid_rowconfigure(1, weight=4)
        self.parentFrame.grid_rowconfigure(2, weight=3)
        self.locationFrame.grid(row=1, column=0)
        self.darkArtsFrame.grid(row=1, column=1)

class Location:

    def __init__(self, frame):
        self.frame = frame

    def loadContent(self):
        lf = LabelFrame(self.frame, text="Locations")
        lf.grid(row=0, column=0)
        Label(lf, text="Hello harry").grid(row=0)


class DarkArts:

    def __init__(self, frame):
        self.frame = frame

    def loadContent(self):

        lf = LabelFrame(self.frame, text="Cards")
        lf.grid(row=0, column=0)
        Label(lf, text="Goodbye Hermione!").grid(row=0)





class ActivePlayerBoard:
    def __init__(self, root):
        self.root = root



