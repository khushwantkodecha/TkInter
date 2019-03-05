from tkinter import *

root = Tk()

root.geometry("400x400")

#define function for button first
def func1():
    print("button one is pressed")

#define function for button first
def func2():
    print("button two is pressed")

#build frame that will contain buttons
frame = Frame(root,bg="green",borderwidth=4,relief=SUNKEN)
frame.pack(side=LEFT,anchor="nw")

#building button and add it to made frame
button1 = Button(frame,text="button1",command=func1)
button1.pack(side=LEFT)

#building button and add it to made frame
button2 = Button(frame,text="button2",command=func2)
button2.pack(side=LEFT)

root.mainloop()