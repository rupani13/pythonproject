#the 3rd higest value from list without predefined sorting function(Descending)
def list_with_out_sorted():
    list1 = [20, 15, 60, 40, 35, 50]
    for i in range(len(list1)):
        for j in range(i+1, len(list1)):
            if list1[i] < list1[j]:
             temp = list1[i]
             list1[i] = list1[j]
             list1[j] = temp
             third_val = list1[2]
    print("Descending Order:", list1)
    print("Higher_value:", third_val)



#the 3rd higest value from list without predefined sorting function(Ascending)
    list1 = [20, 15, 60, 40, 35, 50]
    for i in range(len(list1)):
        for j in range(i + 1, len(list1)):
            if list1[i] > list1[j]:
                temp = list1[i]
                list1[i] = list1[j]
                list1[j] = temp
                min_val = list1[0]
                max_val = list1[5]
    print("Ascending Order: ", list1)
    print("Smallest value: ", min_val)
    print("Higher value: ", max_val)



if __name__ == "__main__":
    print("list without predefined sorting function:")
    list_with_out_sorted()
