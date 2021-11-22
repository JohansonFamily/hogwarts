import tkinter as tk
from PIL import ImageTk, Image
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
        self.parentFrame = tk.Frame(self.root, width=self.WIDTH, height=self.HEIGHT)
        self.parentFrame.grid(row=0)
        self.players = players
        self.gameOptions = gameOptions
        self.arrayImageList = []
        self.arrayPlayerSelection = []
        self.gameSelection = tk.IntVar()
        self.header = tk.Frame(self.parentFrame, width=self.WIDTH, height=100)
        self.start_top = tk.Frame(self.parentFrame, width=self.WIDTH, height=500)
        self.start_bottom = tk.Frame(self.parentFrame, width=self.WIDTH, height=400)
        self.header.grid_propagate(0)
        self.start_top.grid_propagate(0)
        self.start_bottom.grid_propagate(0)
        self.header.grid(row=0)
        self.setupTop()
        self.setupBottom()

    def close(self):
        self.parentFrame.destroy()

    def setupTop(self):

        # Setup frames for starting screen
        self.start_top.grid(row=1, column=0)
        self.start_top.grid_columnconfigure(0, weight=4)
        self.start_top.grid_columnconfigure(1, weight=1)
        self.start_top.grid_columnconfigure(2, weight=3)

        # Create widgets for top frame

        ## LABELS ##
        lblWelcome = tk.Label(self.start_top, text=self.txtWelcome, font="Arial 46")
        lblHowManyPlayers = tk.Label(self.start_top, text=self.txtHowManyPlayers, font="Arial 24")
        lblWhichGame = tk.Label(self.start_top, text=self.txtWhichGame, font="Arial 18")
        lblWelcome.grid(columnspan=3, row=0, padx=0, pady=10, sticky='S')
        lblHowManyPlayers.grid(columnspan=3, row=1, pady=20)
        lblWhichGame.grid(columnspan=3, row=7, pady=10)

        ## CHECKBOXES ##
        for i in range(len(self.players)):
            self.arrayPlayerSelection.append(tk.IntVar())

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
        ckbx = tk.Checkbutton(self.start_top, text=self.players[0].name, padx=20, pady=0,
                           variable=self.arrayPlayerSelection[0], command=lambda: self.showPlayerPics(0))
        ckbx.grid(column=1, row=0 + 3, sticky='W')
        ckbx = tk.Checkbutton(self.start_top, text=self.players[1].name, padx=20, pady=0,
                           variable=self.arrayPlayerSelection[1], command=lambda: self.showPlayerPics(1))
        ckbx.grid(column=1, row=1 + 3, sticky='W')
        ckbx = tk.Checkbutton(self.start_top, text=self.players[2].name, padx=20, pady=0,
                           variable=self.arrayPlayerSelection[2], command=lambda: self.showPlayerPics(2))
        ckbx.grid(column=1, row=2 + 3, sticky='W')
        ckbx = tk.Checkbutton(self.start_top, text=self.players[3].name, padx=20, pady=0,
                           variable=self.arrayPlayerSelection[3], command=lambda: self.showPlayerPics(3))
        ckbx.grid(column=1, row=3 + 3, sticky='W')

        ## GAME SELECTION ##
        frame_game_selection = tk.Frame(self.start_top)
        frame_game_selection.grid(columnspan=3, row=8)
        for i in range(0, len(self.gameOptions)):
            tk.Radiobutton(frame_game_selection, text=self.gameOptions[i], variable=self.gameSelection, value=i + 1)\
                .pack(side='left')

        ## START and QUIT ##
        tk.Button(self.start_top, text="Start Game", command=lambda: self.startGame()).grid(columnspan=3,
                                                                                         row=9, pady=(30, 5))
        self.root.bind('<Return>', self.startEnter)
        tk.Button(self.start_top, text="Quit", command=self.root.quit).grid(columnspan=3, row=10, column=0)

        # Set defaults
        self.gameSelection.set(1)

    def setupBottom(self):

        arrayImageFiles = []

        # Setup frames for pics
        self.start_bottom.grid(row=2, column=0)
        self.start_bottom.grid_columnconfigure(0, weight=100)
        self.start_bottom.grid_columnconfigure(1, weight=1)
        self.start_bottom.grid_columnconfigure(2, weight=1)
        self.start_bottom.grid_columnconfigure(3, weight=1)
        self.start_bottom.grid_columnconfigure(4, weight=1)
        self.start_bottom.grid_columnconfigure(5, weight=100)

        for i in range(len(self.players)):
            # Load picture files using pillow
            arrayImageFiles.append(ImageTk.PhotoImage(self.players[i].imageFile))

            # Create places for images to present
            self.arrayImageList.append(tk.Label(self.start_bottom, image=arrayImageFiles[i]))
            self.arrayImageList[i].image = arrayImageFiles[i]

            # Set defaults
            self.arrayPlayerSelection[i].set(1)
            #self.start_bottom.grid_columnconfigure(i+1, weight=1)
            self.arrayImageList[i].grid(row=0, column=i+1, pady=20)

    def showPlayerPics(self, col):
        # Use this if you want a consistent order
        if self.arrayPlayerSelection[col].get() == 1:
            self.arrayImageList[col].grid(row=0, column=col+1)
        else:
            self.arrayImageList[col].grid_remove()

    def startEnter(self, e):
        # Capture event and call startGame
        self.startGame()

    def startGame(self):
        self.header.destroy()
        self.start_top.destroy()
        self.start_bottom.destroy()
        self.parentFrame.destroy()

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
        self.parentFrame = tk.Frame(self.root, width=self.WIDTH, height=self.HEIGHT)
        self.parentFrame.grid_propagate(0)

        self.headerFrame = tk.LabelFrame(self.parentFrame, text="Header")
        self.locationFrame = tk.LabelFrame(self.parentFrame, text='Locations')
        self.darkArtsFrame = tk.LabelFrame(self.parentFrame, text="Dark Arts")
        self.cardStoreFrame = tk.LabelFrame(self.parentFrame, text="Card Store")
        self.villainsFrame = tk.LabelFrame(self.parentFrame, text="Villains")
        self.playerListFrame = tk.LabelFrame(self.parentFrame, text="Player List")
        self.activePlayerFrame = tk.LabelFrame(self.parentFrame, text="Active Player")

        self.header = Header(self.headerFrame)
        self.location = Location(self.locationFrame)
        self.darkArts = DarkArts(self.darkArtsFrame)
        self.cardStore = CardStore(self.cardStoreFrame)
        self.villains = Villains(self.villainsFrame)
        self.playerList = PlayerList(self.playerListFrame)
        self.activePlayer = ActivePlayer(self.activePlayerFrame)

        self.setupGameBoard()

    def setupGameBoard(self):
        self.parentFrame.grid(row=0)
        self.parentFrame.grid_rowconfigure(0, weight=1)
        self.parentFrame.grid_rowconfigure(1, weight=1)
        self.parentFrame.grid_rowconfigure(2, weight=1)
        self.parentFrame.grid_rowconfigure(3, weight=20)
        self.parentFrame.grid_columnconfigure(0, weight=2)
        self.parentFrame.grid_columnconfigure(1, weight=2)
        self.parentFrame.grid_columnconfigure(2, weight=1)
        self.parentFrame.grid_columnconfigure(3, weight=1)
        self.parentFrame.grid_columnconfigure(4, weight=10)

        self.headerFrame.grid(row=0,columnspan=5, padx=10, sticky="EW")
        self.locationFrame.grid(row=1, column=0, padx=10, sticky='NSEW')
        self.darkArtsFrame.grid(row=1, column=1, columnspan=2, padx=10, sticky='NSEW')
        self.villainsFrame.grid(row=2, columnspan=3, padx=10, sticky='NSEW')
        self.cardStoreFrame.grid(row=1, rowspan=2, column=3, padx=10, sticky='NSEW')
        self.playerListFrame.grid(row=1, rowspan=2, column=4, padx=10, sticky='NSEW')
        self.activePlayerFrame.grid(row=3, columnspan=5, padx=10, pady=10, sticky='NSEW')

