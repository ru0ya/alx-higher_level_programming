#!/usr/bin/python3
"""takes url,sends request to url and displays body of response"""

import urllib.request
import sys


if __name__ == "__main__":
    url = sys.argv[1]

    try:
        with urllib.request.urlopen(url) as response:
            print(response.read().decode('utf-8'))

    except urllib.error.HTTPError as err:
        print("Error code:", err.code)
