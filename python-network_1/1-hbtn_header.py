#!/usr/bin/python3
"""Displays the value of X-Request-Id header from a given URL"""

import urllib.request
import sys

if __name__ == "__main__":
    req = urllib.request.Request(sys.argv[1])
    with urllib.request.urlopen(req) as response:
        print(response.headers.get("X-Request-Id"))
