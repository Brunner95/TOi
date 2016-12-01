import random
from math import floor
import os
from tkinter import *
import tkinter as tk
from tkinter import messagebox

class FiboApp(tk.Tk):
	def __init__(self):
		tk.Tk.__init__(self)
		self.a_2Var = IntVar()
		self.a_1Var = IntVar()
		self.a_2Var.set(1)
		self.a_1Var.set(0)
		self.a_2t = StringVar()
		self.a_1t = StringVar()
		self.Count = IntVar()
		self.Count.set(0)
		self.a_2t.set("a_2 : " + str(self.a_2Var.get()))
		self.a_1t.set("a_1 : " + str(self.a_1Var.get()))
		self.Mtitle = tk.Label(self, text = "Fibbonaci-Row", bg="blue", fg="white")
		self.titlesep = tk.Frame(height=2, bd=1, relief=SUNKEN,bg="#6FA0ED")
		self.infolabel = tk.Label(self, text = "", bg="#6FA0ED",fg="white")
		self.headseper = tk.Frame(self,height=2, bd=1, relief=SUNKEN,bg="#6FA0ED")
		self.a_2 = tk.Label(self, textvariable = self.a_2t, bg="blue", fg="white")
		self.a_1 = tk.Label(self, textvariable = self.a_1t, bg="blue", fg="white")
		self.bodysep = tk.Frame(self,height=2, bd=1, relief=SUNKEN,bg="#6FA0ED")
		self.inpentry = tk.Entry(self)
		self.inpentry.insert(END, "entry next F-Value")
		self.subButton = tk.Button(self, text="submit", relief = RAISED, command = self.onClick,height="4", width="70", bg="#6FA0ED",fg="white", font=("Helvetica",10))
		

		self.Mtitle.grid(row=0)
		self.titlesep.grid(row=1)
		self.infolabel.grid(row=2)
		self.headseper.grid(row=3)
		self.a_1.grid(row=4)
		self.a_2.grid(row=5)
		self.bodysep.grid(row=6)
		self.inpentry.grid(row=7)
		self.subButton.grid(row=8)


	def onClick(self):

		inp_user = self.inpentry.get()
		inp_user = int(inp_user)
		a2 = self.a_2Var.get()
		a1 = self.a_1Var.get()
		Count = self.Count.get()

		if inp_user == (a2 + a1):
			nextValForA1 = a2
			nextValForA2 = inp_user
			Count = Count + 1
			self.Count.set(Count)
			self.a_2Var.set(nextValForA2)
			self.a_1Var.set(nextValForA1)
			self.a_2t.set("a_2 : " + str(self.a_2Var.get()))
			self.a_1t.set("a_1 : " + str(self.a_1Var.get()))


		else:
			messagebox.showinfo("you lost","You have lost the game and made TOi sad\nscore: " + str(Count))
			self.destroy()
			os.system("games.py 1")

app = FiboApp()
app.mainloop()
		
		