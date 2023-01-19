#!/bin/bash
#takes url as an argument,sends get request
curl -s -H "X-School-User-Id: 98" "$1"
