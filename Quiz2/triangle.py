num = int(input("Please enter a number: "))
count = 0
row = num
for i in range(num):
    for j in range(count):
        print(" ", end = "")
    for z in range(row):
        print("*", end = "")
    row -= 1
    count += 1
    print("\n", end = "")
