#!/usr/bin/python3
def fizzbuzz():
    for i in range(1, 101):
        if i % 3 == 0:
            print("Fizz", end=' ' if not i % 5 == 0 else '')
        if i % 5 == 0:
            print("Buzz", end=' ')
        if not (i % 3 == 0 or i % 5 == 0):
            print(i, end=' ')
