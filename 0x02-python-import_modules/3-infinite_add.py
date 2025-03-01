#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv
    count = len(argv) - 1
    if count == 0:
        print(0)
    else:
        sum = 0
        for i in range(count):
            sum += int(argv[i + 1])
        print(sum)
