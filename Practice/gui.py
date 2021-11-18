from tkinter import *
from PIL import ImageTk, Image

import player


def startingScreen(root):

	# Selection variables for checkboxes
	arrayPlayerSelection= [IntVar(value=1), IntVar(), IntVar(), IntVar()]
	arrayPlayerNames = ["Harry Potter", "Hermione Granger", "Neville Longbottom", "Ron Weasly"]

	# Setup parent frame with 2 rows for two child frames
	frame_parent = LabelFrame(root, text='frame_parent', width=500)
	#frame_parent.grid_propagate(0)	
	frame_parent.grid(column=0,row=0)
	frame_parent.grid_rowconfigure(0, weight=1)
	frame_parent.grid_rowconfigure(1, weight=1)
	frame_parent.grid_columnconfigure(0, weight=1)

	# Setup top and bottom frames
	frame = LabelFrame(frame_parent, text='frame', width=1000)
	frame.grid(column=0,row=0)
	frame.grid_rowconfigure(0, weight=0)
	frame.grid_columnconfigure(0, weight=6)
	frame.grid_columnconfigure(1, weight=1)
	frame.grid_columnconfigure(2, weight=4)

	frame_pics = LabelFrame(frame_parent, text='frame_pics', width=1400)
	frame_pics.grid(column=0,row=1,pady=30)
	
	# Load picture files using pillow
	arrayImageFiles = [ImageTk.PhotoImage(Image.open('images/harry.jpg')), ImageTk.PhotoImage(Image.open('images/hermione.jpg')), ImageTk.PhotoImage(Image.open('images/neville.jpg')), ImageTk.PhotoImage(Image.open('images/ron.jpg'))]

	# Setup widgets in the top frame
	txtWelcome = Label(frame, text="Welcome to the world of Hogwart's Battle!", font="Arial 46")
	txtWelcome.grid(columnspan=3,row=0, padx=0, pady=0, sticky=S)
	txtHowManyPlayers = Label(frame, text="Which brave heroes will be joining us?", font="Arial 24").grid(columnspan=3,row=1,pady=20)
	ckbxHarry = Checkbutton(frame, text="Harry Potter", padx = 20, variable=arrayPlayerSelection[0], command=lambda: showPlayerPics(0)).grid(column=1,row=3,sticky=W)
	ckbxHermione = Checkbutton(frame, text="Hermione Granger", padx = 20, variable=arrayPlayerSelection[1], command=lambda: showPlayerPics(1)).grid(column=1,row=4,sticky=W)
	ckbxNeville = Checkbutton(frame, text="Neville Longbottom", padx = 20, variable=arrayPlayerSelection[2], command=lambda: showPlayerPics(2)).grid(column=1,row=5,sticky=W)
	ckbxRon = Checkbutton(frame, text="Ron Weasly", padx = 20, variable=arrayPlayerSelection[3], command=lambda: showPlayerPics(3)).grid(column=1,row=6,sticky=W)
	btnStart = Button(frame, text="Start Game", command=lambda: startGame()).grid(columnspan=3,row=7, pady=30)
	btnQuit = Button(frame, text="Quit", command=root.destroy)
	#btnQuit = Button(frame, text="Quit", command=root.destroy, highlightbackground='white', foreground='black')
	btnQuit.grid(columnspan=3, row=8,pady=0, sticky=N)
	
	# Create places for images to present
	arrayImageList = []
	for i in range(0,4): 
		arrayImageList.append(Label(frame_pics, image=arrayImageFiles[i]))
		arrayImageList[i].image = arrayImageFiles[i]

	def showPlayerPics(col):
		# Use this if you want a consistent order
		if arrayPlayerSelection[col].get()==1: arrayImageList[col].grid(row=0, column=col)
		else: arrayImageList[col].grid_remove()

		# Use this if you want to select the order based on checkbox selection
		'''
		if arrayPlayerSelection[col].get()==1: arrayImageList[col].pack(side=LEFT)
		else: arrayImageList[col].pack_forget()
		'''

	# I am only doing this to default one image so the text doesn't shift on me.  I am sure there is a better way, but this does work, so ¯\_(ツ)_/¯
	showPlayerPics(0)

	def startGame():
		# Remove initial player selection screen
		frame_parent.destroy()

		#setup active players here
		player_list = []
		if arrayPlayerSelection[0].get()==1: player_list.append(player.HarryPotter())
		if arrayPlayerSelection[1].get()==1: player_list.append(player.HermioneGranger())
		if arrayPlayerSelection[2].get()==1: player_list.append(player.NevilleLongbottom())
		if arrayPlayerSelection[3].get()==1: player_list.append(player.RonWeasly())

		# Setup default screen for game play
		defaultScreen(root, player_list)

