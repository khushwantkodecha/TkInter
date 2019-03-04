#this code is only for png images
from tkinter import *

root = Tk()

root.title("show image using label")
root.geometry("500x500")

#to choose image path and file
photo = PhotoImage(file="1.png")

#add image file to the label
label1 = Label(image=photo)

#add label to frame
label1.pack()

root.mainloop()
