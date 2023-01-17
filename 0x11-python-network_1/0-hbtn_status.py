#!/usr/bin/python3

import urllib.request


if __name__ == "__main__":
    with urllib.request.urlopen("https://alx-intranet.hbtn.io/status") as reply:
        data = reply.read()
        print(" Body response:")
        print("type: {}/t".format(type(data)))
        print("content: {}/t".format(data))
        print("utf8 content: {}/t".format(data.decode("utf-8")))

