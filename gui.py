import tkinter as tk
from tkmacosx import Button
from PIL import ImageTk, Image
import game
import random
import tkinter.messagebox as messagebox


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
            ckbx = tk.Checkbutton(self.start_top, text=self.players[i].name, padx = 20, pady=0,
                                        variable=self.arrayPlayerSelection[i], command=lambda i=i: self.showPlayerPics(i))
            ckbx.grid(column=1,row=i+3,sticky='W')

        ## GAME SELECTION ##
        frame_game_selection = tk.Frame(self.start_top)
        frame_game_selection.grid(columnspan=3, row=8)
        for i in range(len(self.gameOptions)):
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

    def __init__(self, game):

        self.root = game.root

        # establish parentFrame that will hold all gui elements
        self.parentFrame = tk.Frame(self.root, width=self.WIDTH, height=self.HEIGHT)
        self.parentFrame.grid_propagate(0)

        # Create frames for each section
        self.headerFrame = tk.LabelFrame(self.parentFrame, text="Header")
        self.locationFrame = tk.Frame(self.parentFrame)
        self.darkArtsFrame = tk.Frame(self.parentFrame)
        self.cardStoreFrame = tk.LabelFrame(self.parentFrame, text="Card Store")
        self.villainsFrame = tk.Frame(self.parentFrame)
        self.playerListFrame = tk.Frame(self.parentFrame)
        self.activePlayerFrame = tk.LabelFrame(self.parentFrame, text="Active Player")

        # Create objects for each section and pass in frame and appropriate data
        self.header = Header(self.headerFrame)
        self.location = Location(self.locationFrame)
        self.darkArts = DarkArts(self.darkArtsFrame, game)
        self.cardStore = CardStore(self.cardStoreFrame, game)
        self.villains = Villains(self.villainsFrame)
        self.playerList = PlayerList(self.playerListFrame, game)
        self.activePlayer = ActivePlayer(self.activePlayerFrame, game)
        self.pu = PopUp(game)

        # Place the objects on the game board
        self.setupGameBoard()

    def setupGameBoard(self):
        # Set up weights for each section
        self.parentFrame.grid(row=0)
        self.parentFrame.grid_rowconfigure(0, weight=1)
        self.parentFrame.grid_rowconfigure(1, weight=1)
        self.parentFrame.grid_rowconfigure(2, weight=1)
        self.parentFrame.grid_rowconfigure(3, weight=80)
        self.parentFrame.grid_columnconfigure(0, weight=2)
        self.parentFrame.grid_columnconfigure(1, weight=2)
        self.parentFrame.grid_columnconfigure(2, weight=1)
        self.parentFrame.grid_columnconfigure(3, weight=0)
        self.parentFrame.grid_columnconfigure(4, weight=5)

        # place each frame into the right section
        self.headerFrame.grid(row=0,columnspan=5, padx=10, sticky="EW")
        self.locationFrame.grid(row=1, column=0, padx=10, sticky='NSEW')
        self.darkArtsFrame.grid(row=1, column=1, columnspan=2, padx=10, sticky='NSEW')
        self.villainsFrame.grid(row=2, columnspan=3, padx=10, sticky='NSEW')
        self.cardStoreFrame.grid(row=1, rowspan=2, column=3, padx=10, sticky='NSEW')
        self.playerListFrame.grid(row=1, rowspan=2, column=4, padx=10, sticky='NSEW')
        self.activePlayerFrame.grid(row=3, columnspan=5, padx=10, pady=10, sticky='NSEW')


class Header:

    # This is for any admin function.  I am thinking save game or next turn???
    def __init__(self,frame):
        self.frame = frame
        self.lbl = tk.Label(self.frame, text="Header information to go here.")
        self.lbl.grid(row=0,column=0)


class Location:

    def __init__(self, frame):
        self.frame = frame

    def loadContent(self):
        imgRaw = Image.open('images/location1.png')
        imgResized = imgRaw.resize((220, 132), Image.ANTIALIAS)
        imgProcessed = ImageTk.PhotoImage(imgResized)

        imgLocation = tk.Label(self.frame, image=imgProcessed, padx=10)
        imgLocation.image = imgProcessed
        imgLocation.grid(row=0, padx=10, pady=10)


