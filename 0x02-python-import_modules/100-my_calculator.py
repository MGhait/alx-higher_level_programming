#!/usr/bin/python3
if __name__ == "__main__":
    from calculator_1 import add, sub, mul, div
    from sys import argv, exit
    args = len(argv) - 1
    if args != 3:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        exit(1)
    else:
        first = int(argv[1])
        last = int(argv[3])
        op = argv[2]
        if op == '+':
            print("{} + {} = {}".format(first, last, add(first, last)))
        elif op == '-':
            print("{} - {} = {}".format(first, last, sub(first, last)))
        elif op == '*':
            print("{} * {} = {}".format(first, last, mul(first, last)))
        elif op == '/':
            print("{} / {} = {}".format(first, last, div(first, last)))
        else:
            print("Unknown operator. Available operators: +, -, * and /")
            exit(1)
