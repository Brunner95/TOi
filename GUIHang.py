import random
from math import floor
import os
from tkinter import *
import tkinter as tk
from tkinter import messagebox
from PIL import ImageTk, Image
import PIL


class HangManApp(tk.Tk):
	def __init__(self):
		tk.Tk.__init__(self)
		self.GenWord = StringVar()
		self.img = ImageTk.PhotoImage(Image.open('hangman00-re.jpg'))
		self.list_correctLetters = StringVar()
		self.list_UsedLetters = StringVar()
		self.word_list = ["hangman", "chairs", "backpack", "body", "clothing",
        	    		"computer", "science", "program", "glasses", "sweatshirt",
        	     		"physics", "developer", "friends", "clock", "biology",
        	     		"algebra", "suitcase", "knives", "ninjas", "shampoo","erp","sap"
        			]

		#generate random word in list
		leng = (len(self.word_list) - 1)
		val = floor(random.random() * leng)
		self.word = self.word_list[val]
		self.GenWord.set(self.word)

		l_word = len(self.word)
		s_string = ""
		for i in range(0,l_word):
			s_string +="_ "	
		self.list_correctLetters.set(s_string)

		self.Mtitle = tk.Label(self, text = "Hangman", bg="blue", fg="white")
		self.titlesep = tk.Frame(height=2, bd=1, relief=SUNKEN, bg="#6FA0ED")
		self.introlabel = tk.Label(self, text="BLABLABAL.... Intro",bg="#6FA0ED",fg="white")
		self.introsep = tk.Frame(self, height=2, bd=1, relief=SUNKEN,bg="#6FA0ED")
		self.dynHangMan = tk.Label(self, image = self.img, width = 250, height = 300, bg="white")
		self.corrLetters = tk.Label(self, textvariable = self.list_correctLetters,bg="blue",fg="white")
		self.dynUsedLetters = tk.Label(self, textvariable = self.list_UsedLetters,bg="blue",fg="white")
		self.inpentry = tk.Entry(self)
		self.inpentry.insert(END, "entry your code")
		self.submit = tk.Button(self, text="Submit", command=self.onClick)

		self.attempts = IntVar()
		self.attempts.set(0)

		self.Mtitle.grid(row=0)
		self.titlesep.grid(row=1)
		self.introlabel.grid(row=2)
		self.introsep.grid(row=3)
		self.dynHangMan.grid(row=4)
		self.corrLetters.grid(row=5)
		self.dynUsedLetters.grid(row=6)
		self.inpentry.grid(row=7)
		self.submit.grid(row=8)



			

	def onClick(self):
		user_inp = self.inpentry.get()
		user_inp = user_inp.lower()
		correctWord = self.GenWord.get()
		usedLetters = self.list_UsedLetters.get()
		correctLetters = self.list_correctLetters.get()
		splittedCorrectLetters = correctLetters.split( )

		if user_inp == correctWord:
			#winMessage
			messagebox.showinfo("you won", "Congratulation!")
			self.destroy()
			os.system("games.py 1")

		else:
			for n in range(0,len(correctWord)):
				if user_inp.find(correctWord[n]) != -1:
					splittedCorrectLetters[n] = correctWord[n]

			myString = ""
			for j in range(0,len(splittedCorrectLetters)):
				myString += splittedCorrectLetters[j] + " " 
			self.list_correctLetters.set(myString)		


			usedLetters = usedLetters + " " + user_inp + " , "
			self.list_UsedLetters.set(usedLetters)

			if len(user_inp) == len(correctWord) and user_inp != correctWord:
				#lose msg
				messagebox.showinfo("you lost","You have lost the game and made TOi sad\ngenerated word: " + correctWord)
				self.destroy()
				os.system("games.py 1")
			else:
				attempts = self.attempts.get()
				attempts = attempts + 1
				nwString = "0" + str(attempts)
				hangmStr = "hangman"+ nwString +"-re.jpg"
				imgCont = ImageTk.PhotoImage(Image.open(hangmStr))
				self.dynHangMan.configure(image = imgCont)
				self.dynHangMan.image = imgCont
				self.attempts.set(attempts)

				if attempts == 9:
					#lose msg
					messagebox.showinfo("you lost","You have lost the game and made TOi sad\ngenerated String was: " + correctWord)
					self.destroy()
					os.system("games.py 1")

app = HangManApp()
app.mainloop()