def defaultScreen(root, player_list):

	# Setup parent frame with 2 rows for two child frames
	frame_parent = Frame(root)
	frame_parent.grid(column=0,row=0)
	frame_parent.grid_rowconfigure(1, weight=3)
	frame_parent.grid_rowconfigure(2, weight=1)
	frame_parent.grid_columnconfigure(0, weight=1)
	frame_parent.grid_columnconfigure(1, weight=4)

	# Setup internal frames
	frmPlayers = Frame(frame_parent)
	frmActive = Frame(frame_parent)
	frmBoard = Frame(frame_parent)

	frmPlayers.grid(column=0,row=1,rowspan=2)
	frmActive.grid(column=1,row=2)
	frmBoard.grid(column=1,row=1)

	#PlayerFrame(player.HarryPotter(), frmPlayers)
	

	def backtoStart():
		frame_parent.destroy()
		startingScreen(root)
	
	# Setup Header - decided the window title was duplicate
	#lblHeader = Label(frame_parent, text="HOGWART'S BATTLE", font="Arial 32")
	#lblHeader.grid(column=0, row=0, columnspan=2)

	

	# Setup player grid
	arrayPlayerFrames = []
	for i in range(len(player_list)):
		frmPlayer = LabelFrame(frmPlayers, text=player_list[i].name, width=400, height=(920-(20*(len(player_list)-1)))/len(player_list))
		frmPlayer.grid_propagate(0)
		frmPlayer.grid(row=i,column=0, padx=10, pady=10)
		#frmPlayer.grid_rowconfigure(i, weight=1)
		arrayPlayerFrames.append(frmPlayer)
		#Label(arrayPlayerFrames[i], text=player_list[i].name).grid(row=0,column=0, padx=10, pady=10, sticky=N)
		#Label(arrayPlayerFrames[i], text="Life: "+str(player_list[i].life)).grid(row=1,column=0,padx=10,pady=10, sticky=N)
	
	p1 = player.Player(arrayPlayerFrames[0])

	# Setup main board area
	lblFrame = LabelFrame(frmBoard, text="Game Board", width=1000, height=600)
	lblFrame.grid_propagate(0)
	lblFrame.grid(row=0,column=0, padx=10, pady=10)
	lbl = Label(lblFrame, text=player_list[0].name).grid(row=0,column=0, padx=10, pady=10)
	b=Button(lblFrame,text="Click Me!").grid(row=1)
	btnQuit = Button(lblFrame, text="Quit", command=root.quit).grid(row=2)
	
	# Setup Active player grid
	lblFrame2 = LabelFrame(frmActive, text="Active Player", width=1000, height=300)
	lblFrame2.grid_propagate(0)
	lblFrame2.grid(row=0,column=0, padx=10, pady=10)
	lbl2 = Label(lblFrame2, text=player_list[0].name).grid(row=0,column=0, padx=10, pady=10)
	b2=Button(lblFrame2,text="Click Me!").grid(row=1)
	btnQuit2 = Button(lblFrame2, text="Quit", command= lambda: backtoStart()).grid(row=2)


