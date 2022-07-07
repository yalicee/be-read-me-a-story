import os

import firebase_admin
from firebase_admin import credentials

if "GOOGLE_APPLICATION_CREDENTIALS" in os.environ:
    cred = credentials.Certificate(os.getenv("GOOGLE_APPLICATION_CREDENTIALS"))
else:

    ENV_KEYS = {
        "type": "service_account",
        "private_key_id": os.getenv("FIREBASE_PRIVATE_KEY_ID"),
        "private_key": os.getenv("FIREBASE_PRIVATE_KEY").replace("\\n", "\n"),
        "client_email": os.getenv("FIREBASE_CLIENT_EMAIL"),
        "client_id": os.getenv("FIREBASE_CLIENT_ID"),
        "token_uri": os.getenv("FIREBASE_TOKEN_URI"),
        "project_id": os.getenv("FIREBASE_PROJECT_ID"),
    }

    cred = credentials.Certificate(ENV_KEYS)


app = firebase_admin.initialize_app(cred, {
    'databaseURL': 'https://read-me-a-story-18a8d-default-rtdb.europe-west1.firebasedatabase.app/',
    'databaseAuthVariableOverride': {
        'uid': 'override'
    },
})
