from tkinter import *
import time
from threading import Thread


class But_print(Thread):
	def __init__(self):
		super().__init__()
		self.but = Button(root)
		self.but["text"] = "to count"
		self.but.bind("<Button-1>", self.printer)
		self.but.pack()

	def printer(self, event):
		self.start()
		
	def run(self):
		for i in range(10):
			print(10 - i - 1, "second")
			time.sleep(1)

root = Tk()
obj = But_print()
root.mainloop()


		