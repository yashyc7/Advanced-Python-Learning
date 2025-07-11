from concurrent.futures import thread
import threading
import time


def print_numbers():
    for i in range(5):
        print(f"Number :{i}")
        time.sleep(1)


def print_letters():
    for i in 'ABCDE':
        print(f"Letter{i}")
        time.sleep(1)
        
#creating the threads below



t1=threading.Thread(target=print_numbers)
t2=threading.Thread(target=print_letters)



t1.start()
t2.start()

#wait for both threads to finish 
t1.join()
t2.join()

print("DONE!")

