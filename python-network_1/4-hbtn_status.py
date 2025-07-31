#!/usr/bin/python3
"""
Fetches a URL (default: https://intranet.hbtn.io/status)
and prints the response body with its type and content.
"""

import requests
import sys

if __name__ == "__main__":
    url = sys.argv[1] if len(sys.argv) > 1 else "https://intranet.hbtn.io/status"
    response = requests.get(url)
    content = response.text

    print("Body response:")
    print("\t- type: {}".format(type(content)))
    print("\t- content: {}".format(content))

