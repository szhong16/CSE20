# assignment: programming assignment 1
# author: Sijia Zhong	
# date: 01/06/2022
# file: hello.py is a program that asks the user to enter user's name,
#       age, and favorite movie and outputs a greeting message that
#       include the information about the user
# input: string data
# output: string data

name = input("Hello! What is your name?\n")
age = int(input("What is your age?\n"))
favMovie = input("What is your favorite movie?\n")
str0 = "Nice to meet you, {}.\n".format(name)
str1 = "You are {} years old".format(str(age))
str2 = " and your favorite movie is {}.".format(favMovie)
print(str0 + str1 + str2)
