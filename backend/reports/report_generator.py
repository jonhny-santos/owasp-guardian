from datetime import datetime


def generate_html_report(result):

    html = f"""
<!DOCTYPE html>
<html>
<head>

<meta charset="UTF-8">

<title>OWASP Guardian Report</title>

<style>

body {{
    font-family: Arial;
    margin: 40px;
}}

h1 {{
    color: #2c3e50;
}}

.score {{
    font-size: 24px;
    font-weight: bold;
    color: green;
}}

.section {{
    margin-top: 20px;
    padding: 15px;
    border: 1px solid #ddd;
}}

</style>

</head>

<body>

<h1>🛡️ OWASP Guardian Report</h1>

<p>
Generated:
{datetime.now()}
</p>

<div class="section">

<h2>Security Score</h2>

<p class="score">
{result["score"]}/100
</p>

</div>

<div class="section">

<h2>HTTPS</h2>

<pre>{result["https"]}</pre>

</div>

<div class="section">

<h2>Headers</h2>

<pre>{result["headers"]}</pre>

</div>

<div class="section">

<h2>Clickjacking</h2>

<pre>{result["clickjacking"]}</pre>

</div>

<div class="section">

<h2>Technology</h2>

<pre>{result["technology"]}</pre>

</div>

<div class="section">

<h2>Cookies</h2>

<pre>{result["cookies"]}</pre>

</div>

</body>
</html>
"""

    return html