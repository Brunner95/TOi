import os
from tkinter import *
import tkinter as tk


root = tk.Tk()

def buttonClicked01():
	root.destroy()
	os.system("followMe.py 1")
def buttonClicked02():
	root.destroy()
	os.system("someFunc01.py 1")
def buttonClicked03():
	root.destroy()
	os.system("someFunc02.py 1")
def buttonClicked04():
	root.destroy()
	os.system("someFunc03.py 1")
def buttonClicked05():
	root.destroy()
	os.system("index.py 1")


separator01 = Frame(height=2, bd=1, relief=SUNKEN,bg="#6FA0ED")
separator02 = Frame(height=2, bd=1, relief=SUNKEN,bg="#6FA0ED")
separator03 = Frame(height=2, bd=1, relief=SUNKEN,bg="#6FA0ED")
separator04 = Frame(height=2, bd=1, relief=SUNKEN,bg="#6FA0ED")

mb01 = tk.Button(root, text="Follow me", relief=RAISED, command=buttonClicked01, width="70", height="5",fg="white", bg="#6FA0ED", font=("Helvetica",10)).pack()
separator01.pack(fill=X, padx=3, pady=3)
mb02 = tk.Button(root, text="Some function", relief=RAISED, command=buttonClicked02, width="70", height="5",fg="white", bg="#6FA0ED", font=("Helvetica",10)).pack()
separator02.pack(fill=X, padx=3, pady=3)
mb03 = tk.Button(root, text="Some function", relief=RAISED, command=buttonClicked03, width="70", height="5",fg="white", bg="#6FA0ED", font=("Helvetica",10)).pack()
separator03.pack(fill=X, padx=3, pady=3)
mb04 = tk.Button(root, text="Some function", relief=RAISED, command=buttonClicked04, width="70", height="5",fg="white", bg="#6FA0ED", font=("Helvetica",10)).pack()
separator04.pack(fill=X, padx=3, pady=3)
mb05 = tk.Button(root, text="go back", relief=RAISED, command=buttonClicked05, width="70", height="5",fg="white", bg="#6FA0ED", font=("Helvetica",10)).pack()


root.mainloop()