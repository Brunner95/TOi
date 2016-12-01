import random
from math import floor
import os
from tkinter import *
import tkinter as tk
from tkinter import messagebox

class TicTacApp(tk.Tk):
	def __init__(self):
		tk.Tk.__init__(self)
		self.inp1 = StringVar()
		self.inp2 = StringVar()
		self.inp3 = StringVar()

		self.inp1.set("Hello")
		self.inp2.set("Hello")
		self.inp3.set("Hello")

		self.board = StringVar()

		self.board.set(self.inp1.get() + self.inp2.get())
	


		self.Field = tk.Label(self, textvariable = self.board, bg="#6FA0ED", fg="white")
		self.Sub = tk.Button(self, text="submit", relief = RAISED, command = self.onClick,height="4", width="70", bg="#6FA0ED",fg="white", font=("Helvetica",10))


		self.Field.grid(row=0)
		self.Sub.grid(row=1)
		


	def onClick(self):

		inp1 = self.inp1.get()
		inp2 = self.inp2.get()
		inp3 = self.inp3.get()

		inp1 = "Yello"
		inp2 = "Yello"
		inp3 = "Yello"
		
		self.board.set(inp1 + "\n" + inp2 + inp3)

app = TicTacApp()
app.mainloop()