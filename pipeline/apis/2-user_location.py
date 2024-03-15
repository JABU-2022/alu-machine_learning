#!/usr/bin/env python3
"""
Prints the location of a specific Github user
"""
import requests
import sys
from datetime import datetime

def get_user_location(url):
    headers = {'Accept': 'application/vnd.github.v3+json'}
    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        location = response.json().get('location', 'Not available')
        if location:
            print(location)
        else:
            print('Not available')

    elif response.status_code == 404:
        print("Not found")

    elif response.status_code == 403:
        rate_limit_reset = int(response.headers.get('X-Ratelimit-Reset', 0))
        reset_time = datetime.fromtimestamp(rate_limit_reset)
        minutes = (reset_time - datetime.now()).total_seconds() / 60
        print(f"Reset in {int(minutes)} min")

if __name__ == '__main__':
    if len(sys.argv) == 2:
        get_user_location(sys.argv[1])
    else:
        print("Usage: ./2-user_location.py <URL>")

