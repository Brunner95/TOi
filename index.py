import os
from tkinter import *
import tkinter as tk
from tkinter import messagebox
from PIL import ImageTk, Image
import PIL


class IndexApp(tk.Tk):
	def __init__(self):
		tk.Tk.__init__(self)
		self.icon = ImageTk.PhotoImage(Image.open('Arrowhead-Right-01-128.png'))
		self.icon2 = ImageTk.PhotoImage(Image.open('Arrowhead-Left-01-128.png'))
		self.separator01 = Frame(self,height=2, width=560, bd=1, relief=SUNKEN, bg="#6FA0ED")
		self.separator02 = Frame(self,height=2, width=560, bd=1, relief=SUNKEN, bg="#6FA0ED")
		self.separator03 = Frame(self,height=2, width=560, bd=1, relief=SUNKEN, bg="#6FA0ED")
		self.separator04 = Frame(self,height=2, width=560, bd=1, relief=SUNKEN, bg="#6FA0ED")
		self.mb01 = tk.Button(self, text="					explain IoT				", relief=RAISED,image = self.icon, compound=RIGHT, command=self.buttonClicked01, width="560", height="80",fg="white", bg="#6FA0ED", font=("Helvetica",10))
		self.mb02 = tk.Button(self, text="					play video games				", relief=RAISED,image = self.icon, compound=RIGHT, command=self.buttonClicked02, width="560", height="80",fg="white", bg="#6FA0ED", font=("Helvetica",10))
		self.mb03 = tk.Button(self, text="					interaction				", relief=RAISED,image = self.icon, compound=RIGHT, command=self.buttonClicked03, width="560", height="80",fg="white", bg="#6FA0ED", font=("Helvetica",10))
		self.mb04 = tk.Button(self, text="					show my profile				", relief=RAISED,image = self.icon, compound=RIGHT, command=self.buttonClicked04, width="560", height="80",fg="white", bg="#6FA0ED", font=("Helvetica",10))
		self.mb05 = tk.Button(self, text="			go back							", relief=RAISED,image = self.icon2, compound=LEFT, command=self.buttonClicked05, width="560", height="80",fg="white", bg="#6FA0ED", font=("Helvetica",10))

		self.mb01.pack()
		self.separator01.pack(padx=3, pady=3)
		self.mb02.pack()
		self.separator02.pack(padx=3, pady=3)
		self.mb03.pack()
		self.separator03.pack(padx=3, pady=3)
		self.mb04.pack()
		self.separator04.pack(padx=3, pady=3)
		self.mb05.pack()

	def buttonClicked01(self):
		self.destroy()
		os.system("explain.py 1")
	def buttonClicked02(self):
		self.destroy()
		os.system("games.py 1")
	def buttonClicked03(self):
		self.destroy()
		os.system("interactionlist.py 1")
	def buttonClicked04(self):
		self.destroy()
		os.system("profile.py 1")
	def buttonClicked05(self):
		self.destroy()
		os.system("indexfile.py 1")

app = IndexApp()
app.mainloop()