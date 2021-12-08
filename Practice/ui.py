import tkinter as tk
from tkmacosx import Button
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


class Imgbutton:

    def __init__(self, canvas, x, y, image, command=None):

        self.canvas = canvas
        self.x = x
        self.y = y
        self.image = image
        self.command = command

        img = self.canvas.create_image(self.x, self.y, image=self.image, anchor='nw')
        self.canvas.tag_bind(img, "<1>", self.command)

        self.canvas.bind("<Button-1>", self.on_click)
        self.canvas.bind("<B1-Motion>", self.on_drag)

    def on_click(self, e):
        selected = self.canvas.find_overlapping(event.x - 0, event.y - 0, event.x + 0, event.y + 0)
        if selected[-1]:
            self.canvas.selected = selected[-1]  # select the top-most item
            self.canvas.startxy = (event.x, event.y)
            # print(mainCanvas.selected, mainCanvas.startxy)
        else:
            self.canvas.selected = None

    def on_drag(event, e):
        if self.canvas.selected:
            # calculate distance moved from last position
            dx, dy = event.x - self.canvas.startxy[0], event.y - self.canvas.startxy[1]
            # move the selected item
            self.canvas.move(self.canvas.selected, dx, dy)
            # update last position
            self.canvas.startxy = (event.x, event.y)

class ImgBG:

    def __init__(self, canvas):

        self.canvas = canvas

        self.setup()

    def setup(self):
        imgRaw = Image.open('../images/bg.jpg')
        imgResized = imgRaw.resize((1800, 1100), Image.ANTIALIAS)
        self.bg = ImageTk.PhotoImage(imgResized)

        imgRaw = Image.open('../images/game_board.png')
        imgResized = imgRaw.resize((1000, 600), Image.ANTIALIAS)
        self.gb = ImageTk.PhotoImage(imgResized)

        imgRaw = Image.open('../images/player_board.png')
        imgResized = imgRaw.resize((480, 200), Image.ANTIALIAS)
        self.pb = ImageTk.PhotoImage(imgResized)

        imgRaw = Image.open('../images/location1.png')
        imgResized = imgRaw.resize((170, 120), Image.ANTIALIAS)
        self.loc1 = ImageTk.PhotoImage(imgResized)

        imgRaw = Image.open('../images/cards/VillainCardback.jpeg')
        imgResized = imgRaw.resize((170, 110), Image.ANTIALIAS)
        self.vil = ImageTk.PhotoImage(imgResized)

        imgRaw = Image.open('../images/dark arts/DarkArtsCardback.jpeg')
        imgResized = imgRaw.resize((120, 110), Image.ANTIALIAS)
        self.da = ImageTk.PhotoImage(imgResized)

        imgRaw = Image.open('../images/cards/HogwartsCardback.jpeg')
        imgResized = imgRaw.resize((90, 120), Image.ANTIALIAS)
        self.hb = ImageTk.PhotoImage(imgResized)

        imgRaw = Image.open('../images/heart.png')
        imgResized = imgRaw.resize((40, 40), Image.ANTIALIAS)
        self.health = ImageTk.PhotoImage(imgResized)

        imgRaw = Image.open('../images/players/harry/harry_card.png')
        imgResized = imgRaw.resize((200, 150), Image.ANTIALIAS)
        self.pc = ImageTk.PhotoImage(imgResized)

    def place(self, x, y, image):
        self.x = x
        self.y = y
        self.image = image

        self.canvas.create_image(self.x, self.y, image=self.image, anchor='nw')

class GameBoard:
    def __init__(self, game):
        self.root = root

        # establish parentFrame that will hold all gui elements
        self.canvas = tk.Canvas(self.root, width=self.WIDTH, height=self.HEIGHT)


