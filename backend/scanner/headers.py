import requests

def check_security_headers(url):
    try:
        response = requests.get(url, timeout=10)

        headers = response.headers

        findings = []

        security_headers = [
            "Content-Security-Policy",
            "X-Frame-Options",
            "Strict-Transport-Security",
            "X-Content-Type-Options"
        ]

        for header in security_headers:

            if header in headers:
                findings.append({
                    "header": header,
                    "status": "OK"
                })
            else:
                findings.append({
                    "header": header,
                    "status": "AUSENTE"
                })

        return {
            "url": url,
            "status_code": response.status_code,
            "findings": findings
        }

    except Exception as error:
        return {
            "error": str(error)
        }