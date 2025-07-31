#!/usr/bin/python3
"""Displays the value of X-Request-Id in the response header"""
import requests
import sys

if __name__ == "__main__":
    response = requests.get(sys.argv[1])
    print(response.headers.get("X-Request-Id"))