class Header:

    def __init__(self,frame):
        self.frame = frame
        self.lbl = tk.Label(self.frame, text="Header information to go here.")
        self.lbl.grid(row=0,column=0)


class Location:

    def __init__(self, frame):
        self.frame = frame

    def loadContent(self):
        tk.Label(self.frame, text="Locations").grid(row=0)


class DarkArts:

    def __init__(self, frame):
        self.frame = frame

    def loadContent(self):

        tk.Label(self.frame, text="Dark Arts Events").grid(row=0)


class CardStore:

    def __init__(self, frame):
        self.frame = frame

    def loadContent(self, cardDeck):
        imgCardBack = Image.open('images/cards/card_back.jpg')
        # imgCardBackIcon = ImageTk.PhotoImage(imgCardBack.resize((30, 45), Image.ANTIALIAS))
        imgResized = imgCardBack.resize((90,120), Image.ANTIALIAS)
        imgCardBackStore = ImageTk.PhotoImage(imgResized)

        for i in range(0,6):
            img=tk.Label(self.frame, image=imgCardBackStore)
            img.image = imgCardBackStore
            if i==0:img.grid(row=0,column=0,padx=10,pady=10)
            if i==1:img.grid(row=0,column=1,padx=10,pady=10)
            if i==2:img.grid(row=1,column=0,padx=10,pady=10)
            if i==3:img.grid(row=1,column=1,padx=10,pady=10)
            if i==4:img.grid(row=2,column=0,padx=10,pady=10)
            if i==5:img.grid(row=2,column=1,padx=10,pady=10)



class Villains:

    def __init__(self, frame):
        self.frame = frame

    def loadContent(self):

        tk.Label(self.frame, text="This is for the Villains!").grid(row=0)

class PlayerList:

    def __init__(self, frame):
        self.frame = frame

    def loadContent(self):

        tk.Label(self.frame, text="This is for the Players!").grid(row=0)


class ActivePlayer:

    def __init__(self, frame):
        self.frame = frame

    def loadContent(self):

        tk.Label(self.frame, text="Active Player Data").grid(row=0)


