#!/usr/bin/python3
if __name__ == "_main_":
    import sys
    result = 0
    for i in range(1, len(sys.argv)):
            result += int(sys.argv[i])
    print(result)
