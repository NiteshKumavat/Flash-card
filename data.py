import requests

response = requests.get(url="https://opentdb.com/api.php?amount=10&type=multiple")
all_questions = response.json()["results"]
