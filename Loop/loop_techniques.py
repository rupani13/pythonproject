# All Loop techniques Program

l1 = ["eat", "sleep", "repeat"]

# printing the tuples in object directly
for ele in enumerate(l1):
    print(ele)
for count, ele in enumerate(l1, 100):
    print(count, ele)

# getting desired output from tuple
for count, ele in enumerate(l1):
    print(count)
    print(ele)

# zip program

var1 = ['name', 'colour', 'shape']
var2 = ['apple', 'red', 'a circle']

for var1, var2 in zip(var1, var2):
    print('What is your {0}?  I am {1}'.format(var1, var2))