# All While Loop Program

# using list in while loop

list1 = [1, 2, 3, 4, 5, 6]

while list1:
    print(list1.pop())

# sum in while loop

n = 10
var = 0
i = 5

while i <= n:
    var = var + i
    i = i+1
print("The sum is", var)

# while loop with else

i = 0
while i < 4:
    i += 1
    print(i)
else:
    print("No Break")

i = 0
while i < 4:
    i += 1
    print(i)
    break
else:
    print("No Break")

# Continue with wile loop

a = 0
b = "The_Book"
while a < len(b):
    if b[a] == 'o':
        a += 1
        continue
    print("Value:", b[a])
    a += 1

#  Break In while loop

a = 0
b = "The_Book"
while a < len(b):
    if b[a] == 'o':
        a += 1
        break
    print("letter:", b[a])
    a += 1