from tkinter import *

root = Tk()

root.geometry("500x500")

#this function will be called when button is pressed
def pressbutton():
    print(f"The value of username is {uservalue.get()}")
    print(f"The value of password is {passvalue.get()}")

label1 = Label(root,text="username")
label2 = Label(root,text="password")

#add lables on gridlayout
#add label and first row and first column
label1.grid()
#add label at 2nd row and first column
label2.grid(row=1)


#will take value of string type
usesrvalue = StringVar()
passvalue = StringVar()

#makes textfield for username and password
userentry = Entry(root,textvariable=uservalue)
passentry = Entry(root,textvariable=passvalue)

#adds these above fields to grids
userentry.grid(row=0,column=1)
passentry.grid(row=1,column=1)

#Button(text="Submit", command=pressbutton).grid()

#creats button for sign up
button = Button(root,text="sign up",command=pressbutton)
button.grid(row=3,column=1)


root.mainloop()
