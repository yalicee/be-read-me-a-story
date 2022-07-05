import requests


def test_app():
    url = "http://127.0.0.1:5000"
    res = requests.get(url)
    assert res.status_code == 200
    print(res.text)
    assert res.text == "<p>Hello, World!</p>"


def test_app_error():
    url = "http://127.0.0.1:5000/doggos"
    res = requests.get(url)
    assert res.status_code == 404
