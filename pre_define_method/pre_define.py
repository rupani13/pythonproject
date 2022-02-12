# How to find 3 largest value without pre define method

list1 = [12, 25, 15, 40, 35, 50, 10]

for i in range(len(list1)):
    for j in range(i + 1, len(list1)):
        if list1[i] < list1[j]:
            list1[i], list1[j] = list1[j], list1[i]
print("Descending order in list:", list1)
print("largest 3 value in list:", list1[2])

for i in range(len(list1)):
    for j in range(i + 1, len(list1)):
        if list1[i] > list1[j]:
            list1[i], list1[j] = list1[j], list1[i]
print("ascending  order in list:", list1)
print("smallest 3 value in list:", list1[2])



