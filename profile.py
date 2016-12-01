import os
from tkinter import *
import tkinter as tk

root = tk.Tk()

def buttonClicked():
	root.destroy()
	os.system("index.py 1")
#get current username
username = "username"

ml = tk.Label(root, text="Profile of: " + username, fg="white", bg="#6FA0ED", width = 80, height=5).pack()
btn_back = tk.Button(root, text="Go To Index", relief=RAISED, command=buttonClicked, height="4", width="70", bg="#6FA0ED",fg="white", font=("Helvetica",10)).pack()

root.mainloop()