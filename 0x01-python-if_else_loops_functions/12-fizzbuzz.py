#!/usr/bin/python3

def fizzbuzz():
    [print("FizzBuzz", end=" ") if not (x % 3) and not (x % 5)
        else print("Fizz", end=" ") if not (x % 3)
        else print("Buzz", end=" ") if not (x % 5)
        else print(x, end=" ") for x in range(1, 101)]
