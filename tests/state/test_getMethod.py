import os

import requests
from dotenv import load_dotenv

load_dotenv()

port = os.getenv('DATABASE_HOST')
baseUrl = f'http://{port}:8000'


# Getting all States objects
def test_state_get():
    headers = {
        'Accept': '*/*',
        'User-Agent': 'request',
    }
    url = f'{baseUrl}/states/'
    
    response = requests.get(url, headers=headers)
    expectedResponse = requests.get('https://httpbin.org/status/200')
    
    assert response.json()
    assert response.status_code == expectedResponse.status_code

# Getting a specific State object with a ID
def test_stateId_get():
    headers = {
        'Accept': '*/*',
        'User-Agent': 'request',
    }

    url = f'{baseUrl}/states/6'
    
    response = requests.get(url, headers=headers)
    expectedResponse = requests.get('https://httpbin.org/status/200')
    
    assert response.json()
    assert response.status_code == expectedResponse.status_code
	
# Sending a request with a object's ID that does not exists    	
def test_stateId_get404():
    headers = {
        'Accept': '*/*',
        'User-Agent': 'request',
    }

    url = f'{baseUrl}/states/30'
    
    response = requests.get(url, headers=headers)
    responseStatusCode = response.status_code
    bad_r = requests.get('https://httpbin.org/status/404')
    
    assert responseStatusCode == bad_r.status_code

