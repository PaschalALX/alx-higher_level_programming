#!/usr/bin/python3
import random

number = random.randint(-10, 10)

print(number, "is positive")\
     if number > 0 else print(number, "is zero")\
     if number == 0 else print(number, "is negative")
