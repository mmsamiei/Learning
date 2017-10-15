import time

# this function must execute in an independent Thread
def countdown(n):
    while n > 0:
        print('T-minus', n)
        n -= 1
        time.sleep(1) # sleep in unit of sec.

from threading import Thread
t = Thread(target=countdown, args=(10,))
t.start()
t2 = Thread(target=countdown, args=(10,))
t2.start()
