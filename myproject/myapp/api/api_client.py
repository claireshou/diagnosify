import os
import requests
from dotenv import load_dotenv


# Load environment variables from .env file
load_dotenv()

def Init_Session():
    url = "https://endlessmedicalapi1.p.rapidapi.com/InitSession"

    headers = {
        "x-rapidapi-key": os.getenv("x-rapidapi-key"),
        "x-rapidapi-host": "endlessmedicalapi1.p.rapidapi.com"
    }

    response = requests.get(url, headers=headers)

    # Check if the response is successful
    if response.status_code == 200:
        response_data = response.json()
        print(response_data)  # Print the full response for debugging

        # Extract the SessionID
        session_id = response_data.get('SessionID')
        if session_id:
            print(f"Session ID: {session_id}")
        else:
            print("SessionID not found in the response.")
    else:
        print(f"Error: {response.status_code} - {response.text}")
        
    return session_id

def Accept_Terms(session_id):
    url = "https://endlessmedicalapi1.p.rapidapi.com/AcceptTermsOfUse"

    payload = {"SessionID": session_id,
               "passphrase":"I have read, understood and I accept and agree to comply with the Terms of Use of EndlessMedicalAPI and Endless Medical services. The Terms of Use are available on endlessmedical.com"}
    headers = {
        "x-rapidapi-key": os.getenv("x-rapidapi-key"),
        "x-rapidapi-host": "endlessmedicalapi1.p.rapidapi.com",
        "Content-Type": "application/json"
    }

    response = requests.post(url, params=payload, headers=headers)

    print(response.json())

def Get_Features():
    url = "https://endlessmedicalapi1.p.rapidapi.com/GetFeatures"

    headers = {
        "x-rapidapi-key": os.getenv("x-rapidapi-key"),
        "x-rapidapi-host": "endlessmedicalapi1.p.rapidapi.com"
    }

    response = requests.get(url, headers=headers)

    print(response.json())    

def Update_Features(symptom_name, session_id):
    url = "https://endlessmedicalapi1.p.rapidapi.com/UpdateFeature"

    payload = {"name": symptom_name,
               "value": "1",
               "SessionID": session_id}
    headers = {
        "x-rapidapi-key": os.getenv("x-rapidapi-key"),
        "x-rapidapi-host": "endlessmedicalapi1.p.rapidapi.com",
        "Content-Type": "application/json"
    }

    response = requests.post(url, params=payload, headers=headers)

    print(response.json())
    
def Analyze(session_id):
    url = "https://endlessmedicalapi1.p.rapidapi.com/Analyze"
    
    querystring = {"SessionID": session_id}

    headers = {
        "x-rapidapi-key": os.getenv("x-rapidapi-key"),
        "x-rapidapi-host": "endlessmedicalapi1.p.rapidapi.com",
         "SessionID": session_id
    }

    response = requests.get(url, headers=headers, params=querystring)

    print(response.json())
        

session_id = Init_Session()
Accept_Terms(session_id)
Update_Features("NotSoSeasonal", session_id)
Analyze(session_id)
#Get_Features()
    

