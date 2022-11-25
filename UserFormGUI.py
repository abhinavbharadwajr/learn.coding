from tkinter import *

# Creating GUI for the form

root = Tk()
root.configure(background='white')

# Form Structure

TextLabel1 = Label(root, text="Enter Username : ", bg="black", fg="white")
TextLabel1.grid(row=1, column=0, padx=425, sticky=W)

usrnmeText = Text(root, height=3, width=50, bg="white", fg="black")
usrnmeText.grid(row=1, column=0, padx=500)

TextLabel2 = Label(root, text="Enter your Password : ", bg="black", fg="white")
TextLabel2.grid(row=2, column=0, padx=425, sticky=W)

passwordText = Text(root, height=3, width=50, bg="white", fg="black")
passwordText.grid(row=2, column=0, padx=500)

TextLabel3 = Label(root, text="Re-type your Password : ", bg="black", fg="white")
TextLabel3.grid(row=3, column=0, padx=425, sticky=W)

confPassText = Text(root, height=3, width=50, bg="white", fg="black")
confPassText.grid(row=3, column=0, padx=500)