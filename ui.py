import tkinter as tk
from tkmacosx import Button
from PIL import ImageTk, Image

class Imgbutton(tk.Canvas):

    def __init__(self, master=None, image=None, command=None, **kw):

        # Declared style to keep a reference to the original relief
        style = kw.get("relief", "groove")

        if not kw.get('width') and image:
            kw['width'] = image.width()
        else: kw['width'] = 50

        if not kw.get('height') and image:
            kw['height'] = image.height()
        else: kw['height'] = 24

        kw['relief'] = style
        kw['borderwidth'] = kw.get('borderwidth', 2)
        kw['highlightthickness'] = kw.get('highlightthickness',0)

        super(Imgbutton, self).__init__(master=master, **kw)

        self.set_img = self.create_image(kw['borderwidth'], kw['borderwidth'],
                anchor='nw', image=image)

        self.bind_class( self, '<Button-1>',
                    lambda _: self.config(relief='sunken'), add="+")

        # Used the relief reference (style) to change back to original relief.
        self.bind_class( self, '<ButtonRelease-1>',
                    lambda _: self.config(relief=style), add='+')

        self.bind_class( self, '<Button-1>',
                    lambda _: command() if command else None, add="+")

def myfun(e):
    root.quit()

root = tk.Tk()
root.title('Hogwarts Battle')
root.geometry("1500x1000+100+100")
#root.wm_attributes('-transparentcolor','black')

imgRaw = Image.open('images/bg.jpg')
imgResized = imgRaw.resize((1500, 1000), Image.ANTIALIAS)
imgProcessed = ImageTk.PhotoImage(imgResized)

aimgRaw = Image.open('images/coin.jpg')
aimgResized = aimgRaw.resize((50, 50), Image.ANTIALIAS)
aimgProcessed = ImageTk.PhotoImage(aimgResized)

# This function, tied to the escape key, will end the entire program
def escape(e):
	try:
		root.quit()
	except Exception as exc:
		print(str(e.type) + ": " + str(exc))

# This ties the escape key to ending the program
root.bind("<Escape>", escape)

frame = tk.Frame(root, width=1500, height=1000, background="white")
frame.pack(fill='both', expand=True)

bottomframe = tk.Frame(root, width=1500, height=1000, bg='red')
bottomframe.pack()

mainCanvas=tk.Canvas(bottomframe, bg='white', height=1000, width=1500)
mainCanvas.place(x=0, y=0, anchor='nw')
btn = tk.Button(bottomframe, image=aimgProcessed, command=root.quit, bd=0)
mainCanvas.create_image(0,0,image=imgProcessed, anchor='nw')
mainCanvas.create_image(200,100,image=aimgProcessed, anchor='nw')
mainCanvas.create_text(200, 200, text="Some text", fill='white')
mainCanvas.create_window(200,300, window=btn)
img = mainCanvas.create_image(200,100,image=aimgProcessed, anchor='nw')
mainCanvas.tag_bind(img, "<1>", myfun)



'''
lbl = tk.Label(bottomframe, image=imgProcessed)
lbl.place(x=0,y=0)
lbl.image = imgProcessed
lbl=tk.Label(bottomframe, text='Hello World!', background='systemTransparent')
lbl.place(x=200, y=200)
'''

def creatLayers(no_of_layers, max_nodes_in_each_layer, frame1=bottomframe):

    listLayerRect=[]
    listDelimiterRect=[]

    #The canvas is created here.
    mainCanvas=tk.Canvas(frame1, bg="white", height=1000, width=1000)
    mainCanvas.pack(side='left')

    for i in range (0,no_of_layers):

        x=15*i

        #rectangles that are being drawn on the canvas.
        mainCanvas.create_polygon(x,0,x+10,0,x+10,1000,x,1000, outline='gray', fill='gray', width=2)

#        listLayerRect.append(Tkinter.Canvas(frame1, bg="blue", height=1000, width=30))
#        listDelimiterRect.append(Tkinter.Canvas(frame1, bg="yellow", height=1000, width=30))


L1 = tk.Label(frame, text="Layers")
E1 = tk.Entry(frame, bd =8)
L2 = tk.Label(frame, text="Layers2")

def helloCallBack(E=E1,):
   # tkMessageBox.showinfo( "Hello Python", "Hello World")
   k=int(E.get())
   print(k)

   creatLayers(k,k)

B = tk.Button(frame, text ="Enter", command = helloCallBack)

B.pack(side='left')
#L1.pack(side=LEFT)
E1.pack(side='left')
#L2.pack(side=LEFT)

root.mainloop()