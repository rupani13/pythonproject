#the 3rd higest value from list with predefined sorting function

def list_sorted():
    list1 = [70, 20, 30, 10, 90, 60]
    asc_sorted_list = sorted(list1)  #ascending order
    list1.sort(reverse=True) #descending orfer
    third_val = list1[2]
    max_val = list1[0]
    print("Ascending Order: ", asc_sorted_list)
    print("Descending Order: ", list1)
    print("3rd Highest value: ", third_val)
    print("Highest value: ", max_val)


if __name__ == "__main__":
    print("list with predefined sorting function:")
    list_sorted()
