import requests

def check_clickjacking(url):

    response = requests.get(url)

    if "X-Frame-Options" in response.headers:

        return {
            "status": "PROTEGIDO"
        }

    return {
        "status": "VULNERAVEL"
    }
