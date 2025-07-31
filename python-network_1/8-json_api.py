#!/usr/bin/python3
"""Sends POST request with q parameter and displays user info or error"""
import requests
import sys

if __name__ == "__main__":
    q = sys.argv[1] if len(sys.argv) > 1 else ""
    try:
        response = requests.post("http://0.0.0.0:5000/search_user", data={'q': q})
        r_json = response.json()
        if r_json:
            print(f"[{r_json.get('id')}] {r_json.get('name')}")
        else:
            print("No result")
    except ValueError:
        print("Not a valid JSON")
