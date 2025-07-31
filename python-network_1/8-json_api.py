#!/usr/bin/python3
"""
Sends a POST request to a given URL with a search parameter `q`
and displays the JSON response in a specific format.

Handles missing parameters and invalid JSON responses gracefully.
"""

import requests
import sys

if __name__ == "__main__":
    url = "http://0.0.0.0:5000/search_user"
    q = sys.argv[1] if len(sys.argv) > 1 else ""
    data = {'q': q}

    try:
        response = requests.post(url, data=data)
        json_data = response.json()
        if json_data:
            print("[{}] {}".format(json_data.get("id"), json_data.get("name")))
        else:
            print("No result")
    except ValueError:
        print("Not a valid JSON")
