import tkinter as tk
from tkmacosx import Button
from PIL import ImageTk, Image
import game

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
        if selected[-1] != 1:
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


class GameBoard:

    def __init__(self, root):
        self.root = root

        imgRaw = Image.open('images/bg.jpg')
        imgResized = imgRaw.resize((1500, 1000), Image.ANTIALIAS)
        self.imgProcessed = ImageTk.PhotoImage(imgResized)

        self.mainCanvas = tk.Canvas(self.root, height=1000, width=1500
                                    , bd=0, highlightthickness=0, relief='ridge')
        self.mainCanvas.place(x=0, y=0, anchor='nw')
        self.mainCanvas.create_image(0, 0, image=self.imgProcessed, anchor='nw')



root = tk.Tk()
root.title('Hogwarts Battle')
root.geometry("1500x1000+100+100")
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

gb = GameBoard(root)

tk.mainloop()
