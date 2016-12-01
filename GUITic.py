import random
from math import floor
import os
from tkinter import *
import tkinter as tk
from tkinter import messagebox

class TicTacApp(tk.Tk):
	def __init__(self):
		tk.Tk.__init__(self)
		self.CurrentPlayer = IntVar()
		self.CurrentPlayer.set(0)

		#define field values
		self.Field1 = StringVar()
		self.Field2 = StringVar()
		self.Field3 = StringVar()
		self.Field4 = StringVar()
		self.Field5 = StringVar()
		self.Field6 = StringVar()
		self.Field7 = StringVar()
		self.Field8 = StringVar()
		self.Field9 = StringVar()

		#set field values
		self.Field1.set("1")
		self.Field2.set("2")
		self.Field3.set("3")
		self.Field4.set("4")
		self.Field5.set("5")
		self.Field6.set("6")
		self.Field7.set("7")
		self.Field8.set("8")
		self.Field9.set("9")


		#main String of label
		self.Field = StringVar()
		self.Field.set(self.Field1.get() + "  |  " + self.Field2.get() + "  |  " + self.Field3.get() + "\n" + "-----------" + "\n" + self.Field4.get() + "  |  " + self.Field5.get() + "  |  " + self.Field6.get() + "\n" + "-----------" + "\n" + self.Field7.get() + "  |  " + self.Field8.get() + "  |  " + self.Field9.get())
		self.Mtitle = tk.Label(self, text = "Tic-Tac-Toe", bg="blue", fg="white")
		self.titlesep = tk.Frame(height=2, bd=1, relief=SUNKEN,bg="#6FA0ED")
		self.infolabel = tk.Label(self, text = "info-text", bg="#6FA0ED",fg="white")
		self.headseper = tk.Frame(self,height=2, bd=1, relief=SUNKEN, bg="#6FA0ED")
		self.TicTacField = tk.Label(self, textvariable = self.Field, bg="#6FA0ED", fg="white")
		self.Ticsep = tk.Frame(self,height=2, bd=1, relief=SUNKEN,bg="#6FA0ED")
		self.inpentry = tk.Entry(self)
		self.inpentry.insert(END, "entry position")
		self.subButton = tk.Button(self, text="submit", relief = RAISED, command = self.onClick,height="4", width="70", bg="#6FA0ED",fg="white", font=("Helvetica",10))	
				
			
		
		self.Mtitle.grid(row=0)
		self.titlesep.grid(row=1)
		self.infolabel.grid(row=2)
		self.headseper.grid(row=3)
		self.TicTacField.grid(row=4)
		self.Ticsep.grid(row=5)
		self.inpentry.grid(row=6)
		self.subButton.grid(row=7)
		

	def onClick(self):


		#get current field for computer
		b1 = self.Field1.get()
		b2 = self.Field2.get()
		b3 = self.Field3.get()
		b4 = self.Field4.get()
		b5 = self.Field5.get()
		b6 = self.Field6.get()
		b7 = self.Field7.get()
		b8 = self.Field8.get()
		b9 = self.Field9.get()

		in_player = self.inpentry.get()
		in_player = int(in_player)

		if in_player == 1 and b1 == '1':
			self.Field1.set("X")
			b1 = self.Field1.get()
		elif in_player == 2 and b2 == '2':
			self.Field2.set("X")
			b2 = self.Field2.get()
		elif in_player == 3 and b3 == '3':
			self.Field3.set("X")
			b3 = self.Field3.get()
		elif in_player == 4 and b4 == '4':
			self.Field4.set("X")
			b4 = self.Field4.get()
		elif in_player == 5 and b5 == '5':
			self.Field5.set("X")
			b5 = self.Field5.get()
		elif in_player == 6 and b6 == '6':
			self.Field6.set("X")
			b6 = self.Field6.get()
		elif in_player == 7 and b7 == '7':
			self.Field7.set("X")
			b7 = self.Field7.get()
		elif in_player == 8 and b8 == '8':
			self.Field8.set("X")
			b8 = self.Field8.get()
		elif in_player == 9 and b9 == '9':
			self.Field9.set("X")
			b9 = self.Field9.get()
		self.Field.set(self.Field1.get() + "  |  " + self.Field2.get() + "  |  " + self.Field3.get() + "\n" + "-----------" + "\n" + self.Field4.get() + "  |  " + self.Field5.get() + "  |  " + self.Field6.get() + "\n" + "-----------" + "\n" + self.Field7.get() + "  |  " + self.Field8.get() + "  |  " + self.Field9.get())
	
	
		#check if player finished game
		if (b7 == 'X' and b8 == 'X' and b9 == 'X') or (b4 == 'X' and b5 == 'X' and b6 == 'X') or (b1 == 'X' and b2 == 'X' and b3 == 'X') or (b7 == 'X' and b4 == 'X' and b1 == 'X') or (b8 == 'X' and b5 == 'X' and b2 == 'X') or (b9 == 'X' and b6 == 'X' and b3 == 'X') or (b7 == 'X' and b5 == 'X' and b3 == 'X') or (b9 == 'X' and b5 == 'X' and b1 == 'X'):
			#playerwinmessage and leave game
			messagebox.showinfo("Congratulation", "You beat TOi")
			self.destroy()
			os.system("games.py 1")	

		elif (b1 == 'O' or b1 == 'X') and (b2 == 'O' or b2 == 'X') and (b3 == 'O' or b3 == 'X') and (b4 == 'O' or b4 == 'X') and (b5 == 'O' or b5 == 'X') and (b6 == 'O' or b6 == 'X') and (b7 == 'O' or b7 == 'X') and (b8 == 'O' or b8 == 'X') and (b9 == 'O' or b9 == 'X'):
			#draw message and leave game
			messagebox.showinfo("Draw", "The game endded in a draw")
			self.destroy()
			os.system("games.py 1")	

		#computer finish move when pos = 2 * O
		#fill first row when pos = 2 * O
		if b7 == 'O' and b8 == 'O' and b9 == '9':
			self.Field9.set("O")
			b9 = self.Field9.get()
		elif b8 == 'O' and b9 == 'O' and b7 == '7':
			self.Field7.set("O")
			b7 = self.Field7.get()
		elif b7 == 'O' and b9 == 'O' and b8 == '8':
			self.Field8.set("O")
			b8 = self.Field8.get()

		#fill in second row when pos = 2 * O
		elif b4 == 'O' and b5 == 'O' and b6 == '6':
			self.Field6.set("O")
			b6 = self.Field6.get()
		elif b4 == 'O' and b6 == 'O' and b5 == '5':
			self.Field5.set("O")
			b5 = self.Field5.get()
		elif b5 == 'O' and b6 == 'O' and b4 == '4':
			self.Field4.set("O")
			b4 = self.Field4.get()

		#fill in third row when pos = 2 * O 
		elif b1 == 'O' and b2 == 'O' and b3 == '3':
			self.Field3.set("O")
			b3 = self.Field3.get()
		elif b1 == 'O' and b3 == 'O' and b2 == '2':
			self.Field2.set("O")
			b2 = self.Field2.get()
		elif b2 == 'O' and b3 == 'O' and b1 == '1':
			self.Field1.set("O")
			b1 = self.Field1.get()

		#fill in first column when pos = 2 * O
		elif b7 == 'O' and b4 == 'O' and b1 == '1':
			self.Field1.set("O")
			b1 = self.Field1.get()
		elif b7 == 'O' and b1 == 'O' and b4 == '4':
			self.Field4.set("O")
			b4 = self.Field4.get()
		elif b4 == 'O' and b1 == 'O' and b7 == '7':
			self.Field7.set("O")
			b7 = self.Field7.get()

		#fill in second column when pos = 2 * O
		elif b8 == 'O' and b5 == 'O' and b2 == '2':
			self.Field2.set("O")
			b2 = self.Field2.get()
		elif b8 == 'O' and b2 == 'O' and b5 == '5':
			self.Field5.set("O")
			b5 = self.Field5.get()
		elif b5 == 'O' and b2 == 'O' and b8 == '8':
			self.Field8.set("O")
			b8 = self.Field8.get()

		#fill in third column when pos = 2 * O
		elif b9 == 'O' and b6 == 'O' and b3 == '3':
			self.Field3.set("O")
			b3 = self.Field3.get()
		elif b9 == 'O' and b3 == 'O' and b6 == '6':
			self.Field6.set("O")
			b6 = self.Field6.get()
		elif b3 == 'O' and b6 == 'O' and b9 == '9':
			self.Field9.set("O")
			b9 = self.Field9.get()
	
		#fill in first diagonale when pos = 2 * O
		elif b7 == 'O' and b5 == 'O' and b3 == '3':
			self.Field3.set("O")
			b3 = self.Field3.get()
		elif b5 == 'O' and b3 == 'O' and b7 == '7':
			self.Field7.set("O")
			b7 = self.Field7.get()
		elif b7 == 'O' and b3 == 'O' and b5 == '5':
			self.Field5.set("O")
			b5 = self.Field5.get()

		#fill in second diagonale when pos = 2 * O
		elif b9 == 'O' and b5 == 'O' and b1 == '1':
			self.Field1.set("O")
			b1 = self.Field1.get()
		elif b9 == 'O' and b1 == 'O' and b5 == '5':
			self.Field5.set("O")
			b5 = self.Field5.get()
		elif b1 == 'O' and b5 == 'O' and b9 == '9':
			self.Field9.set("O")
			b9 = self.Field9.get()
	
		#check firstRow (2 signs)

		elif b7 == 'X' and b8 == 'X' and b9 == '9':
			self.Field9.set("O")
			b9 = self.Field9.get()
		elif b7 == 'X' and b9 == 'X' and b8 == '8':
			self.Field8.set("O")
			b8 = self.Field8.get()
		elif b8 == 'X' and b9 == 'X' and b7 == '7':
			self.Field7.set("O")	
			b7 = self.Field7.get()
	 
		#check secondRow (2 signs)
	
		elif b4 == 'X' and b5 == 'X' and b6 == '6':
			self.Field6.set("O")
			b6 = self.Field6.get()
		elif b4 == 'X' and b6 == 'X' and b5 == '5':
			self.Field5.set("O")
			b5 = self.Field5.get()
		elif b5 == 'X' and b6 == 'X' and b4 == '4':
			self.Field4.set("O")
			b4 = self.Field4.get()

		#check thirdRow (2 signs)
	
		elif b1 == 'X' and b2 == 'X' and b3 == '3':
			self.Field3.set("O")
			b3 = self.Field3.get()
		elif b1 == 'X' and b3 == 'X' and b2 == '2':
			self.Field2.set("O")
			b2 = self.Field2.get()
		elif b2 == 'X' and b3 == 'X' and b1 == '1':
			self.Field1.set("O")
			b1 = self.Field1.get()

		#check first column (2 signs)
	
		elif b7 == 'X' and b4 == 'X' and b1 == '1':
			self.Field1.set("O")
			b1 = self.Field1.get()
		elif b4 == 'X' and b1 == 'X' and b7 == '7':
			self.Field7.set("O")
			b7 = self.Field7.get()
		elif b7 == 'X' and b1 == 'X' and b4 == '4':
			self.Field4.set("O")
			b4 = self.Field4.get()

		#check second column (2 signs)

		elif b8 == 'X' and b5 == 'X' and b2 == '2':
			self.Field2.set("O")
			b2 = self.Field2.get()
		elif b5 == 'X' and b2 == 'X' and b8 == '8':
			self.Field8.set("O")
			b8 = self.Field8.get()
		elif b8 == 'X' and b2 == 'X' and b5 == '5':
			self.Field5.set("O")
			b5 = self.Field5.get()

		#check third column (2 signs)
		elif b9 == 'X' and b6 == 'X' and b3 == '3':
			self.Field3.set("O")
			b3 = self.Field3.get()
		elif b6 == 'X' and b3 == 'X' and b9 == '9':
			self.Field9.set("O")
			b9 = self.Field9.get()
		elif b9 == 'X' and b3 == 'X' and b6 == '6':
			self.Field6.set("O")
			b6 = self.Field6.get()
	
		#check diagonal one (2 signs)
		elif b7 == 'X' and b5 == 'X' and b3 == '3':
			self.Field3.set("O")
			b3 = self.Field3.get()
		elif b7 == 'X' and b3 == 'X' and b5 == '5':
			self.Field5.set("O")
			b5 = self.Field5.get()
		elif b5 == 'X' and b3 == 'X' and b7 == '7':
			self.Field7.set("O")	
			b7 = self.Field7.get()
	
		#check diagonal two (2 signs)

		elif b9 == 'X' and b5 == 'X' and b1 == '1':
			self.Field1.set("O")
			b1 = self.Field1.get()
		elif b5 == 'X' and b1 == 'X' and b9 == '9':
			self.Field9.set("O")
			b9 = self.Field9.get()
		elif b9 == 'X' and b1 == 'X' and b5 == '5':
			self.Field5.set("O")
			b5 = self.Field5.get()
	
		#check first sign
		elif b7 == 'O' and b8 == '8':
			self.Field8.set("O")
			b8 = self.Field8.get()
		elif b7 == 'O' and b4 == '4':
			self.Field4.set("O")
			b4 = self.Field4.get()
		elif b7 == 'O' and b5 == '5':
			self.Field5.set("O")
			b5 = self.Field5.get()
		elif b8 == 'O' and b9 == '9':
			self.Field9.set("O")
			b9 = self.Field9.get()
		elif b8 == 'O' and b5 == '5':
			self.Field5.set("O")
			b5 = self.Field5.get()
		elif b9 == 'O' and b6 == '6':
			self.Field6.set("O")
			b6 = self.Field6.get()
		elif b9 == 'O' and b5 == '5':
			self.Field5.set("O")
			b5 = self.Field5.get()
		elif b4 == 'O' and b5 == '5':
			self.Field5.set("O")
			b5 = self.Field5.get()
		elif b4 == 'O' and b1 == '1':
			self.Field1.set("O")
			b1 = self.Field1.get()
		elif b5 == 'O' and b6 == '6':
			self.Field6.set("O")
			b6 = self.Field6.get()
		elif b5 == 'O' and b1 == '1':
			self.Field1.set("O")
			b1 = self.Field1.get()
		elif b5 == 'O' and b2 == '2':
			self.Field2.set("O")
			b2 = self.Field2.get()
		elif b5 == 'O' and b3 == '3':
			self.Field3.set("O")
			b3 = self.Field3.get()
		elif b1 == 'O' and b2 == '2':
			self.Field2.set("O")
			b2 = self.Field2.get()
		elif b2 == 'O' and b3 == '3':
			self.Field3.set("O")
			b3 = self.Field3.get()
		elif b3 == 'O' and b6 == '6':
			self.Field6.set("O")
			b6 = self.Field6.get()
		
		#check no fields
		#check middleField
		elif b5 == '5':
			self.Field5.set("O")
			b5 = self.Field5.get()
		elif b7 == '7':
			self.Field7.set("O")
			b7 = self.Field7.get()
		elif b9 == '9':
			self.Field9.set("O")
			b9 = self.Field9.get()
		elif b1 == '1':
			self.Field1.set("O")
			b1 = self.Field1.get()
		elif b3 == '3':
			self.Field3.set("O")
			b3 = self.Field3.get()
		elif b8 == '8':
			self.Field8.set("O")
			b8 = self.Field8.get()
		elif b4 == '4':
			self.Field4.set("O")
			b4 = self.Field4.get()
		elif b6 == '6':
			self.Field6.set("O")
			b6 = self.Field6.get()
		elif b2 == '2':
			self.Field2.set("O")
			b2 = self.Field2.get()

		self.Field.set(self.Field1.get() + "  |  " + self.Field2.get() + "  |  " + self.Field3.get() + "\n" + "-----------" + "\n" + self.Field4.get() + "  |  " + self.Field5.get() + "  |  " + self.Field6.get() + "\n" + "-----------" + "\n" + self.Field7.get() + "  |  " + self.Field8.get() + "  |  " + self.Field9.get())

		if (b7 == 'O' and b8 == 'O' and b9 == 'O') or (b4 == 'O' and b5 == 'O' and b6 == 'O') or (b1 == 'O' and b2 == 'O' and b3 == 'O') or (b7 == 'O' and b4 == 'O' and b1 == 'O') or (b8 == 'O' and b5 == 'O' and b2 == 'O') or (b9 == 'O' and b6 == 'O' and b3 == 'O') or (b7 == 'O' and b5 == 'O' and b3 == 'O') or (b9 == 'O' and b5 == 'O' and b1 == 'O'):		
			#computerwin message and leave game
			messagebox.showinfo("TOi won", "TOi has beaten you in Tic-Tac-Toe")
			self.destroy()
			os.system("games.py 1")


app = TicTacApp()
app.mainloop()