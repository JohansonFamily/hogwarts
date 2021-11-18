from tkinter import *
from PIL import ImageTk, Image
#from tkmacosx import Button

import player
live_heart = '\u2764'; dead_heart = '\u2661'; location_symbol = '\u2620'; empty_location = '\u25cf'; zip_zap = '\u26a1'; coin = '\U0001FA99'

def startingScreen(root):

    # Selection variables for checkboxes
    arrayPlayerSelection= [IntVar(), IntVar(), IntVar(), IntVar()]
    arrayPlayerNames = ["Harry Potter", "Hermione Granger", "Neville Longbottom", "Ron Weasly"]
    nbrGame = IntVar()

    # Load picture files using pillow
    arrayImageFiles = [ImageTk.PhotoImage(Image.open('images/harry.jpg')), ImageTk.PhotoImage(Image.open('images/hermione.jpg')), ImageTk.PhotoImage(Image.open('images/neville.jpg')), ImageTk.PhotoImage(Image.open('images/ron.jpg'))]

    def showPlayerPics(col):
        # Use this if you want a consistent order
        if arrayPlayerSelection[col].get()==1: arrayImageList[col].grid(row=0, column=col)
        else: arrayImageList[col].grid_remove()

        # Use this if you want to select the order based on checkbox selection
        '''
        if arrayPlayerSelection[col].get()==1: arrayImageList[col].pack(side=LEFT)
        else: arrayImageList[col].pack_forget()
        '''
        
    def startEnter(e):
        startGame()

    def startGame():
        top_frame.destroy()
        bottom_frame.destroy()

        # Create Players
        global players
        players = []
        
        for i in range(0,4):
            if arrayPlayerSelection[i].get()==1: 
                #players[n]=player.Player(arrayPlayerNames[i])
                #players.append(player.Player(arrayPlayerNames[i]))
                if arrayPlayerNames[i]=="Harry Potter": players.append(player.Harry())
                if arrayPlayerNames[i]=="Hermione Granger": players.append(player.Hermione())
                if arrayPlayerNames[i]=="Neville Longbottom": players.append(player.Neville())
                if arrayPlayerNames[i]=="Ron Weasly": players.append(player.Ron())


        setupBoard(root, nbrGame.get())

    # Setup frames for starting screen
    top_frame = Frame(root, width=1500, height=700)
    top_frame.grid(row=0, column=0)
    top_frame.grid_columnconfigure(0,weight=4)
    top_frame.grid_columnconfigure(1,weight=1)
    top_frame.grid_columnconfigure(2,weight=3)
    top_frame.grid_rowconfigure(0,weight=6)
    top_frame.grid_rowconfigure(1,weight=1)
    top_frame.grid_rowconfigure(2,weight=1)
    top_frame.grid_rowconfigure(3,weight=1)
    top_frame.grid_rowconfigure(4,weight=1)
    top_frame.grid_rowconfigure(5,weight=1)
    top_frame.grid_rowconfigure(6,weight=1)
    top_frame.grid_rowconfigure(7,weight=1)
    top_frame.grid_rowconfigure(8,weight=1)
    top_frame.grid_rowconfigure(9,weight=1)
    
    top_frame.grid_propagate(0)
    bottom_frame = Frame(root, width=1500, height=300)
    bottom_frame.grid(row=1, column=0)

    # Load content for top frame
    txtWelcome = Label(top_frame, text="Welcome to the world of Hogwart's Battle!", font="Arial 46")
    txtWelcome.grid(columnspan=3,row=0, padx=0, pady=10, sticky=S)
    txtHowManyPlayers = Label(top_frame, text="Which brave heroes will be joining us?", font="Arial 24")
    txtHowManyPlayers.grid(columnspan=3,row=1,pady=20)
    ckbxHarry = Checkbutton(top_frame, text="Harry Potter", padx = 20, pady=0, variable=arrayPlayerSelection[0], command=lambda: showPlayerPics(0)).grid(column=1,row=3,sticky=W)
    ckbxHermione = Checkbutton(top_frame, text="Hermione Granger", padx = 20, pady=0, variable=arrayPlayerSelection[1], command=lambda: showPlayerPics(1)).grid(column=1,row=4,pady=0,sticky=W)
    ckbxNeville = Checkbutton(top_frame, text="Neville Longbottom", padx = 20, variable=arrayPlayerSelection[2], command=lambda: showPlayerPics(2)).grid(column=1,row=5,sticky=W)
    ckbxRon = Checkbutton(top_frame, text="Ron Weasly", padx = 20, variable=arrayPlayerSelection[3], command=lambda: showPlayerPics(3)).grid(column=1,row=6,sticky=W)
    txtWhichGame = Label(top_frame, text="Which game do you want to play?", font="Arial 18")
    txtWhichGame.grid(columnspan=3,row=7, pady=10)
    
    frame_game_selection = Frame(top_frame)
    frame_game_selection.grid(columnspan=3,row=8)
    for i in range(0,1):
        Radiobutton(frame_game_selection, text="Game "+str(i+1),variable=nbrGame, value=i+1).pack(side=LEFT)
    btnStart = Button(top_frame, text="Start Game", command=lambda: startGame()).grid(columnspan=3,row=9, pady=(30,5))
    root.bind('<Return>',startEnter)
    btnQuit = Button(top_frame, text="Quit", command=root.quit).grid(columnspan=3,row=10,column=0)

    # Create places for images to present
    arrayImageList = []
    for i in range(0,4): 
        arrayImageList.append(Label(bottom_frame, image=arrayImageFiles[i]))
        arrayImageList[i].image = arrayImageFiles[i]

    # Set defaults
    for i in range(0,4):
        arrayPlayerSelection[i].set(1)
        arrayImageList[i].grid(row=0, column=i)
    nbrGame.set(1)


        
def setupBoard(root, nbrGame):

    # Setup Images
    imgCardBackIcon = ImageTk.PhotoImage(Image.open('images/cards/card_back.jpg').resize((30,45), Image.ANTIALIAS))
    imgCardBackStore = ImageTk.PhotoImage(Image.open('images/cards/card_back.jpg').resize((90,120), Image.ANTIALIAS))

    frmPlayer = []
    playercnt = len(players)

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


    # Setup Active Player section

        

'''
class Board():

    def __init__(self):
'''