#!/usr/bin/python3
if __name__ == "__main_":
    import sys
    n = len(sys.argv)

    if n == 1:
        print(f"{n} argument.", n- 1)
    elif n == 2:
        print(f"{n} arguments:", n - 1)
    else:
        print(f"{n} arguments:", n - 1)

    for i in range(1, n):
        print("{}:{}".format(i, sys.argv[i]))
