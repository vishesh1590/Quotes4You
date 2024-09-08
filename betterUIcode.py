# Import Module
from tkinter import *

# create root window
root = Tk()

# root window title and dimension
root.title("Welcome to Quotes4u")
# Set geometry(widthxheight)
root.geometry('500x600')

lbl = Label(root, text = "How are you Feeling Today?")
lbl.grid()
lbl = Label(root, text = "I am feeling postive")
lbl.grid()
lbl = Label(root, text = "I am feeling negative")
lbl.grid()

# function to display text when
# button is clicked
def clicked():
    lbl.configure(text = "")


# button widget with red color text
# inside
btn = Button(root, text = "Click me" ,
             fg = "red", command=clicked)
# set Button grid
btn.grid(column=1, row=2)

# Execute Tkinter
root.mainloop()