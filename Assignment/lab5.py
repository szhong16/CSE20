import re
#word = input("Please, enter a palindrome: ")
#backward = word[::-1]
#if (word == backward):
    #print("The word {} is a palindrome.".format(word))
#else:
    #print("The word {} is not a palindrome.".format(word))
#word = input("Please, enter a word: ")
#backward = word[::-1]
#print(backward)
text = input("Please enter an email address: ")
d = re.compile(r"[a-zA-Z0-9_]+@[a-zA-Z0-9_]+.[a-zA-Z0-9_]+")
x = d.search(text)
#print(x.group())
if x:
    print("{} is a valid email address".format(text))
else:
    print("{} is not a valid email address".format(text))
