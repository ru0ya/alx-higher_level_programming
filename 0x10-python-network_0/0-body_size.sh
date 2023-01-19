#!/bin/bash
#takes in a URL, sends it a request and displays size of the body of response
curl -s "$1" | wc -c
