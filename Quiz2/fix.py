# This is the program code:
num1 = input("Enter the first number: ")
num2 = input("Enter the second number: ")
if num1 > num2:
    print ("The first number is greater than the second number:")
    print ("{} > {}".format(num1, num2)) # should print 'value of num1' > 'value of num2'
else:
    print ("The second number is greater than the first number:")
    print ("{} < {}".format(num1, num2)) # should print 'value of num1' < 'value of num2'
