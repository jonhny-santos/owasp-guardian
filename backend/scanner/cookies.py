# backend/scanner/cookies.py

import requests


def check_cookies(url):

    response = requests.get(url)

    cookies = []

    for cookie in response.cookies:

        cookies.append({
            "name": cookie.name
        })

    return cookies