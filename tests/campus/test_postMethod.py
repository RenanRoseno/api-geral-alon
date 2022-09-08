import os

import requests
from dotenv import load_dotenv

load_dotenv()

port = os.getenv('DATABASE_HOST')
baseUrl = f'http://{port}:8000'

# Sending any unrequired attribute like '"Campus construction date" : "2002"' or '"id": "777"' will not affect
# the request because of the serializer.
newCampus = {
    "name": "IF Dummy",
    "id_city": "104"
}

# A post request with a existent id_city value
def test_campus_post():
    headers = {
        'Accept': '*/*',
        'User-Agent': 'request',
    }

    url = f'{baseUrl}/campus/'
    
    response = requests.post(url, headers=headers, data=newCampus)
    expectedResponse = requests.get('https://httpbin.org/status/201')
    
    assert response.json()
    assert response.status_code == expectedResponse.status_code

# A city with a '355' id does not exist.
invalidCampus = {
    "name": "IF Dummy",
    "id_city": "355"
}

# A post request with a non-existent id_city value
def test_campus_post_InvalidCity():
    headers = {
        'Accept': '*/*',
        'User-Agent': 'request',
    }

    url = f'{baseUrl}/campus/'
    
    response = requests.post(url, headers=headers, data=invalidCampus)
    expectedResponse = requests.get('https://httpbin.org/status/400')
    
    assert response.json()
    assert response.status_code == expectedResponse.status_code
