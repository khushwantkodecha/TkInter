from tkinter import *

root = Tk()

#width x height
root.geometry("400x400")

root.minsize(200,100)
root.maxsize(600,600)

label1 = Label(text="hello world")
label1.pack()

root.mainloop()
