# Multiprocessing Program
import multiprocessing
result = []


def square_list(list1):
    global result
    for num in list1:
        result.append(num * num)
    print("Result(in process p1): {}".format(result))


if __name__ == "__main__":
    list1 = [1, 2, 3, 4]
    p1 = multiprocessing.Process(target=square_list, args=(list1,))
    p1.start()
    p1.join()

# Sharing data between processes


def square_list(list2, var, square_sum):
    for idx, num in enumerate(list2):
        var[idx] = num * num
    square_sum.value = sum(var)
    print("Result(in process p1): {}".format(var[:]))
    print("Sum of squares(in process p1): {}".format(square_sum.value))


if __name__ == "__main__":
    list2 = [1, 2, 3, 4]
    var = multiprocessing.Array('i', 4)
    square_sum = multiprocessing.Value('i')
    p1 = multiprocessing.Process(target=square_list, args=(list2, var, square_sum))
    p1.start()
    p1.join()

    print("Result(in main program): {}".format(var[:]))
    print("Sum of squares(in main program): {}".format(square_sum.value))