class xGameBoard:

    def __init__(self, root):
        self.root = root

        self.mainCanvas = tk.Canvas(self.root, height=1100, width=1800
                                    , bd=0, highlightthickness=0, relief='ridge')
        self.mainCanvas.place(x=0, y=0, anchor='nw')
        self.images = ImgBG(self.mainCanvas)

        self.place_initial_images()
        self.place_player_list()
        self.frame = tk.Frame(self.root, width=700, height=300)
        self.frame.grid_propagate(0)
        self.mainCanvas.create_window(1050, 300, window=self.frame, anchor='nw')
        self.place_player_frame()

    def place_initial_images(self):
        self.images.place(0, 0, self.images.bg)
        self.images.place(10, 10, self.images.gb)
        self.images.place(500, 650, self.images.pb)
        self.images.place(38, 110, self.images.loc1)
        self.images.place(38,250,self.images.vil)
        self.images.place(315, 110, self.images.da)
        self.images.place(780, 35, self.images.hb)
        self.images.place(520, 670, self.images.health)
        self.images.place(25, 620, self.images.pc)
        self.images.place(380, 700, self.images.hb)

    def place_player_list(self):
        spacing = 20
        width = 140
        startpos = 20
        for i in range(0,2):
            self.mainCanvas.create_rectangle(1050, startpos, 1750, startpos+width
                                             , width=2, outline='white', tags='Hello World')
            self.mainCanvas.create_text(1100, startpos-10, text="Harry Potter", fill='white')
            startpos = startpos+spacing+width

    def place_player_frame(self):
        self.lblFrame = []
        for i in range(0,2):
            self.frame.grid_rowconfigure(i, weight=1)
            self.lblFrame.append(tk.LabelFrame(self.frame, text="Harry Potter"))
            self.lblFrame[i].grid(row=i, pady=0, sticky='NSEW')
            # self.lblFrame[i].bind("<Button-1>", self.selectPlayer)

        heartRaw = Image.open('../images/heart.jpg')
        heartResized = heartRaw.resize((15, 15), Image.ANTIALIAS)
        heartProcessed = ImageTk.PhotoImage(heartResized)
        coinRaw = Image.open('../images/coin.jpg')
        coinResized = coinRaw.resize((15, 15), Image.ANTIALIAS)
        coinProcessed = ImageTk.PhotoImage(coinResized)
        zipRaw = Image.open('../images/zip.jpg')
        zipResized = zipRaw.resize((15, 15), Image.ANTIALIAS)
        zipProcessed = ImageTk.PhotoImage(zipResized)

        self.frame.grid_columnconfigure(0, weight=2)
        for i in range(0,2):
            for widget in self.lblFrame[i].winfo_children():
                widget.destroy()
            lblLife = tk.Label(self.lblFrame[i], text="Health:  " + str(4))
            lblLife.grid(row=0, padx=10, pady=(5, 0), sticky='w')
            lblCoins = tk.Label(self.lblFrame[i], text="Coins:  " + str(2))
            lblCoins.grid(row=1, padx=10, sticky='w')
            lblZips = tk.Label(self.lblFrame[i], text="Zip-zaps: " + str(1))
            lblZips.grid(row=2, padx=10, sticky='w')
            for j in range(4):
                heart = tk.Label(self.lblFrame[i], image=heartProcessed)
                heart.image = heartProcessed
                heart.grid(row=0, column=j + 1)
            for j in range(min(10, 2)):
                coins = tk.Label(self.lblFrame[i], image=coinProcessed)
                coins.image = coinProcessed
                coins.grid(row=1, column=j + 1)
            for j in range(min(10, 1)):
                zip = tk.Label(self.lblFrame[i], image=zipProcessed)
                zip.image = zipProcessed
                zip.grid(row=2, column=j + 1)


root = tk.Tk()
root.title('Hogwarts Battle')
root.geometry("1800x1100+100+50")
# removes header
#root.overrideredirect(0)

# root.config(bg='white')

# This function, tied to the escape key, will end the entire program
def escape(e):
	try:
		root.quit()
	except Exception as exc:
		print(str(e.type) + ": " + str(exc))

# This ties the escape key to ending the program
root.bind("<Escape>", escape)

# Add fonts for all the widgets
root.option_add("*Font", "Arial 14")

# Setup initial root dimensions to span width of window
root.grid_rowconfigure(0, weight=1)
root.grid_columnconfigure(0, weight=1)

# Create a new game instance and start it.  Eventually, we can add loading a saved game or selecting the game here.
# game.selectGame(root)

gb = xGameBoard(root)

tk.mainloop()
