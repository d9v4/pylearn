import time
from threading import Thread
def countdown(n):
	for i in range(n):
		print(n - i - 1, "left")
		time.sleep(1)
	
def count(e):
	for i in range(e):
		print(e - i - 1, "second")
		time.sleep(1)

q = Thread(target=count, args=(3, ))
t = Thread(target=countdown, args=(3, ))
t.start()
q.start()

for i in range(3):
	print(3 - i - 1, "main")
	time.sleep(1)