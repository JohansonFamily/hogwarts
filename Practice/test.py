'''
from tkinter import *
from PIL import Image, ImageTk


root = Tk()
root.title("Game")


frame = Frame(root)
frame.pack()


canvas = Canvas(frame, bg="black", width=700, height=400)
canvas.pack()

imgRaw = Image.open('images/bg.jpg')
imgResized = imgRaw.resize((50, 50), Image.ANTIALIAS)
imgProcessed = ImageTk.PhotoImage(imgResized)

bg = Image.open("images/bg.jpg")
background = ImageTk.PhotoImage(bg)
canvas.create_image(350,200,image=background)

character = Image.open('Practice/images/character.png')
imgResized = ImageTk.PhotoImage(character.resize((50, 50), Image.ANTIALIAS))
canvas.create_image(100,100,image=imgResized)

root.mainloop()
'''

'''
import tkinter as tk


root = tk.Tk()
root.geometry('250x200')
root.columnconfigure(0, weight=1)  # Used to allow column 0 in root to expand

some_frame = tk.LabelFrame(root, text='Hello')
some_frame.grid(row=0, column=0, sticky='ew')
some_frame.columnconfigure(1, weight=1)  # Used to allow column 1 in some_frame to expand

entry = tk.Entry(some_frame)
entry.grid(row=0, column=1)

root.mainloop()
'''

'''
import tkinter as tk
from tkinter import ttk


class App(tk.Tk):
    def __init__(self):
        super().__init__()

        # configure the root window
        self.title("Hogwart's Battle")
        self.geometry('1500x1000+100+100')

        # label
        self.label = ttk.Label(self, text='Hello, Tkinter!')
        self.label.pack()

        # button
        self.button = ttk.Button(self, text='Click Me')
        self.button['command'] = self.button_clicked
        self.button.pack()

    def button_clicked(self): self.quit()


if __name__ == "__main__":
    app = App()
    app.mainloop()

'''


'''



class MainApplication(tk.Frame):
    def __init__(self, parent, *args, **kwargs):
        tk.Frame.__init__(self, parent, *args, **kwargs)
        self.parent = parent

        <create the rest of your GUI here>

if __name__ == "__main__":
    root = tk.Tk()
    MainApplication(root).pack(side="top", fill="both", expand=True)
    root.mainloop()



class Navbar(tk.Frame): ...
class Toolbar(tk.Frame): ...
class StatusBar(tk.Frame): ...
class Main(tk.Frame): ...

class MainApplication(tk.Frame):
    def __init__(self, parent, *args, **kwargs):
        tk.Frame.__init__(self, parent, *args, **kwargs)
        self.statusbar = StatusBar(self, ...)
        self.toolbar = Toolbar(self, ...)
        self.navbar = Navbar(self, ...)
        self.main = Main(self, ...)

        self.statusbar.pack(side="bottom", fill="x")
        self.toolbar.pack(side="top", fill="x")
        self.navbar.pack(side="left", fill="y")
        self.main.pack(side="right", fill="both", expand=True)


'''


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
