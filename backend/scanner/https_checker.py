def check_https(url):

    if url.startswith("https://"):

        return {
            "check": "HTTPS",
            "status": "OK"
        }

    return {
        "check": "HTTPS",
        "status": "INSEGURO"
    }