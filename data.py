import requests

# Gets questions from the opendatabase API
parameters = {
    "amount": 10,
    "type": "boolean"
}

questions = requests.get(url="https://opentdb.com/api.php", params=parameters)
questions.raise_for_status()
q_dict = questions.json()

question_data = q_dict["results"]
