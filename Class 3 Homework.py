import time
print("Welcome to the pyramid maker. You will tell me how many rows to put into the pyramid.")
time.sleep(1)
rows = int(input("How many rows should there be in the pyramid?"))
for i in range(0,rows):
    print(" " * (rows - 1) + "* " * (i + 1))
    rows = rows - 1
while True:
    rows = int(input("And the next one?"))
    for i in range(0,rows):
        print(" " * (rows - 1) + "* " * (i + 1))
        rows = rows - 1
