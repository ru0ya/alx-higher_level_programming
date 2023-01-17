#!/usr/bin/python3
"""takes url, sends request to url and displays id value"""


import sys
import urllib.request


if __name__ == "__main__":
    with urllib.request.urlopen(argv[1]) as response:
        print(response.getheader("X-Request-Id"))
