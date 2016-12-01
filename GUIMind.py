import random
from math import floor
import os
from tkinter import *
import tkinter as tk
from tkinter import messagebox


class MasterMindApp(tk.Tk):
	def __init__(self):
		tk.Tk.__init__(self)
		self.var_c_p = StringVar()
		self.var_c_v = StringVar()
		self.var_c_p.set("0")
		self.var_c_v.set("0")
		self.Mtitle = tk.Label(self, text = "Mastermind", bg="blue", fg="white")
		self.titlesep = tk.Frame(height=2, bd=1, relief=SUNKEN,bg="#6FA0ED")
		self.infolabel = tk.Label(self, text = "Willkommen bei Mastermind, knacken Sie den 4-stelligen Code\nzugelassene Zahlen sind: 1,2,3,4,5,6 \neine Zahl kann auch mehrmals vorkommen", bg="#6FA0ED",fg="white")
		self.headseper = tk.Frame(self,height=2, bd=1, relief=SUNKEN,bg="#6FA0ED")
		self.corr_pos_label = tk.Label(self, textvariable = self.var_c_p, bg="blue", fg="white")
		self.corr_val_label = tk.Label(self, textvariable = self.var_c_v, bg="blue", fg="white")
		self.inpentry = tk.Entry(self)
		self.inpentry.insert(END, "entry your code")
		self.subButton = tk.Button(self, text="Submit", relief=RAISED, command=self.on_Click,  height="4", width="70", bg="#6FA0ED",fg="white", font=("Helvetica",10))	
		self.countVar = IntVar()
		self.countVar.set(0)		

		
		self.Mtitle.grid(row=0)
		self.titlesep.grid(row=1)
		self.infolabel.grid(row=2)
		self.headseper.grid(row=3)
		self.corr_pos_label.grid(row=4)
		self.corr_val_label.grid(row=5)
		self.inpentry.grid(row=6)
		self.subButton.grid(row=7)

		self.generated_str = ""
		self.string = "123456"
		for i in range(0,4):
			val = floor(random.random() * 6)
			self.value = self.string[val]
			self.generated_str = self.generated_str + self.value		
		

	def on_Click(self):
		countAttempts = self.countVar.get()
		checkString = self.inpentry.get()
		genStr = self.generated_str
		#print(genStr)
		returnPosCorrect = []
		
		count_val_at_pos = 0
		for j in range(0,4):
			if checkString[j] == genStr[j]:
				count_val_at_pos = count_val_at_pos + 1

		corr_pos = str(count_val_at_pos) + " Zahlen sind gleich und an der richtigen Stelle!"
		returnPosCorrect.append(corr_pos)

		count_same_values = 0
		for n in range(0,4):
			if (checkString.find(genStr[n]) != -1):
				count_same_values = count_same_values + 1
	
		corr_val = str(count_same_values) + " Zahlen sind gleich, jedoch nicht an der selben Stelle"
		returnPosCorrect.append(corr_val)


		self.var_c_p.set(returnPosCorrect[0])
		self.var_c_v.set(returnPosCorrect[1])
		

		if checkString == genStr:
			cVar = countAttempts + 1
			cVar = str(cVar)
			messagebox.showinfo("you won", "Congratulation!\nyour entry was: " + checkString + "\ngenerated String was: " + genStr + "\nattempts: " + cVar)
			self.destroy()
			os.system("games.py 1 ")

		elif countAttempts == 12:
			messagebox.showinfo("you lost","You have lost the game and made TOi sad\ngenerated String was: " + genStr)
			self.destroy()
			os.system("games.py 1")

		elif checkString != genStr:
			countAttempts = countAttempts + 1
			self.countVar.set(countAttempts)
		

app = MasterMindApp()
app.mainloop()





