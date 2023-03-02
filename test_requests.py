import requests
import json

base_url = "https://x-clients-be.onrender.com"
"auth/login"

def test_simple_req():
    resp = requests.get(base_url +'/company')

    response_body = resp.json()
    first_company = response_body[0]

    assert first_company["name"] == "Барбершоп 'ЦирюльникЪ'"
    assert resp.status_code == 200
    assert resp.headers["Content-Type"] == "application/json; charset=utf-8"
    resp.json()

def test_auth():

    creds = {
        'username' : 'michaelangelo',
        'password' : 'party-dude'
    }
    resp = requests.post(base_url +'/auth/login', json=creds)
    token = resp.json()["userToken"]
    assert resp.status_code == 201

def test_create_company():
    creds = {
        'username' : 'michaelangelo',
        'password' : 'party-dude'
    }
    company = {
        "name": "python",
        "description": "requests"
    }
    # Авторизация
    resp = requests.post(base_url +'/auth/login', json=creds)
    token = resp.json()["userToken"]

    # создание
    my_headers = {}
    my_headers["x-clien-token"] = token
    

    resp = requests.post(base_url +'/company', json=company, headers=my_headers)
    assert resp.status_code == 201