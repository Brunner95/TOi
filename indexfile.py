import os
from tkinter import *
import tkinter as tk
from tkinter import messagebox
from PIL import ImageTk, Image
import PIL


class IndexFileApp(tk.Tk):
	def __init__(self):
		tk.Tk.__init__(self)
		self.img = ImageTk.PhotoImage(Image.open('Arrowhead-Right-01-128.png'))
		self.mb = tk.Button(self, text="					Go To Index				", image = self.img, compound=RIGHT, relief=RAISED, command=self.buttonClicked, height="80", width="250", bg="#6FA0ED",fg="white", font=("Helvetica",10))
		self.separator = Frame(self,height=2, bd=1, relief=SUNKEN,bg="#6FA0ED")
		self.ml = tk.Label(self, text="Hello my name is TOi\nI'm a IOT-project and\nI want to interact\nwith human beings", font=("Helvetica", 20), fg="white", width="35", height="15", bg="blue")

		self.ml.pack()
		self.separator.pack(fill=X, padx=3, pady=3)
		self.mb.pack(fill= X)


	def buttonClicked(self):
		self.destroy()
		os.system("index.py 1")


app = IndexFileApp()
app.mainloop()	