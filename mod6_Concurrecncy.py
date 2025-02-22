'15.1'
import time
import os
import multiprocessing
import random

def timeProcess(self, *args):
    print(*args)
  

if __name__ == "__main__":
    now = time.time()   
    for n in range(3):
        randNum = random.random()
        p = multiprocessing.Process(target=timeProcess, args=(time.ctime(now)))
        time.sleep(randNum)
        p.start()