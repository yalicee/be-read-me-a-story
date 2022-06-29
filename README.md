# Installation

```
python3 -m venv venv
source venv/bin/activate
export GOOGLE_APPLICATION_CREDENTIALS="/home/username/path/to/repository/service-account-file.json"

pip install -r requirements.txt
```

Note: you will need to initalise the virtual environement whenever you want to run the project, and export your credential key. You may need to re-install dependencies when more are added.

To exit the virtual environment, run:

```
deactivate
```

## Configuring firebase-admin

To access firebase you will need a service agent key. These should be added to the root of this direction, but you should NOT commit them (there is a .gitignore inplace).

# Running

Type these in terminal to run flask/pytest:

```
flask run
pytest
```
