import os

import requests
from dotenv import load_dotenv

load_dotenv()

port = os.getenv('DATABASE_HOST')
baseUrl = f'http://{port}:8000'

# Sending a Delete request that will remove a Campus object utilizing its id
def test_campus_delete():
    headers = {
        'Accept': '*/*',
        'User-Agent': 'request',
    }

    url = f'{baseUrl}/campus/4'
    
    response = requests.delete(url, headers=headers)
    expectedResponse = requests.get('https://httpbin.org/status/204')
    
    assert response.status_code == expectedResponse.status_code

# Sending a Delete request with a non-existent object's id
def test_campus_delete404():
    headers = {
        'Accept': '*/*',
        'User-Agent': 'request',
    }

    url = f'{baseUrl}/campus/355'
    
    response = requests.delete(url, headers=headers)
    expectedResponse = requests.get('https://httpbin.org/status/404')
    
    assert response.status_code == expectedResponse.status_code
