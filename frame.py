from tkinter import *

root = Tk()

root.geometry("500x500")

#creating frame that will contain text of label1
frame1 = Frame(root,bg="grey",borderwidth=4,relief=SUNKEN)
#it will pack this frame1 into basic GUI
frame1.pack(side=LEFT,fill=Y)

#creating frame that will contain text of label2
frame2 = Frame(root,bg="red",borderwidth=3,relief=SUNKEN)
#it will pack this frame2 into basic GUI
frame2.pack(side=TOP,fill=X)

#creating label and add this label text to frame1
label1 = Label(frame1,text="hello this text will be puted in the frame1",bg="grey")
label1.pack()

#creating label and add this label text to frame1
label2 = Label(frame2,text="this text will be puted into frame2",fg="yellow",bg="red",font=("arial",9,"italic"))
label2.pack()

root.mainloop()
