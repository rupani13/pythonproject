# Program the if else using loop
def even_odd_list():
    list = [5, 10, 15, 20]
    odd = []
    even = []
    for i in list:
        if i%2!=0:
            odd.append(i)
        else:
            even.append(i)
    print("odd list", odd)
    print("even list", even)

if __name__ == "__main__":
    even_odd_list()
