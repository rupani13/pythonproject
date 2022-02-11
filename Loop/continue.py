# All Continue Program

for i in range(1, 9):
    if i == 5:
        continue
    else:
        print("\nValue i:", i, end=" ")


# another program using continue

def Pattern(n):

    var = 0
    a = 1
    while a <= n:
        if var < a:
            print("* ", end="")
            var += 1
            continue

        if var == a:
            print("")
            a += 1
            var = 0


Pattern(5)
