import requests

def detect_technology(url):

    try:

        response = requests.get(
            url,
            timeout=10
        )

        return {
            "server":
            response.headers.get(
                "Server",
                "Unknown"
            )
        }

    except Exception as error:

        return {
            "error": str(error)
        }