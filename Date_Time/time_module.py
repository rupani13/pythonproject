import time
curr = time.ctime(1627908313.717886)
print("Current time:", curr)
# Delaying Execution of programs
for i in range(4):
    time.sleep(1)
    print(i)

curr1 = time.localtime(1627908313.717886)
print("Local time:", curr1)