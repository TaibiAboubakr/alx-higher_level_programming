#!/usr/bin/python3
"""a Python script that fetches https://alx-intranet.hbtn.io/status"""
import urllib.request
with urllib.request.urlopen('https://alx-intranet.hbtn.io/status') as response:
    html = response.read()
    utf8_content = html.decode('utf-8')
    print("Body response:")
    print(f"\t- type: {type(html)}")
    print(f"\t- content: {html}")
    print(f"\t- utf8 content: {utf8_content}")
