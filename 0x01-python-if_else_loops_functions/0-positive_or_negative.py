#!/usr/bin/python3
import random
number = random.randint(-10, 10)
if(number > 0):
    print("{0} is Positive".format(number))
elif(number < 0):
    print("0 is Negative".format(number))
else:
    print("is Zero")
