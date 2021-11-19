from tkinter import *
from PIL import ImageTk  # , Image
import game

# import random

live_heart = '\u2764'
dead_heart = '\u2661'
location_symbol = '\u2620'
empty_location = '\u25cf'
zip_zap = '\u26a1'
coin = '\U0001FA99'


class ParentScreen:
    ### CONSTANTS ###
    WIDTH = 1500
    HEIGHT = 1000

    def __init__(self, root):
        self.root = root
        self.parentFrame = Frame(self.root, width=self.WIDTH, height=self.HEIGHT)
        self.parentFrame.grid(row=0)

    def close(self):
        self.parentFrame.destroy()


class StartingScreen(ParentScreen):
    ### CONSTANTS ###
    txtWelcome = "Welcome to the world of Hogwart's Battle!"
    txtHowManyPlayers = "Which brave heroes will be joining us?"
    txtWhichGame = "Which game do you want to play?"

    def __init__(self, root, players, gameOptions):

        super().__init__(root)

        self.players = players
        self.gameOptions = gameOptions
        self.arrayImageList = []
        self.arrayPlayerSelection = []
        self.gameSelection = IntVar()
        self.start_top = Frame(self.parentFrame, width=self.WIDTH, height=600)
        self.start_bottom = Frame(self.parentFrame, width=self.WIDTH, height=400)
        self.setupTop()
        self.setupBottom()

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
            ckbx = Checkbutton(self.start_top, text=self.players[i].name, padx = 20, pady=0, variable=self.arrayPlayerSelection[i], command=lambda: self.showPlayerPics(i))
            ckbx.grid(column=1,row=i+3,sticky=W)
            print(i)
        '''

        # I don't know why this works, but the above code does not, but this should be something that we figure out and put into the above format so it can be dynamic with player changes.
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


class GameBoard(ParentScreen):
    """
    def __init__(self, root, players):

        super().__init__(root)

        self.players = players
        self.playercnt = len(players)

        # Setup Images
        self.imgCardBackIcon = ImageTk.PhotoImage(Image.open('images/cards/card_back.jpg').resize((30,45), Image.ANTIALIAS))
        self.imgCardBackStore = ImageTk.PhotoImage(Image.open('images/cards/card_back.jpg').resize((90,120), Image.ANTIALIAS))

        self.framePlayer = []

        # Setup main frames
        self.game_frame = Frame(self.parentFrame,width=1300,height=450)
        self.player_frame = Frame(root, width=1300, height=400)


    def addCardstoBuy():
        for i in range(0,6):
            img=Label(frmCardStore, image=imgCardBackStore)
            img.image = imgCardBackStore
            if i==0:img.grid(row=0,column=0,padx=10,pady=10)
            if i==1:img.grid(row=0,column=1,padx=10,pady=10)
            if i==2:img.grid(row=1,column=0,padx=10,pady=10)
            if i==3:img.grid(row=1,column=1,padx=10,pady=10)
            if i==4:img.grid(row=2,column=0,padx=10,pady=10)
            if i==5:img.grid(row=2,column=1,padx=10,pady=10)

    def addPlayerContent():
        for i in range(playercnt):
            Label(frmPlayer[i], text="Life: "+(dead_heart+' ')*(10-players[i].life)+(live_heart+' ')*players[i].life, foreground="red").grid(row=1,column=0,sticky=W,padx=20,pady=(5,0))
            Label(frmPlayer[i], text="Zip-zaps: "+str(players[i].zips)).grid(row=2,column=0,sticky=W,padx=20)
            Label(frmPlayer[i], text="Coins: "+str(players[i].coins)).grid(row=3,column=0,sticky=W,padx=20)
            #Label(frmPlayer[i], text="Cards: "+str(players[i].hand)).grid(row=0,rowspan=3,column=1,padx=20)
            img=Label(frmPlayer[i], image=imgCardBackIcon)
            img.image = imgCardBackIcon
            img.grid(row=0,rowspan=3,column=1,padx=20)

    def updatePlayerStats(i):

        players[i].damage(2)
        addPlayerContent()

    def selectPlayer(e):
        frmActivePlayer = LabelFrame(player_frame, text="Selected Player", width=1280, height=550)
        frmActivePlayer.grid(row=0,column=0)
        frmActivePlayer.grid_propagate(0)
        Button(frmActivePlayer, text="Quit", command=root.quit).grid(row=2)
        try:
            playernum=int(str(e.widget)[-1:])-1
        except Exception as e:
            playernum = 0
        Button(frmActivePlayer, text="Add Content to Player Sections", command=lambda: addPlayerContent()).grid(row=0)
        Button(frmActivePlayer, text="Update player stats for "+players[playernum].name, command=lambda: updatePlayerStats(playernum)).grid(row=1)


    # Setup main frames for starting screen
    game_frame = Frame(root, width=1300, height=450)
    game_frame.grid(row=0, column=0)
    game_frame.grid_columnconfigure(0,weight=1)
    game_frame.grid_columnconfigure(1,weight=1)
    game_frame.grid_columnconfigure(2,weight=1)
    game_frame.grid_columnconfigure(3,weight=1)
    game_frame.grid_rowconfigure(0,weight=1)
    game_frame.grid_rowconfigure(1,weight=1)
    game_frame.grid_propagate(0)
    player_frame = Frame(root, width=1300, height=400)
    player_frame.grid(row=1, column=0)
    player_frame.grid_columnconfigure(0,weight=1)
    player_frame.grid_rowconfigure(0,weight=1)
    player_frame.grid_propagate(0)

    frmLocations = LabelFrame(game_frame, text="Locations", width=200, height=200)
    frmLocations.grid(row=0,column=0)
    frmLocations.grid_propagate(0)
    Button(frmLocations, text="Quit", command=root.quit).grid(row=0,column=0)
    frmHorcrux = LabelFrame(game_frame, text="Horcrux", width=200, height=250)
    frmHorcrux.grid(row=1,column=0)
    frmHorcrux.grid_propagate(0)
    Button(frmHorcrux, text="Quit", command=root.quit).grid(row=0,column=0)
    frmDarkArts = LabelFrame(game_frame, text="Dark Arts Cards", width=300, height=450)
    frmDarkArts.grid(row=0,column=2,rowspan=2)
    frmDarkArts.grid_propagate(0)
    Button(frmDarkArts, text="Quit", command=root.quit).grid(row=0,column=0)
    frmCardStore = LabelFrame(game_frame, text="Cards for Purchase", width=230, height=450)
    frmCardStore.grid(row=0,column=3,rowspan=2, padx=20)
    frmCardStore.grid_propagate(0)
    addCardstoBuy()
    frmPlayers = Frame(game_frame, width=400, height=450)
    frmPlayers.grid(row=0,column=4,rowspan=2)
    frmPlayers.grid_propagate(0)
    Button(frmPlayers, text="Quit", command=root.quit).grid(row=0,column=0)

    # Setup Player section
    for i in range(playercnt):
        lblF = LabelFrame(frmPlayers, text = players[i].name,width=400, height=448/playercnt)
        lblF.grid(row=i,column=0)
        lblF.grid_propagate(0)
        lblF.bind("<Button-1>",selectPlayer)
        frmPlayer.append(lblF)

    addPlayerContent()
    #frmPlayer[0].event_generate("<Button-1>", when="tail")
    selectPlayer(1)
    """
