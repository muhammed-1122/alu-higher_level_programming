#!/usr/bin/python3
"""Sends request to a URL and displays the X-Request-Id header value"""
import urllib.request
import sys

url = sys.argv[1]
with urllib.request.urlopen(url) as response:
    print(response.headers.get('X-Request-Id'))

