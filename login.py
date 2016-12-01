#create login + register
#if registerbutton is clicked => open window with sap-mail, and 2x pw then commit
#after commit data ist saved
#to login = get data and whatch if user + pw is equvivalent to saved data
import os
from tkinter import *
import tkinter as tk
from tkinter import messagebox
from PIL import ImageTk, Image
import PIL

class LoginApp(tk.Tk):
	def __init__(self):
		tk.Tk.__init__(self)
		self.LoginIcon = ImageTk.PhotoImage(Image.open('Windows-8-Login-128.png'))
		self.RegIcon = ImageTk.PhotoImage(Image.open('User-Add-128.png'))
		self.BackIcon = ImageTk.PhotoImage(Image.open('Arrowhead-Left-01-128.png')) 
		self.mtitle = tk.Label(self, text="I'm a very shy robot.\nMy mother robot had taught me to don't interact with unknown human", font=("Helvetica", 10), fg="white", width="70", height="5", bg="#6FA0ED")
		self.logButton = tk.Button(self, text = "					Login				", image = self.LoginIcon, compound=RIGHT, relief=RAISED, command=self.buttonLogin, height="80", width="560", bg="#6FA0ED",fg="white", font=("Helvetica",10))
		self.mbody = tk.Label(self, text="	not registered yet", font=("Helvetica", 10), width="70", height="5", fg="white", bg="#6FA0ED")
		self.regButton = tk.Button(self, text = "					Register				", image = self.RegIcon, compound=RIGHT, relief=RAISED, command=self.buttonReg, height="80", width="560", bg="#6FA0ED",fg="white", font=("Helvetica",10))
		self.backButton = tk.Button(self, text = "			   back							", image = self.BackIcon, compound=LEFT, relief=RAISED, command=self.buttonBack, height="80", width="560", bg="#6FA0ED",fg="white", font=("Helvetica",10))
		self.titlesep = Frame(self,height=2,width=560, bd=1, relief=SUNKEN,bg="#6FA0ED")
		self.bodyupsep = Frame(self,height=2,width=560, bd=1, relief=SUNKEN,bg="#6FA0ED")
		self.bodydownsep = Frame(self,height=2,width=560, bd=1, relief=SUNKEN,bg="#6FA0ED")
		self.regsep = Frame(self,height=2,width=560, bd=1, relief=SUNKEN,bg="#6FA0ED") 
		
		self.title("Login")
		self.mtitle.pack()
		self.titlesep.pack(padx=3, pady=3)
		self.logButton.pack()
		self.bodyupsep.pack(padx=3, pady=3)
		self.mbody.pack()
		self.bodydownsep.pack(padx=3, pady=3)
		self.regButton.pack()
		self.regsep.pack(padx=3, pady=3)
		self.backButton.pack()


	def buttonLogin(self):
		self.destroy()

	def buttonReg(self):
		self.destroy()
	
	def buttonBack(self):
		self.destroy()
		os.system("indexfile.py 1")

app = LoginApp()
app.mainloop()

