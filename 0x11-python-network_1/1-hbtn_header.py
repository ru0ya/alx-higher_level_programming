#!/usr/bin/python3
# Sends a request to the URL and displays the value of the X-Request-Id variable found in the header of the response.
import urllib.request
import sys

if __name__ == "__main__":
     URL = sys.argv[1]
     with urllib.request.urlopen(URL) as response:
        X_Request_d = response.headers.get("X-Request-Id")
        print(f"{X_Request_d}")
