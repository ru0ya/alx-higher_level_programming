#!/usr/bin/python3
"""takes url, sends request to url and displays id value"""


import sys
import urllib.request


if __name__ == "__main__":
    url = sys.argv[1]
    agizo = urllib.request.Request(url)

    with urllib.request.urlopen(agizo) as response:
        headers = response.info()
        x_request_id = headers.get("X-Request-Id")
        print(f"{ x_request_id}")