class DarkArts:

    def __init__(self, frame, game):
        self.frame = frame
        self.game = game
        self.draw = self.game.darkArtsDeck
        self.discard = []

    def loadContent(self):
        imgRaw = Image.open('images/cards/DarkArtsCardback.jpeg')
        imgResized = imgRaw.resize((140, 140), Image.ANTIALIAS)
        imgProcessed = ImageTk.PhotoImage(imgResized)

        # draw pile
        imgLocation = tk.Button(self.frame, image=imgProcessed, command=lambda: self.draw_card(self.game))
        imgLocation.image = imgProcessed
        imgLocation.grid(row=0, column=0, padx=10, pady=10)

        # discard pile
        if len(self.discard) == 0:
            imgFile = imgRaw
        else:
            imgFile = self.discard[len(self.discard)-1].imageFile

        imgResized = imgFile.resize((140, 140), Image.ANTIALIAS)
        imgProcessed = ImageTk.PhotoImage(imgResized)
        imgDarkArts = tk.Label(self.frame, image=imgProcessed)
        imgDarkArts.image = imgProcessed
        imgDarkArts.grid(row=0, column=1, padx=10, pady=10)

    def draw_card(self, game):
        if len(self.draw) == 0:
            self.draw = self.discard.copy()
            self.discard.clear()
            random.shuffle(self.draw)
        self.discard.append(self.draw[0])
        self.draw[0].use(game)
        self.draw.remove(self.draw[0])
        self.loadContent()
        self.game.gb.playerList.loadContent()
        self.game.gb.activePlayer.loadContent()



