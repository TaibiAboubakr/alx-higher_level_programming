#!/usr/bin/python3
"""a Python script that takes in a URL, sends a request to the URL
and displays the value of the X-Request-Id variable found in the header
of the response."""
import urllib.request
import urllib.parse
import sys


if __name__ == "__main__":

    url = sys.argv[1]
    email = sys.argv[2]
    data = urllib.parse.urlencode({'email': email}).encode('utf-8')
    req = urllib.request.Request(url, data=data, method="POST")
    with urllib.request.urlopen(req) as resp:
        resp_content = resp.read().decode("utf-8")
        print(resp_content)
