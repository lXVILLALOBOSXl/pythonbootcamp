import requests

parameters = {
    "amount": 10,
    "type": "boolean"
}

response = requests.get("https://opentdb.com/api.php?amount=10&type=boolean", params=parameters)
response.raise_for_status()
response = response.json()["results"]

question_data = [
    {'question': item['question'], 'correct_answer': item['correct_answer']}
    for item in response
]

