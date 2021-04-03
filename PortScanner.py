import socket
import time

def scan():
	try:
		target = input("Target: ")
		for i in range(10000):
			try:
				scaning = socket.socket()
				scaning.settimeout(0.5)
				scaning.connect((target, i))

			except socket.error:
				time.sleep(0.1)
			else:
				print("")
				print("Port ", i, "open")
	except:
		print("Bye!")

scan()
