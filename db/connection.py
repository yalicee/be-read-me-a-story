import os

import firebase_admin
from firebase_admin import credentials

cred = credentials.Certificate(os.getenv("GOOGLE_APPLICATION_CREDENTIALS"))

app = firebase_admin.initialize_app(
    cred,
    {
        "databaseURL": "https://read-me-a-story-18a8d-default-rtdb.europe-west1.firebasedatabase.app/",
        "databaseAuthVariableOverride": {"uid": "override"},
    },
)
