# Multithreading set 2
import threading

x = 0  # global variable


def increment():
    global x
    x += 1


def thread_task():
    for _ in range(100000):
        increment()


def main_task():
    global x
    x = 0
    t1 = threading.Thread(target=thread_task)  # creating threads
    t1.start()  # start threads
    t1.join()  # wait until threads finish their job


if __name__ == "__main__":
    for i in range(5):
        main_task()
        print("Iteration {0}: x = {1}".format(i, x))

# Using lock
y = 0
def increment():
    global y
    y += 1


def thread_task(lock):
    for _ in range(100000):
        lock.acquire()
        increment()
        lock.release()


def main_task():
    global y
    y = 0

    # creating a lock
    lock = threading.Lock()
    t1 = threading.Thread(target=thread_task, args=(lock,))     # creating threads
    t1.start()    # start threads
    t1.join()     # wait until threads finish their job


if __name__ == "__main__":
    for i in range(5):
        main_task()

        print("Iteration {0}: y = {1}".format(i, x))


