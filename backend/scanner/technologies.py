import requests


def detect_technology(url):

    response = requests.get(url)

    server = response.headers.get(
        "Server",
        "Desconhecido"
    )

    return {
        "server": server
    }