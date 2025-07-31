#!/usr/bin/python3
"""Sends request to URL and handles HTTPError exceptions with code output"""
import urllib.request
import urllib.error
import sys

try:
    with urllib.request.urlopen(sys.argv[1]) as response:
        print(response.read().decode('utf-8'))
except urllib.error.HTTPError as e:
    print("Error code:", e.code)
