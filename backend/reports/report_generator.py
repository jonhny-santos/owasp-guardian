from datetime import datetime


def generate_html_report(result):

    score = result["score"]

    color = "#28a745"

    if score < 80:
        color = "#ffc107"

    if score < 50:
        color = "#dc3545"

    return f"""
<!DOCTYPE html>

<html>

<head>

<meta charset="UTF-8">

<title>OWASP Guardian Report</title>

<style>

body {{
    font-family: Arial;
    margin: 40px;
    background: #f4f4f4;
}}

.card {{
    background: white;
    padding: 20px;
    margin-bottom: 15px;
    border-radius: 8px;
}}

.score {{
    font-size: 40px;
    font-weight: bold;
    color: {color};
}}

h1 {{
    color: #1f2937;
}}

pre {{
    white-space: pre-wrap;
}}

</style>

</head>

<body>

<h1>🛡️ OWASP Guardian</h1>

<p>Generated: {datetime.now()}</p>

<div class="card">

<h2>Security Score</h2>

<div class="score">
{score}/100
</div>

</div>

<div class="card">
<h2>HTTPS</h2>
<pre>{result["https"]}</pre>
</div>

<div class="card">
<h2>Security Headers</h2>
<pre>{result["headers"]}</pre>
</div>

<div class="card">
<h2>Clickjacking</h2>
<pre>{result["clickjacking"]}</pre>
</div>

<div class="card">
<h2>Technology</h2>
<pre>{result["technology"]}</pre>
</div>

<div class="card">
<h2>Cookies</h2>
<pre>{result["cookies"]}</pre>
</div>

</body>

</html>
"""