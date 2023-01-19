#!/usr/bin/python3
# script that fetches https://alx-intranet.hbtn.io/status
# You must use the package urllib
import urllib.request

if __name__ == "__main__":
    #req = urllib.request.Request('https://alx-intranet.hbtn.io/status')
    #with urllib.request.urlopen(req) as response:
    with urllib.request.urlopen('https://alx-intranet.hbtn.io/status') as response:
        #reading the content of the response as html var
        html = response.read()
        #printing html content
        print("Body response:")
        print(f"\t- type: {type(html)}")
        print(f"\t- content: {html}")
        print(f"\t- utf8 content: {html.decode('utf-8')}")
