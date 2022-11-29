#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)

last_number = abs(number) % 10

print(f"Last digit of {number} is", end=" ")

if last_number > 5 and number > 0:
    print(f"{last_number} and is greater than 5")
elif last_number == 0:
    print(f"{last_number } and is 0")
elif last_number < 6 or number < 0:
    last_number = -last_number if number < 0 else last_number
    print(f"{last_number} and is less than 6 and not 0")
