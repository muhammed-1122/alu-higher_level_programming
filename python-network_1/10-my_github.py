#!/usr/bin/python3
"""Displays GitHub user id using Basic Auth with username and token"""
import requests
import sys

if __name__ == "__main__":
    response = requests.get("https://api.github.com/user",
                            auth=(sys.argv[1], sys.argv[2]))
    try:
        print(response.json().get('id'))
    except Exception:
        print("None")
