from threading import *
import time

class optionA(Thread):
    def run(self):
        for i in range(5):
            print("Option A")
            time.sleep(1)

class optionB(Thread):
    def run(self):
        for i in range(5):
            print("Option B")
            time.sleep(1)


obj1 = optionA()
obj2 = optionB()
obj1.start()
obj2.start()
obj1.join()
obj2.join()
print("Both threads have completed execution.")