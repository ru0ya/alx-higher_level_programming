#!/usr/bin/python3
"""uses requests to fetch a url"""

import requests

if __name__ == "__main__":
    response = requests.get("https://alx-intranet.hbtn.io/status")
    print("Body response:")
    print("- type: {} ".format(type(response.text)))
    print("- content: {} ".format(response.text))
