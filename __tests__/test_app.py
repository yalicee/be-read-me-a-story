import requests
import time

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
    url = "http://localhost:9000/.json?ns=stories"
    res = requests.get(url)
    story = res.json()["26437e71-8993-4025-a049-686d875fd0e1"]
    storyDict = res.json()
    storyKeys = storyDict.keys()
    storyList = list(storyKeys)

    assert res.status_code == 200
    assert story['title']== "The Twelve Princesses"
    assert story['created_at']== 1656575857
    assert story['created_by']== "andy@email.com"
    assert story["cover"]== "gs:/path/to/firebase/image.jpg"
    assert story["families"]== {"fid_0": True,"fid_1": True}
    assert story["chapters"]== [{
        "chapter_src": "gs:/path/to/recording/file.ogg",
        "created_by": "andy@email.com",
        "played": False
    }]
    assert len(storyList) == 2
    assert type (storyDict) is dict


def test_post_story_200():
    url = "http://localhost:9000/.json?ns=stories"
    res = requests.post(url, json={
            "title": "The Twelve Princesses",
            "created_by": "andy@email.com",
            "created_at": int(time.time()),
            "cover": "gs:/path/to/firebase/image.jpg",
            "chapters": [
                {
                    "created_by": "andy@email.com",
                    "chapter_src": "gs:/path/to/recording/file.ogg",
                    "played": False
                }
            ],
            "families": {
                "fid_0": True,
                "fid_1": True
            }
        })
    assert res.status_code==200

def test_post_story_400():
    url = "http://localhost:9000/.json?ns=stories"
    res = requests.post(url, "The Twelve Princesses")
    assert res.status_code==400