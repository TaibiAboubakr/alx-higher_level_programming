#!/bin/bash
# Bash script that takes in a URL, sends a request to that URL, and displays the size of the body of the response

# Check if a URL is provided as an argument
if [ $# -eq 0 ]; then
    echo "Usage: $0 <URL>"
    exit 1
fi

# Get the URL from the command line argument
url=$1

# Use curl to send a request and measure the size of the response body
response=$(curl -sI "$url" | grep -i 'Content-Length' | awk '{print $2}' | tr -d '\r\n')
if [ -z "$response" ]; then
    echo "Unable to retrieve content size. Check the URL and try again."
    exit 1
fi

echo "$response"
.