import os

import requests
from dotenv import load_dotenv

load_dotenv()

port = os.getenv('DATABASE_HOST')
baseUrl = f'http://{port}:8000'

newData = {
    "name": "IF Dummy Neo",
    "id_city": 59
}

# A put request with a existent id value
def test_campus_put():
    headers = {
        'Accept': '*/*',
        'User-Agent': 'request',
    }

    url = f'{baseUrl}/campus/3/'
    
    response = requests.put(url, headers=headers, data=newData)
    expectedResponse = requests.get('https://httpbin.org/status/200')
    
    assert response.json()
    assert response.status_code == expectedResponse.status_code

# A put request with a non-existent id value
def test_campus_put404():
    headers = {
        'Accept': '*/*',
        'User-Agent': 'request',
    }

    url = f'{baseUrl}/campus/355/'
    
    response = requests.put(url, headers=headers, data=newData)
    expectedResponse = requests.get('https://httpbin.org/status/404')
    
    assert response.json()
    assert response.status_code == expectedResponse.status_code
