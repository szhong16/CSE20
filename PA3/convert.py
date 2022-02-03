# assignment: programming assignment 3
# author: Sijia Zhong
# date: 2022.02.02
# file: convert.py is a program that converting
      # Fahrenheit to Celsius or Pounds to kg or Miles to km
      # base on what user choose
# input: the options for converting[F/f, P/p, M/m];
       # the number for converting
       # the options for continue or not[Y/N]
# output: A line which contains the input value and the output value after converting

import re
import math

#Global variables 

str1 = "Welcome to the SI Unit Converter!\n"
str2 = "Please choose one of the following conversions:\n"
str3 = "Fahrenheit to Celsius - F\n"
str4 = "Pounds to kg - P\n"
str5 = "Miles to km - M\n"
str6 = "Do you want to continue? [Y/N]: \n"
fstr = "Please enter a temperature in Fahrenheit: \n"
pstr = "Please enter pounds: \n"
mstr = "Please enter miles: \n"
numEx = re.compile(r"[0-9]+")
floatEx = re.compile(r"[0-9]+.[0-9]+")

def format (num, precision = 2):
    theNum = floatEx.match(str(num))
    if theNum:
        theNum = theNum.group()
        frac = theNum.split(".")[1]
        if frac == "0":
            theNum = round(float(theNum))
        else:
            theNum = round(float(theNum), 2)
        return theNum
    elif float(num) < 0:
        number = str(float(num))
        frac = number.split(".")[1]
        if frac == "0":
            number = round(float(number))
        else:
            number = round(float(number), 2)
            return number
    else:
        return num

def isfloat (token):
    check = floatEx.match(token)
    if token.isdigit() or check:
        return True
    else:
        return False

def fahrenheit_celsius ():
    x = float(fahrenheit)
    celsius = (x - 32) * 5 / 9
    celsius = format(celsius)
    return celsius

def pounds_kg ():
    y = float(pound)
    kg = y * 0.45359237
    kg = format(kg)
    return kg

def miles_km ():
    z = float(mile)
    km = z * 1.609344
    km = format(km)
    return km

if __name__ == '__main__':
    print(str1)
    while (True):
        theChoice = input(str2 + str3 + str4 + str5)
        if theChoice == "F" or theChoice == "f":
            fahrenheit = input(fstr)
            while not isfloat(fahrenheit):
                print("You did not enter a number.")
                fahrenheit = input(fstr)
            if isfloat(fahrenheit):
                c = fahrenheit_celsius ()
                print("{} Fahrenheit corresponds to {} Celsius.".format(format(fahrenheit), c))
                chooseOne = input(str6)
                if (chooseOne == "Y" or chooseOne == "y"):
                      continue
                else:
                    print("Goodbye!")
                    exit()
        elif theChoice == "P" or theChoice == "p":
            pound = input(pstr)
            while not isfloat(pound):
                print("You did not enter a number.")
                pound = input(pstr)
            if isfloat(pound):
                kg = pounds_kg ()
                print("{} pounds corresponds to {} kg.".format(format(pound), kg))
                chooseOne = input(str6)
                if (chooseOne == "Y" or chooseOne == "y"):
                    continue
                else:
                    print("Goodbye!")
                    exit()
        elif theChoice == "M" or theChoice == "m":
            mile = input(mstr)
            while not isfloat(mile):
                print("You did not enter a number.")
                mile = input(mstr)
            if isfloat(mile):
                km = miles_km ()
                print("{} miles corresponds to {} km.".format(format(mile), km))
                chooseOne = input(str6)
                if (chooseOne == "Y" or chooseOne == "y"):
                    continue
                else:
                    print("Goodbye!")
                    exit()
        else:
            print("You did not choose correctly.")
            continue
