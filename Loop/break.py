# All Break program
a = 0
b = "The_Book"
while a < len(b):
    if b[a] == 'e':
        a += 1
        break
    print("letter:", b[a])
    a += 1

# Using for loop
for i in b:
    print("value:", i)
    if i == 'o':
        break


