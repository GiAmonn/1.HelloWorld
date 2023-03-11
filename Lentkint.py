from tkinter import * 
import tkinter as tk

frame = tk.Tk()
frame.title("Length Checker")
frame.geometry('500x250')
var = StringVar()

def checklen(*args):
    text = var.get()
    len_label.config(text = f"{text} has {len(text)} characters.")


note_lbl = tk.Label(frame, text = "Write something: ")
note_lbl.pack()

inputtext = tk.Entry(frame, textvar = var)
inputtext.pack()

len_label = tk.Label(frame, text = "")
len_label.pack()

var.trace("w",checklen)

frame.mainloop()
