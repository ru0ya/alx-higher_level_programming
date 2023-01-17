#!/usr/bin/python3
"""takes url, sends request and displays
body of response:
    if status code is >= 400 it prints its
    error code
    """

import sys
import requests


if __name__ == "__main__":
    url = sys.argv[1]

    req = requests.get(url)

    if req.status_code >= 400:
        print("Error code: {}", req.status_code)
    else:
        print(req.text)
