#!/usr/bin/python3

if __name__ == "__main__":
    from sys import argv

    #total number of arguments
    argc = len(argv)
    c = 0

    for i in range(1, argc):
        c = c + 1
    
    if argc == 1:
        print("0 arguments.")
    elif c > 1:
        print("{} arguments:".format(c))
        for j in range(1, argc):
            print("{}: {}".format(j, argv[j]))
    else:
        print("{} argument:".format(c))
        print("{}: {}".format(c, argv[c]))