class CardStore:

    def __init__(self, frame, game):
        self.frame = frame
        self.game = game

    def loadContent(self):
        deck = self.game.cardDeck
        # layout cards
        for i in range(0,6):
            # Pull the image file from the card object, resize it to what we want, then use a button to display
            imgRaw = deck[i].imageFile
            imgResized = imgRaw.resize((90, 120), Image.ANTIALIAS)
            imgProcessed = ImageTk.PhotoImage(imgResized)
            img=tk.Button(self.frame, image=imgProcessed, bd=0,
#                       focuscolor='systemWindowBackgroundColor', activebackground='systemWindowBackgroundColor',
                       command=lambda i=i: self.use_card(deck[i]))
            img.image=imgProcessed
            img.grid(row=i//2,column=i%2,padx=5,pady=5)
            img.bind("<Enter>", lambda event, i=imgRaw: self.show_card(event, i))
            img.bind("<Leave>", self.hide_card)

    def show_card(self, e, img):
        imgRaw = img
        imgResized = imgRaw.resize((300,400), Image.ANTIALIAS)
        imgProcessed = ImageTk.PhotoImage(imgResized)
        self.imgLabel=tk.Label(self.game.root, image=imgProcessed)
        self.imgLabel.image = imgProcessed
        self.imgLabel.grid(row=0, column=0, pady=10, sticky='s')

    def hide_card(self, e):
        self.imgLabel.destroy()


    # This is what is called if someone clicks on the card
    def use_card(self, card):
        card.use(self.game.ap)
        self.game.gb.playerList.loadContent()
        self.game.gb.activePlayer.loadContent()


class Villains:

    def __init__(self, frame):
        self.frame = frame
        self.deck = []



    def loadContent(self):
        imgRaw = Image.open('images/cards/VillainCardback.jpeg')
        imgResized = imgRaw.resize((180, 100), Image.ANTIALIAS)
        imgProcessed = ImageTk.PhotoImage(imgResized)



        imgVillain = tk.Label(self.frame, image=imgProcessed)
        imgVillain.image = imgProcessed
        imgVillain.grid(row=0, column=0, padx=10, pady=10)
        imgVillain = tk.Label(self.frame, image=imgProcessed)
        imgVillain.image = imgProcessed
        imgVillain.grid(row=0, column=2, padx=10, pady=10)
        imgVillain = tk.Label(self.frame, image=imgProcessed)
        imgVillain.image = imgProcessed
        imgVillain.grid(row=1, column=0, padx=10, pady=10)
        imgVillain = tk.Label(self.frame, image=imgProcessed)
        imgVillain.image = imgProcessed
        imgVillain.grid(row=1, column=1, padx=10, pady=10)
        imgVillain = tk.Label(self.frame, image=imgProcessed)
        imgVillain.image = imgProcessed
        imgVillain.grid(row=1, column=2, padx=10, pady=10)


class PlayerList:

    def __init__(self, frame, game):
        self.frame = frame
        self.game = game
        self.lblFrame = []
        for i in range(len(self.game.players)):
            self.frame.grid_rowconfigure(i, weight=1)
            self.lblFrame.append(tk.LabelFrame(self.frame, text=self.game.players[i].name))
            self.lblFrame[i].grid(row=i, pady=5, sticky='NSEW')
            self.lblFrame[i].bind("<Button-1>", self.selectPlayer)
        self.loadContent()

    def loadContent(self):
        heartRaw = Image.open('images/heart.jpg')
        heartResized = heartRaw.resize((15, 15), Image.ANTIALIAS)
        heartProcessed = ImageTk.PhotoImage(heartResized)
        coinRaw = Image.open('images/coin.jpg')
        coinResized = coinRaw.resize((15, 15), Image.ANTIALIAS)
        coinProcessed = ImageTk.PhotoImage(coinResized)
        zipRaw = Image.open('images/zip.jpg')
        zipResized = zipRaw.resize((15, 15), Image.ANTIALIAS)
        zipProcessed = ImageTk.PhotoImage(zipResized)


        self.frame.grid_columnconfigure(0, weight=2)
        for i in range(len(self.game.players)):
            for widget in self.lblFrame[i].winfo_children():
                widget.destroy()
            lblLife = tk.Label(self.lblFrame[i], text="Health:  "+str(self.game.players[i].life))
            lblLife.grid(row=0, padx=10, pady=(5,0), sticky='w')
            lblCoins = tk.Label(self.lblFrame[i], text="Coins:  "+str(self.game.players[i].coins))
            lblCoins.grid(row=1, padx=10, sticky='w')
            lblZips = tk.Label(self.lblFrame[i], text="Zip-zaps: "+str(self.game.players[i].zips))
            lblZips.grid(row=2, padx=10, sticky='w')
            for j in range(self.game.players[i].life):
                heart = tk.Label(self.lblFrame[i], image=heartProcessed)
                heart.image = heartProcessed
                heart.grid(row=0, column=j+1)
            for j in range(min(10,self.game.players[i].coins)):
                coins = tk.Label(self.lblFrame[i], image=coinProcessed)
                coins.image = coinProcessed
                coins.grid(row=1, column=j+1)
            for j in range(min(10,self.game.players[i].zips)):
                zip = tk.Label(self.lblFrame[i], image=zipProcessed)
                zip.image = zipProcessed
                zip.grid(row=2, column=j+1)
            frmCards = tk.Frame(self.lblFrame[i], width=300, height=80)
            frmCards.grid(row=0, rowspan=3, column=12)
            frmCards.grid_columnconfigure(0, weight=1)
            frmCards.grid_rowconfigure(0, weight=1)
            frmCards.grid_propagate(0)

            lblCards = tk.Label(frmCards, text="  Cards in Hand: ", padx=5)
            #lblCards.pack()
            lblCards.place()
            for k in range(len(self.game.players[i].deck)):
                imgRaw = self.game.players[i].deck[k].imageFile
                imgResized = imgRaw.resize((60, 80), Image.ANTIALIAS)
                imgProcessed = ImageTk.PhotoImage(imgResized)
                img = tk.Label(frmCards, image=imgProcessed, bd=0)
                img.image = imgProcessed
                img.place(x=50+20*k, y=0)

    def selectPlayer(self, e):

        try:
            self.game.idxActivePlayer = int(str(e.widget)[-1:]) - 1
            self.game.ap = self.game.players[self.game.idxActivePlayer]
        except Exception as e:
            self.game.idxActivePlayer = 0
            self.game.ap = self.game.players[0]

        self.game.gb.activePlayer.loadContent()


class ActivePlayer:

    def __init__(self, frame, game):
        self.frame = frame
        self.game = game

    def loadContent(self):
        for widget in self.frame.winfo_children():
            widget.destroy()
        self.frame.config(text=self.game.ap.name)
        b1 = Button(self.frame, text="Hurt Player", width=200, height=100, bg='red',
             fg="white", command=lambda: self.damage(2))
        b1.grid(row=0)
        b2 = Button(self.frame, text="Heal Player", width=200, height=100,
                    bg='green', fg='white', command=lambda: self.heal(2))
        b2.grid(row=1)

        b3 = Button(self.frame, text="Popup", width=200, height=100,
                    bg='blue', fg='white', command=lambda: self.game.gb.pu.popUpCard())
        b3.grid(row=2, column=0)

        for i in range(len(self.game.ap.deck)):
            imgRaw = self.game.ap.deck[i].imageFile
            imgResized = imgRaw.resize((90, 120), Image.ANTIALIAS)
            imgProcessed = ImageTk.PhotoImage(imgResized)
            img = tk.Button(self.frame, image=imgProcessed, bd=0,
                            command=lambda i=i: self.use_card(self.game.ap.deck[i]))
            img.image = imgProcessed
            img.grid(row = 2, column=1+i)

    def use_card(self, card):
        card.use(self.game.ap)
        self.game.ap.deck.remove(card)
        self.game.gb.playerList.loadContent()
        self.game.gb.activePlayer.loadContent()

    def damage(self, nbr):
        self.game.ap.damage(nbr)
        self.game.gb.playerList.loadContent()

    def heal(self,nbr):
        self.game.ap.heal(nbr)
        self.game.gb.playerList.loadContent()


class PopUp:

    def __init__(self, game):
        self.game = game

    def popUpCard(self):
        # Toplevel object which will
        # be treated as a new window
        newWindow = tk.Toplevel(self.game.root)

        # sets the title of the
        # Toplevel widget
        newWindow.title("Choose")

        # sets the geometry of toplevel
        newWindow.geometry("300x300+600+500")
        newWindow.grid_columnconfigure(0, weight=1)
        newWindow.grid_columnconfigure(1, weight=1)
        lbl = tk.Label(newWindow, text="Would you prefer to lose 2 hearts or discard a card?", wraplength=260, padx=20, pady=20)
        lbl.grid(row=0, columnspan=2)
        b1 = tk.Button(newWindow, text="Lose 2 hearts")
        b1.grid(row=1, column=0)
        b2 = tk.Button(newWindow, text="Discard a card")
        b2.grid(row=1, column=1)


