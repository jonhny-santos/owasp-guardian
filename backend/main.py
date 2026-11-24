from fastapi import FastAPI

from scanner.headers import check_security_headers
from scanner.https_checker import check_https
from scanner.clickjacking import check_clickjacking
from scanner.score import calculate_score
from scanner.technologies import detect_technology
from scanner.cookies import check_cookies

app = FastAPI()


@app.get("/scan")
def scan(url: str):

    headers_result = check_security_headers(url)

    score = calculate_score(headers_result)

    return {
        "score": score,
        "headers": headers_result,
        "https": check_https(url),
        "clickjacking": check_clickjacking(url),
        "technology": detect_technology(url),
        "cookies": check_cookies(url)
    }