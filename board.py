from tkinter import *
from PIL import ImageTk
#import cards

live_heart = '\u2764'; dead_heart = '\u2661'; location_symbol = '\u2620'; empty_location = '\u25cf'; zip_zap = '\u26a1'; coin = '\U0001FA99'

class Board():

    ### CONSTANTS ###
    WIDTH = 1500
    HEIGHT = 1000
    numberofgames = 1
    txtWelcome = "Welcome to the world of Hogwart's Battle!"
    txtHowManyPlayers= "Which brave heroes will be joining us?"
    txtWhichGame = "Which brave heroes will be joining us?"


    def __init__(self, root, players, gameOptions):

        self.root = root
        self.players = players
        self.gameOptions = gameOptions
        self.arrayImageList = []
        self.arrayPlayerSelection = [IntVar(), IntVar(), IntVar(), IntVar()]
        self.gameselection = IntVar()
        self.start_top = Frame(root, width=self.WIDTH, height=600)
        self.start_bottom = Frame(root, width=self.WIDTH, height=400)
        self.setupTop(root)
        self.setupBottom(root)
        
 

    def setupTop(self, root):

        # Setup frames for starting screen
        self.start_top.grid(row=0,column=0)
        self.start_top.grid_columnconfigure(0,weight=4)
        self.start_top.grid_columnconfigure(1,weight=1)
        self.start_top.grid_columnconfigure(2,weight=3)
        self.start_top.grid_rowconfigure(0,weight=6)
        self.start_top.grid_rowconfigure(1,weight=1)
        self.start_top.grid_rowconfigure(2,weight=1)
        self.start_top.grid_rowconfigure(3,weight=1)
        self.start_top.grid_rowconfigure(4,weight=1)
        self.start_top.grid_rowconfigure(5,weight=1)
        self.start_top.grid_rowconfigure(6,weight=1)
        self.start_top.grid_rowconfigure(7,weight=1)
        self.start_top.grid_rowconfigure(8,weight=1)
        self.start_top.grid_rowconfigure(9,weight=1)
        self.start_top.grid_propagate(0)

        # Create widgets for top frame

        ## LABELS ##
        lblWelcome = Label(self.start_top, text=self.txtWelcome, font="Arial 46")
        lblHowManyPlayers = Label(self.start_top, text=self.txtHowManyPlayers, font="Arial 24")
        lblWhichGame = Label(self.start_top, text=self.txtWhichGame, font="Arial 18")
        lblWelcome.grid(columnspan=3,row=0, padx=0, pady=10, sticky=S)
        lblHowManyPlayers.grid(columnspan=3,row=1,pady=20)
        lblWhichGame.grid(columnspan=3,row=7, pady=10)
        
        ## CHECKBOXES ##
        '''
        TODO
        for i in range(len(self.players)):
            ckbx = Checkbutton(self.start_top, text=self.players[i].name, padx = 20, pady=0, variable=self.arrayPlayerSelection[i], command=lambda: self.showPlayerPics(i))
            ckbx.grid(column=1,row=i+3,sticky=W)
            print(i)
        '''
        # I don't know why this works, but the above code does not, but this should be something that we figure out and put into the above format so it can be dynamic with player changes.
        ckbx = Checkbutton(self.start_top, text=self.players[0].name, padx = 20, pady=0, variable=self.arrayPlayerSelection[0], command=lambda: self.showPlayerPics(0))
        ckbx.grid(column=1,row=0+3,sticky=W)
        ckbx = Checkbutton(self.start_top, text=self.players[1].name, padx = 20, pady=0, variable=self.arrayPlayerSelection[1], command=lambda: self.showPlayerPics(1))
        ckbx.grid(column=1,row=1+3,sticky=W)
        ckbx = Checkbutton(self.start_top, text=self.players[2].name, padx = 20, pady=0, variable=self.arrayPlayerSelection[2], command=lambda: self.showPlayerPics(2))
        ckbx.grid(column=1,row=2+3,sticky=W)
        ckbx = Checkbutton(self.start_top, text=self.players[3].name, padx = 20, pady=0, variable=self.arrayPlayerSelection[3], command=lambda: self.showPlayerPics(3))
        ckbx.grid(column=1,row=3+3,sticky=W)

        ## GAME SELECTION ##
        frame_game_selection = Frame(self.start_top)
        frame_game_selection.grid(columnspan=3,row=8)
        for i in range(0,len(self.gameOptions)):
            Radiobutton(frame_game_selection, text=self.gameOptions[i],variable=self.gameselection, value=i+1).pack(side=LEFT)

        ## START and QUIT ##
        btnStart = Button(self.start_top, text="Start Game", command=lambda: self.startGame()).grid(columnspan=3,row=9, pady=(30,5))
        root.bind('<Return>',self.startEnter)
        btnQuit = Button(self.start_top, text="Quit", command=root.quit).grid(columnspan=3,row=10,column=0)

        # Set defaults
        self.gameselection.set(1)

    def setupBottom(self, root):

        arrayImageFiles = []

        # Load picture files using pillow
        for i in range(len(self.players)):
            arrayImageFiles.append(ImageTk.PhotoImage(self.players[i].imageFile))
            #arrayImageFiles = [ImageTk.PhotoImage(Image.open('images/harry.jpg')), ImageTk.PhotoImage(Image.open('images/hermione.jpg')), ImageTk.PhotoImage(Image.open('images/neville.jpg')), ImageTk.PhotoImage(Image.open('images/ron.jpg'))]

        # Setup frames for pics
        self.start_bottom.grid(row=1, column=0)

        # Create places for images to present
        arrayImageList = []
        for i in range(len(self.players)): 
            self.arrayImageList.append(Label(self.start_bottom, image=arrayImageFiles[i]))
            self.arrayImageList[i].image = arrayImageFiles[i]

        # Set defaults
        for i in range(len(self.players)):
            self.arrayPlayerSelection[i].set(1)
            self.arrayImageList[i].grid(row=0, column=i)

    def showPlayerPics(self, col):
        # Use this if you want a consistent order
        if self.arrayPlayerSelection[col].get()==1: self.arrayImageList[col].grid(row=0, column=col)
        else: self.arrayImageList[col].grid_remove()

        # Use this if you want to select the order based on checkbox selection
        '''
        if arrayPlayerSelection[col].get()==1: arrayImageList[col].pack(side=LEFT)
        else: arrayImageList[col].pack_forget()
        '''
        
    def startEnter(e):
        e.startGame()

    def startGame(self):
        self.start_top.destroy()
        self.start_bottom.destroy()

        # Establish final list of players
        for i in reversed(range(len(self.players))):
            if self.arrayPlayerSelection[i].get()==0:
                del self.players[i]
        


    