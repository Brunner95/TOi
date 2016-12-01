import os
from tkinter import *
import tkinter as tk
from tkinter import messagebox
from PIL import ImageTk, Image
import PIL

class GamesApp(tk.Tk):
	def __init__(self):
		tk.Tk.__init__(self)
		self.title("Gameindex")
		self.icon_right = ImageTk.PhotoImage(Image.open('Arrowhead-Right-01-128.png'))
		self.icon_left = ImageTk.PhotoImage(Image.open('Arrowhead-Left-01-128.png'))
		self.separator01 = Frame(height=2, bd=1, relief=SUNKEN,bg="#6FA0ED")
		self.separator02 = Frame(self,height=2, bd=1, relief=SUNKEN,bg="#6FA0ED")
		self.separator03 = Frame(self,height=2, bd=1, relief=SUNKEN,bg="#6FA0ED")
		self.separator04 = Frame(self,height=2, bd=1, relief=SUNKEN,bg="#6FA0ED")

		self.mb01 = tk.Button(self, text="				Hang Man			", image = self.icon_right, compound=RIGHT, relief=RAISED, command=self.buttonClicked01, width="450", height="80",fg="white", bg="#6FA0ED", font=("Helvetica",10))
		self.mb02 = tk.Button(self, text="				Tic-Tac-Toe			", image = self.icon_right, compound=RIGHT, relief=RAISED, command=self.buttonClicked02, width="450", height="80",fg="white", bg="#6FA0ED", font=("Helvetica",10))
		self.mb03 = tk.Button(self, text="				Fibonacci-Row			", image = self.icon_right, compound=RIGHT, relief=RAISED, command=self.buttonClicked03, width="450", height="80",fg="white", bg="#6FA0ED", font=("Helvetica",10))
		self.mb04 = tk.Button(self, text="				Mastermind			", image = self.icon_right, compound=RIGHT, relief=RAISED, command=self.buttonClicked04, width="450", height="80",fg="white", bg="#6FA0ED", font=("Helvetica",10))
		self.mb05 = tk.Button(self, text="								", image = self.icon_left, compound=LEFT, relief=RAISED, command=self.buttonClicked05, width="450", height="80",fg="white", bg="#6FA0ED", font=("Helvetica",10))
	
		self.mb01.pack(fill=X)
		self.separator01.pack(fill=X, padx=3, pady=3)
		self.mb02.pack(fill=X)
		self.separator02.pack(fill=X, padx=3, pady=3)
		self.mb03.pack(fill=X)
		self.separator03.pack(fill=X, padx=3, pady=3)
		self.mb04.pack(fill=X)
		self.separator04.pack(fill=X, padx=3, pady=3)
		self.mb05.pack(fill=X)

	def buttonClicked01(self):
		self.destroy()
		os.system("GUIHang.py 1")
	def buttonClicked02(self):
		self.destroy()
		os.system("GUITic.py 1")
	def buttonClicked03(self):
		self.destroy(self)
		os.system("GUIFibo.py 1")
	def buttonClicked04(self):
		self.destroy()
		os.system("GUIMind.py 1")
	def buttonClicked05(self):
		self.destroy()
		os.system("index.py 1")


app = GamesApp()
app.mainloop()