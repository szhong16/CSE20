def draw_open_square (size):
    for i in range(0, size):
        for j in range(0, size):
            if (i == 0 or i == size - 1):
                print("+",end = "")
            elif (j == 0 or j == size - 1):
                print("+", end = "")
            else:
                print(" ", end = "")
        print("")
        
# main
while True:
    size = input("Enter the size of an open square. Enter 0 to exit the program: ")
    if size == '0':
        break
    elif size.isdigit():
        draw_open_square(int(size))
    else:
        continue
