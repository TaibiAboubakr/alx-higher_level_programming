#!/usr/bin/python3
""" a Python script that takes your GitHub credentials (username and password)
and uses the GitHub API to display your id
"""
import requests
import sys


if __name__ == "__main__":
    username, password = sys.argv[1:]
    credentials = (username, password)
    api_url = f"https://api.github.com/users/{username}"
    try:
        resp = requests.get(api_url, auth=credentials)
        if resp.status_code == 200:
            data = resp.json()
            print(data.get('id'))
        else:
            print("None")
    except ValueError:
        print("Not a valid JSON")
