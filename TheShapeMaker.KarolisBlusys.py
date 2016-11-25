import tkinter as tk
from tkinter import *
import tkinter.messagebox
trace = 0

TITLE_FONT = ("Helvetica", 22, "bold")
#Creates the canvas for the shapes
canvas = Canvas(width=800, height=800)


class SampleApp(tk.Tk):

    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)

        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}
        for F in (StartPage, PageOne, PageTwo):
            page_name = F.__name__
            frame = F(parent=container, controller=self)
            self.frames[page_name] = frame

            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame("StartPage")

    def show_frame(self, page_name):
        '''Show a frame for the given page name'''
        frame = self.frames[page_name]
        frame.tkraise()

#Paramaters for the start page
class StartPage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        label = tk.Label(self, text="Welcome to the shape creator!", font=TITLE_FONT)
        label.pack(side="top", fill="x", pady=10)
       
#Button input
        button1 = tk.Button(self, text="Game rules",
                            command=lambda: controller.show_frame("PageOne"))

       
        button2 = tk.Button(self, command=lambda: controller.show_frame("PageTwo"))


        
        button1.pack()



#Page one
class PageOne(tk.Frame):

    def __init__(self, parent, controller):
#Messagebox input
        def onClick():
            tk.messagebox.showinfo("Game rules:", "1.You draw shapes by clicking the left mouse button \n2.Yuo can move your last drawn shape with the right mouse button \n3.You can clear everything by pressing the left mouse button twice \n4.You can draw ovals, rectangles, lines \n5.Yuo can't pick the shape. It only goes in the order that will be given\n6.ENJOY!")
        tk.Frame.__init__(self, parent)
        self.controller = controller
        label = tk.Label(self, text="You can find game rules and tutorial by pressing the 'Click me!' button!", font=TITLE_FONT)
        label.pack(side="top", fill="x", pady=10)
        buttonM = tk.Button(self, text="Click me!", command = onClick)
        button = tk.Button(self, text="Go to the start page",
                           command=lambda: controller.show_frame("StartPage"))
        buttonM.pack()
        button.pack()
    

#The window that can create shapes and its paramaters
class PageTwo(tk.Frame): 
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        tk.Frame.__init__(self, parent)
        self.controller = controller
        label = tk.Label(self, text="Hello, you can draw shapes on this page!", font=TITLE_FONT)
        label.pack(side="top", fill="x", pady=10)
        button = tk.Button(self, text="Go to the start page",
                           command=lambda: controller.show_frame("StartPage"))
        button.pack()
        canvas.pack()
        canvas.bind('<ButtonPress-1>', self.StartShape) 
        canvas.bind('<B1-Motion>',     self.MakeShape)  
        canvas.bind('<Double-1>',      self.ClearEverything) 
        canvas.bind('<ButtonPress-3>', self.MoveShape)  
        self.canvas = canvas
        self.drawn  = None
        #Shows what kind of shapes can be created
        self.kinds = [canvas.create_oval, canvas.create_rectangle, canvas.create_line]
    def StartShape(self, event):
        self.shape = self.kinds[0]
        self.kinds = self.kinds[1:] + self.kinds[:1] 
        self.start = event
        self.drawn = None
    def MakeShape(self, event):                         
        canvas = event.widget
        if self.drawn: canvas.delete(self.drawn)
        objectId = self.shape(self.start.x, self.start.y, event.x, event.y)
        if trace: print(objectId)
        self.drawn = objectId
    def ClearEverything(self, event):
        event.widget.delete('all')                   
    def MoveShape(self, event):
        if self.drawn:                               
            if trace: print(self.drawn)
            canvas = event.widget
            diffX, diffY = (event.x - self.start.x), (event.y - self.start.y)
            canvas.move(self.drawn, diffX, diffY)
            self.start = event
            


if __name__ == "__main__":
    app = SampleApp()
    app.mainloop()
