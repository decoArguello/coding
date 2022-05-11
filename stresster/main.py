import threading
import logging
import time


def worker():
  print("test de hilos")

threads = []

for i in range(5):
  t = threading.Thread(target=worker)
  threads.append(t)
  t.start()


