def generate_html_report(result):

    html = f"""
    <html>
    <head>
        <title>OWASP Guardian Report</title>
    </head>
    <body>

        <h1>OWASP Guardian</h1>

        <h2>Score: {result["score"]}</h2>

        <pre>{result}</pre>

    </body>
    </html>
    """

    return html