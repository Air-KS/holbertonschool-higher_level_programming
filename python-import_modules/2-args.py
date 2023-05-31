#!/usr/bin/python3

if __name__ == "__main__":
    import sys
    count = len(sys.argv) - 1

    if count < 0 or count == 0:
        print("Not argument")
    else:
        print("{} Argument :".format(count))
    for index in range(1, count + 1):
        # print(index, ":", sys.argv[index])
        print("{}: {}".format(index, sys.argv[index]))
