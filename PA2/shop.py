# assignment: programming assignment 2
# author: Sijia Zhong		
# date: 01/19/2022
# file: shop.py implements a vending machine
# input: strings and numbers (integers)
# output: interactive messages (strings)

print("Vending Machine")
while True:
    # step 1: print the menu and get the user's choice
    greeting = "Please enter what product you want to buy[1-3] or select quit[4]:\n"
    choice1 = "1. A bottle of water - $1.99\n"
    choice2 = "2. A bottle of orange juice - $2.15\n"
    choice3 = "3. A bottle of ice tea - $2.49\n"
    choice4 = "4. Quit\n"
    num = input(greeting + choice1 + choice2 + choice3 + choice4)
    # step 2: depending on the user's choice
    while (num != '1' and num != '2' and num != '3' and num != '4'):
        print("You made a wrong choice!")
        num = input(greeting + choice1 + choice2 + choice3 + choice4)
    if (num == '1'):
        product_price = 199
        product_name = "water"
    elif (num == '2'):
        product_price = 215
        product_name = "orange juice"
    elif (num == '3'):
        product_price = 249
        product_name = "ice tea"
    elif (num == '4'):
        print("Goodbye!")
        quit()
    # step 3: ask for deposit
    deposit = 0
    while (deposit < product_price):
        deposit += int(input("Please deposit money (in cents): \n"))
    # step 4: calculate change, we use the greedy algorithm written below to get the minimum number of coins:
    change = deposit - product_price
    dollars = change // 100
    change = change % 100
    quarters = change // 25 
    change = change % 25
    dimes = change // 10
    change = change % 10
    nickels = change // 5
    change = change % 5
    cents = change
    # step 5: print the selected product and change
    print("You bought a bottle of {}.".format(product_name))
    if (dollars != 0 or quarters != 0 or dimes != 0 or nickels != 0 or cents != 0): 
        print("Your change is:")
        if (dollars != 0):
            print("Dollars - {}".format(dollars))
        if (quarters != 0):
            print("Quarters - {}".format(quarters))
        if (dimes != 0):
            print("Dimes - {}".format(dimes))
        if (nickels != 0):
            print("Nickels - {}".format(nickels))
        if (cents != 0):
            print("Cents - {}".format(cents))
