#!/usr/bin/python3
"""  a Python script that takes in a letter and sends a POST request
to http://0.0.0.0:5000/search_user with the letter as a parameter.
"""
import requests
import sys


if __name__ == "__main__":
    query = "" if len(sys.argv) < 2 else sys.argv[1]
    params = {"q": query}
    req = requests.get("http://0.0.0.0:5000/search_user", params)
    try:
        data = req.json()
        if data and isinstance(data, dict) and 'id' in data and 'name' in data:
            print("[{}] {}".format(data['id'], data['name']))
        else:
            print("No result")
    except ValueError:
        print("Not a valid JSON")
