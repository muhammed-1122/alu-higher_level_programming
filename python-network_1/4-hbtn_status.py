#!/usr/bin/python3
"""
Fetches https://intranet.hbtn.io/status using requests.
Prints the body response, its type, and content.
"""

import requests


if __name__ == "__main__":
    url = "https://intranet.hbtn.io/status"
    response = requests.get(url)
    content = response.text
    print("Body response:")
    print("\t- type: {}".format(type(content)))
    print("\t- content: {}".format(content))
