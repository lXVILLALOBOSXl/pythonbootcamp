import requests
import os
from datetime import datetime

#Nutritionix API data
NUTRITIONIX_ID = os.environ.get("NUTRITIONIX_ID")
NUTRITIONIX_KEY = os.environ.get("NUTRITIONIX_KEY")
NUTRITIONIX_ENDPOINT = "https://trackapi.nutritionix.com/v2/natural/exercise"

NUTRITIONIX_HEADERS = {
    "x-app-id": NUTRITIONIX_ID,
    "x-app-key": NUTRITIONIX_KEY
}


GENDER = "male"
WEIGHT_KG = 80
HEIGHT_CM = 182
AGE = 21
exercise_text = input("Tell me which exercises you did: ")

EXERCISE_DATA = {
    "query":exercise_text,
    "gender":GENDER,
    "weight_kg":WEIGHT_KG,
    "height_cm":HEIGHT_CM,
    "age":AGE
}

# Nutritionix API petition
try:   
    global response
    response = requests.post(url=NUTRITIONIX_ENDPOINT, json=EXERCISE_DATA, headers=NUTRITIONIX_HEADERS)
    response.raise_for_status()
except:
    print("Error has occured trying make Nutritionix petition")

exercises = response.json()["exercises"]

#Sheety API data
SHEETY_USERNAME = os.environ.get("SHEETY_USERNAME")
PROJECT_NAME = os.environ.get("PROJECT_NAME")
SHEET_NAME = os.environ.get("SHEET_NAME")
SHEETY_ENDPOINT = f"https://api.sheety.co/{SHEETY_USERNAME}/{PROJECT_NAME}/{SHEET_NAME}"

#Bearer Token Authentication
bearer_headers = {
    "Authorization": os.environ.get("AUTHORIZATION_BEARER")
}



today_date = datetime.now().strftime("%d/%m/%Y")
now_time = datetime.now().strftime("%X")

for exercise in exercises:

    exercise = {
        "workout":{
            "date":today_date,
            "time":now_time,
            "exercise":exercise['user_input'],
            "duration":exercise['duration_min'],
            "calories":exercise['nf_calories']
        }
    }

    # Nutritionix API petition
    try:   
        response = sheet_response = requests.post(
            url=SHEETY_ENDPOINT, 
            json=exercise, 
            headers=bearer_headers
        )
        response.raise_for_status()
    except:
        print(f"Error has occured trying make Sheety's petition")