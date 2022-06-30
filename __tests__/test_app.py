import requests
import json

def test_app():
    url = "http://127.0.0.1:5000"
    res = requests.get(url)
    assert res.status_code == 200
    assert res.text == "<p>Hello, World!</p>"


def test_app_error():
    url = 'http://127.0.0.1:5000/doggos'
    res = requests.get(url)
    assert res.status_code == 404


def test_get_stories():
    url = "http://127.0.0.1:5000/stories"
    res = requests.get(url)
    # resDict = json.loads(res)
    # keyslist = list(resDict.keys())
    assert res.status_code == 200
    assert res.json()["26437e71-8993-4025-a049-686d875fd0e1"]['title']== "The Twelve Princesses"
    # assert type(json.loads(res)) is dict 
    # assert res.json()[]
# Loop over keyslist and assert the res.json
# check the shape of each story object within the json
