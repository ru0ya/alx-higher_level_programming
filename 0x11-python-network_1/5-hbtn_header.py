#!/usr/bin/python3
"""uses requests to take a url, send request and post its id"""

import requests
import sys

if __name__ == "__main__":
    url = sys.argv[1]

    req = requests.get(url)
    x_request_id = req.headers.get("X-Request-Id")
    print(f"{x_request_id}")
