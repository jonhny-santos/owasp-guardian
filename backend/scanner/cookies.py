import requests


def check_cookies(url):

    try:

        response = requests.get(
            url,
            timeout=10
        )

        cookies = []

        for cookie in response.cookies:

            cookies.append({
                "name": cookie.name,
                "secure": cookie.secure
            })

        return cookies

    except Exception as error:

        return {
            "error": str(error)
        }