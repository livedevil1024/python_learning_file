import os

API_KEY = os.getenv("NUTRITIONIX_API_KEY")
API_ID = os.getenv("NUTRITIONIX_API_ID")
SHEETY_USERNAME = os.getenv("SHEETY_USERNAME")
SHEETY_PASSWORD = os.getenv("SHEETY_PASSWORD")


import requests
from datetime import datetime

today_date = datetime.now().strftime(" %d/%m/%Y")
now_time = datetime.now().strftime(" %X ")

user_input = input("Enter your todays exercise : ")


sheety_endpoint = os.getenv("SHEETY_ENDPOINT")
endpoint ="https://app.100daysofpython.dev/v1/nutrition/natural/exercise"



headers = {
    "x-app-id": API_ID,
    "x-app-key": API_KEY
}

data = {
    "query" : user_input
}

response = requests.post(endpoint,headers=headers, json=data)
result = response.json()

for exer in result["exercises"] :
    sheets_input = {
        "workout": {
            "date": today_date,
            "time" : now_time,
            "exercise" : exer["name"].title(),
            "duration" : exer["duration_min"],
            "calories" : exer["nf_calories"],
        }
    }

sheety_respose = requests.post(sheety_endpoint,json=sheets_input)

print(sheety_respose.text)