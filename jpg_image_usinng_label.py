from tkinter import *
from PIL import Image, ImageTk
root = Tk()

root.title("show image using label")
root.geometry("500x500")

#open jpg image file
image = Image.open("2.jpg")
photo = ImageTk.PhotoImage(image)

#add image file to the label
label1 = Label(image=photo)

#add label to frame
label1.pack()

root.mainloop()
