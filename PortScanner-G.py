import socket
import time
from tkinter import *

def scan():
	target = txt.get()
	for i in range(10000):

		try:
			scaning = socket.socket()
			scaning.settimeout(0.5)
			scaning.connect((target, i))

		except socket.error:
			time.sleep(0)

		else:
			x.append(i)
	lbl2.configure(text = "Complete")

x = ["Open port: "]

window = Tk()
window.title("Port Scaner v 1.0")

lbl = Label(text = "Welcome!")
lbl.grid(column = 0, row = 1)

lbl1 = Label(text = "Input Target: ")
lbl1.grid(column = 0, row = 3)

lbl2 = Label(text = "")
lbl.grid(column = 3, row = 1)

txt = Entry(window, width=20)
txt.grid(column = 1, row = 3 )

lbl2 = Label(text = x)
lbl.grid(column = 1, row = 8)

btn = Button(window, text = "Scan", command=scan, width = 10)
btn.grid(column= 1, row = 7)

window.geometry('400x250')
window.mainloop()