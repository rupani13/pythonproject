# importing the multiprocessing module
import multiprocessing


def print_square(num):
    print("Square: {}".format(num * num))


if __name__ == "__main__":
    p1 = multiprocessing.Process(target=print_square, args=(10,))  # process start
    p1.start()
    p1.join()
    print("Done!")

# cube processing
def print_cube(num):
    print("Cube: {}".format(num * num * num))


if __name__ == "__main__":
    p2 = multiprocessing.Process(target=print_cube, args=(10,))  # process start
    p2.start()
    p2.join()
    print("Done!")