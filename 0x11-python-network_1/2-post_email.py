#!/usr/bin/python3
"""takes a URL and email and sends POST request to passed URL"""


import sys
import urllib.request
import urllib.parse


if __name__ == "__main__":
    url = sys.argv[1]
    email = sys.argv[2]

    data = urllib.parse.urlencode({"email": email}).encode('utf-8')
    agizo = urllib.request.Request(url, data=data, method='POST')

    with urllib.request.urlopen(agizo) as response:
        data = response.read()
        print(data.read.decode("utf-8"))
