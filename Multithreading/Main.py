# Multithreading Program (concept of threads)
import threading
import os

def print_square(num):
    print("Square: {}".format(num * num))

if __name__ == "__main__":
    # creating thread
    t1 = threading.Thread(target=print_square, args=(10,))

    # starting thread 1
    t1.start()
    t1.join()          # wait until thread 1 is completely executed
    print("Done!")

# we print thread name and corresponding process
def task1():
    print("Task 1 assigned to thread: {}".format(threading.current_thread().name))
    print("ID of process running task 1: {}".format(os.getpid()))

if __name__ == "__main__":
    print("ID of process running main program: {}".format(os.getpid()))
    print("Main thread name: {}".format(threading.current_thread().name))

    # creating threads
    t1 = threading.Thread(target=task1, name='t1')
    t1.start()            # starting threads
    t1.join()             # wait until all threads finish