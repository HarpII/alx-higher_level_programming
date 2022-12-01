#!/usr/bin/python3

if __name__ == "__main__":
    from sys import argv

    #total number of arguments
    argc = len(argv)
    sum = 0

    for i in range(1, argc):
       sum += int(argv[i])

    print("{}".format(sum))
