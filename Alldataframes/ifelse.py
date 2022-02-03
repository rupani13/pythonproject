#If and Else Program

#prime no in if and else condition

list = [2, 3, 4, 6, 5, 7, 10]
for i in list:
    if i > 1:
        for x in range(2, i):
            if i % x != 0:
                print(x, 'A Not Prime number')
                break



