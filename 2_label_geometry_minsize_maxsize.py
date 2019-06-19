#imort all libraries for GUI
from tkinter import *

#create object of Tk class
root = Tk()

#width x height
root.geometry("400x400")

#minimum size of frame
root.minsize(200,100)

#maximum size of frame
root.maxsize(600,600)

#set label in the frame
label1 = Label(text="hello world")

#add label in frame
label1.pack()

#execute loop for infinite time 
root.mainloop()
