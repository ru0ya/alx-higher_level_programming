#!/bin/bash
#takes in a URL, sends it a request and displays size of the body of response
curl -s -I "$1" | awk "/^Content-Length/ { print $2}"
