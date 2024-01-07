#!/usr/bin/python3
""" a Python script that takes your GitHub credentials (username and password)
and uses the GitHub API to display your id
"""
import requests
import sys


if __name__ == "__main__":
    username, password = sys.argv[1:]
    credentials = {"user": username,
                   "pass": password}
    req = requests.get(f"https://api.github.com/users/{username}")
    try:
        data = req.json()
        if data:
            print(data.get('id'))
        else:
            print("No result")
    except ValueError:
        print("Not a valid JSON")
