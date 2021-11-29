
import tkinter as tk
from PIL import ImageTk, Image

class DragManager():
    def add_dragable(self, widget):
        widget.bind("<ButtonPress-1>", self.on_start)
        widget.bind("<B1-Motion>", self.on_drag)
        widget.bind("<ButtonRelease-1>", self.on_drop)
        widget.configure(cursor="hand1")

    def on_start(self, event):
        # you could use this method to create a floating window
        # that represents what is being dragged.
        pass

    def on_drag(self, event):
        # you could use this method to move a floating window that
        # represents what you're dragging
        pass

    def on_drop(self, event):
        # find the widget under the cursor
        x,y = event.widget.winfo_pointerxy()
        target = event.widget.winfo_containing(x,y)
        print(x)
        try:
            #target.configure(image=event.widget.cget("image"))
            event.widget.place(x=x-100, y=y-120, anchor='nw')

        except Exception as e:
            print(e.args)


root = tk.Tk()
root.title('Hogwarts Battle')
root.geometry("1500x1000+100+100")
#root.config(bg='white')

def escape(e):
    root.quit()

def on_click(event):
    selected = mainCanvas.find_overlapping(event.x-0, event.y-0, event.x+0, event.y+0)
    if selected[-1] not in [bg, coin]:
        mainCanvas.selected = selected[-1]  # select the top-most item
        mainCanvas.startxy = (event.x, event.y)
        #print(mainCanvas.selected, mainCanvas.startxy)
    else:
        mainCanvas.selected = None

def on_drag(event):
    if mainCanvas.selected:
        # calculate distance moved from last position
        dx, dy = event.x-mainCanvas.startxy[0], event.y-mainCanvas.startxy[1]
        # move the selected item
        mainCanvas.move(mainCanvas.selected, dx, dy)
        # update last position
        mainCanvas.startxy = (event.x, event.y)

root.bind("<Escape>", escape)

#Add fonts for all the widgets
root.option_add("*Font", "Arial 14")

imgRaw = Image.open('../images/bg.jpg')
imgResized = imgRaw.resize((1500, 1000), Image.ANTIALIAS)
imgProcessed = ImageTk.PhotoImage(imgResized)

aimgRaw = Image.open('../images/coin.png')
aimgResized = aimgRaw.resize((50, 40), Image.ANTIALIAS)
aimgProcessed = ImageTk.PhotoImage(aimgResized)

# Setup initial root dimensions to span width of window
root.grid_rowconfigure(0,weight=1)
root.grid_columnconfigure(0,weight=1)

mainCanvas=tk.Canvas(root, height=1000, width=1500)
mainCanvas.place(x=0, y=0, anchor='nw')
bg = mainCanvas.create_image(0,0,image=imgProcessed, anchor='nw')
coin = mainCanvas.create_image(200,100,image=aimgProcessed, anchor='nw')
coin2 = mainCanvas.create_image(500,100,image=aimgProcessed, anchor='nw')

label = tk.Label(root, text="Hello World!")
label.place(x=100, y=100, anchor='nw')

dnd = DragManager()
dnd.add_dragable(label)
mainCanvas.bind("<Button-1>", on_click)
mainCanvas.bind("<B1-Motion>", on_drag)

tk.mainloop()


