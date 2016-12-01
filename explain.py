import os
from tkinter import *
import tkinter as tk
from PIL import ImageTk, Image
import PIL


class ExplainApp(tk.Tk):
	def __init__(self):
		tk.Tk.__init__(self)
		self.icon = ImageTk.PhotoImage(Image.open('Arrowhead-Left-01-128.png'))
		self.img = ImageTk.PhotoImage(Image.open('internet-of-things-re.jpg'))
		self.separator01 = Frame(self,height=2, bd=1, relief=SUNKEN,bg="#6FA0ED")
		self.separator02 = Frame(self,height=2, bd=1, relief=SUNKEN,bg="#6FA0ED")
		self.mylabel02 = "Internet of Things definition:\nThe vast network of devices connected to the Internet,\nincluding smart phones and tablets and almost anything\nwith a sensor on it: cars, machines in production plants,\njet engines, oil drills, wearable devices, and more.\nThese Things collect and exchange data."
		self.ml01 = tk.Label(self,text=self.mylabel02, font=("Helvetica", 10), fg="white", width="70", height="15", bg="blue")
		self.pic = tk.Label(self, image = self.img, width=70, height=300,bg="blue")
		self.mb = tk.Button(self, text="			Go To Index						", image = self.icon, compound = LEFT, relief=RAISED, command=self.buttonClicked, height="80", width="250", bg="#6FA0ED",fg="white", font=("Helvetica",10))

		self.ml01.pack()
		self.separator01.pack(fill=X, padx=3, pady=3)
		self.pic.pack(fill = 'both')
		self.separator02.pack(fill=X, padx=3, pady=3)
		self.mb.pack(fill=X)


	def buttonClicked(self):
		self.destroy()
		os.system("index.py 1")


app = ExplainApp()
app.mainloop()