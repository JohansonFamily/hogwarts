
from tkinter import *
import game

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
            target.configure(image=event.widget.cget("image"))
        except:
            pass


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
root.grid_columnconfigure(0,weight=1)

# Create a new game instance and start it.  Eventually, we can add loading a saved game or selecting the game here.
label = Label(root, text="Hello World!")
label.grid(row=0)

dnd = DragManager()
dnd.add_dragable(label)

mainloop()


