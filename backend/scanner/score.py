# scanner/score.py

def calculate_score(headers_result):

    score = 100

    for finding in headers_result["findings"]:

        if finding["status"] == "AUSENTE":
            score -= 25

    return score
