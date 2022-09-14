import os

import requests
from dotenv import load_dotenv

load_dotenv()

port = os.getenv('DATABASE_HOST')
baseUrl = f'http://{port}:8000'

# Getting all Campus objects 
def test_campus_get():
    headers = {
        'Accept': '*/*',
        'User-Agent': 'request',
    }
    url = f'{baseUrl}/campus/'
    
    response = requests.get(url, headers=headers)
    expectedResponse = requests.get('https://httpbin.org/status/200')
    
    assert response.json()
    assert response.status_code == expectedResponse.status_code

# Getting a specific Campus object with a ID
def test_campusId_get():
    headers = {
        'Accept': '*/*',
        'User-Agent': 'request',
    }

    url = f'{baseUrl}/campus/2'
    
    response = requests.get(url, headers=headers)
    expectedResponse = requests.get('https://httpbin.org/status/200')
    
    assert response.json()
    assert response.status_code == expectedResponse.status_code
        
# Sending a request with a object's ID that does not exists 
def test_campusId_get404():
    headers = {
        'Accept': '*/*',
        'User-Agent': 'request',
    }

    url = f'{baseUrl}/campus/355'
    
    response = requests.get(url, headers=headers)
    bad_r = requests.get('https://httpbin.org/status/404')
    
    assert response.status_code == bad_r.status_code
