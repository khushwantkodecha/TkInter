from tkinter import *

root = Tk()

root.title("label and packs attributes")
root.geometry("400x400")
label = Label(text="hello this is khushwant singh kodecha from Rajasthan",
             bg="green",fg="white",padx=12,pady=10,font=("arial",10,"bold"),borderwidth=4,relief=SUNKEN)
label.pack(side="bottom",anchor="ne",fill=X)

root.mainloop()
