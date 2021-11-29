import tkinter as tk
from tkmacosx import Button
from PIL import ImageTk, Image

class Imgbutton:

    def __init__(self, canvas, x, y, image, command=None):

        self.canvas = canvas
        self.x = x
        self.y = y
        self.image = image
        self.command = command

        img = self.canvas.create_image(self.x, self.y, image=self.image, anchor='nw')
        mainCanvas.tag_bind(img, "<1>", self.command)

        mainCanvas.bind("<Button-1>", on_click)
        mainCanvas.bind("<B1-Motion>", on_drag)

    def click(self):
        selected = mainCanvas.find_overlapping(event.x - 0, event.y - 0, event.x + 0, event.y + 0)
        if selected[-1] != 1:
            mainCanvas.selected = selected[-1]  # select the top-most item
            mainCanvas.startxy = (event.x, event.y)
            # print(mainCanvas.selected, mainCanvas.startxy)
        else:
            mainCanvas.selected = None

    def on_drag(event):
        if mainCanvas.selected:
            # calculate distance moved from last position
            dx, dy = event.x - mainCanvas.startxy[0], event.y - mainCanvas.startxy[1]
            # move the selected item
            mainCanvas.move(mainCanvas.selected, dx, dy)
            # update last position
            mainCanvas.startxy = (event.x, event.y)


def myfun(e):
    root.quit()

root = tk.Tk()
root.title('Hogwarts Battle')
root.geometry("1500x1000+100+100")
#root.wm_attributes('-transparentcolor','black')

imgRaw = Image.open('images/bg.jpg')
imgResized = imgRaw.resize((1500, 1000), Image.ANTIALIAS)
imgProcessed = ImageTk.PhotoImage(imgResized)

aimgRaw = Image.open('images/coin.png')
aimgResized = aimgRaw.resize((50, 40), Image.ANTIALIAS)
aimgProcessed = ImageTk.PhotoImage(aimgResized)

# This function, tied to the escape key, will end the entire program
def escape(e):
	try:
		root.quit()
	except Exception as exc:
		print(str(e.type) + ": " + str(exc))

# This ties the escape key to ending the program
root.bind("<Escape>", escape)
root.grid_rowconfigure(0, weight=1)
root.grid_rowconfigure(1, weight=1)

topframe = tk.Frame(root, width=1500, height=1000)
topframe.pack(fill='both', expand=True)
#tk.Label(topframe, text="Hello World!").grid(row=0)

# Display the image on a label
label = tk.Label(topframe, image=aimgProcessed, pady=50, bg='#eeefff')
# Set the label background color to a transparent color
label.config(bg='#eeefff')
label.pack()

bottomframe = tk.Frame(root, width=1500, height=500, bg='systemTransparent')
bottomframe.pack()

mainCanvas=tk.Canvas(bottomframe, height=1000, width=1500)
mainCanvas.place(x=0, y=0, anchor='nw')
btn = tk.Button(bottomframe, image=aimgProcessed, command=root.quit, bd=0, bg='#eeefff')
mainCanvas.create_image(0,0,image=imgProcessed, anchor='nw')
mainCanvas.create_image(200,100,image=aimgProcessed, anchor='nw')
mainCanvas.create_text(200, 200, text="Some text", fill='white')
mainCanvas.create_window(200,300, window=btn)
img = mainCanvas.create_image(200,100,image=aimgProcessed, anchor='nw')
mainCanvas.tag_bind(img, "<1>", myfun)
coin = Imgbutton(mainCanvas, 200, 400, aimgProcessed)

# img.config(bg='systemTransparent')


root.mainloop()