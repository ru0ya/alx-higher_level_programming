#!/usr/bin/python3
for num in range(0,100):
    if num == 99:
     print("{}".format(num), end= '\n')
    else:
            print("{:02}".format(num), end = ",")
