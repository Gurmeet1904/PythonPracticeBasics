from time import sleep
from threading import *

class Hello(Thread):
    def run(self):
        for i in range(5):
            print("Hello")
            sleep(1)             #Waiting for 1 sec, so that it does to print very fast, and in-between other thread can also run

class Hi(Thread):
    def run(self):
        for i in range(5):
            print("Hi")
            sleep(1)

t1 = Hello()                    #Object of class Hello
t2 = Hi()                       #Object of class Hi


t1.start()           #Instead of run() we are using start() so that it will execute two different threads. run() method is also present in thread() class
sleep(0.2)           #Used to avoid collision: so that 2 threads do not occur at same time
t2.start()


t1.join()            #If join() is not used, then "Bye" will get printed first(as it is present in main thread, and it executes independently)
                     #By using join(), first t1 and t2 will get executed, then anything written in main() thread will get executed
t2.join()

print("Bye")




