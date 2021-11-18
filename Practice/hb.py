from tkinter import *
import game
#from PIL import Image,ImageTk

root = Tk()
root.title('Hogwarts Battle')
root.geometry("1500x1000+100+100")
#root.config(bg='white')

def escape(e):
	root.quit()

root.bind("<Escape>", escape)

#Add fonts for all the widgets
root.option_add("*Font", "Arial 14")

# Setup initial root dimensions to span width of window
root.grid_rowconfigure(0,weight=1)
root.grid_rowconfigure(1,weight=1)
root.grid_columnconfigure(0,weight=1)

# Start Game
game.startingScreen(root)

mainloop()