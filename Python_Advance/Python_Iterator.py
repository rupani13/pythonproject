# All Python Iterator program
# python inbuilt iterator value can be anything which can be iterated
iterable_fun = 'To_the_time_second'
iterable_obj = iter(iterable_fun)

while True:
    try:
        item = next(iterable_obj)
        print(item)
    except StopIteration:
        break

# using list , Tuple, String, Dictionary

list1 = ["To", "Time", "date"]
print("List Iteration")
for i in list1:
    print(i)

# Iterating over a tuple (immutable)
tup = ("To", "Time", "date")
print("Tuple Iteration")
for i in tup:
    print(i)

# Iterating over a String
str = "To", "Time", "date"
print("String Iteration")
for i in str:
    print(i)

# Iterating over dictionary
d = dict()
d['xyz'] = 12345
d['abc'] = 34567
print("Dictionary Iteration")
for i in d:
    print("%s  %d" % (i, d[i]))

#


class Numbers:

  def __iter__(self):
    self.a = 1
    return self

  def __next__(self):
    if self.a <= 5:
      x = self.a
      self.a += 1
      return x
    else:
      raise StopIteration


obj = Numbers()
my_iter = iter(obj)

for x in my_iter:
  print(x)