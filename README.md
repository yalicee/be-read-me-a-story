# Read Me A Story

Read Me A Story is an app that allows family members to record, upload and playback bedtime stories for young children in the family when they are unable to read them in person.

A parent can sign up to the app, create a family group and invite their partner or relatives to join. Family members can then choose to record and upload stories, or view a list of stories created by the family. Stories can be selected from the list and played back to the child.

To find out more about the project watch the [product demonstration](#), visit the [live app](#) or take a look at the accompanying [front-end respository](https://github.com/yangalexyangg/fe-read-me-a-story/).

## Installation

Follow the instructions below to configure and run your own instance of the Read Me A Story API.

### Requirements

This API was built using Flask and requires Python 3.7 or above.

### Setup the project

To run the project locally, first download the source, create a virtual environment and install the dependencies.

```
git clone https://github.com/yangalexyangg/be-read-me-a-story.git
cd be-read-me-a-story
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

Note: Use `deactivate` to leave the virtual environment at any point.

### Configure Firebase

You will need to create a [Firebase](https://firebase.google.com/) project, enable Realtime Database and generate a Service Account key.

After downloading the key, set the `GOOGLE_APPLICATION_CREDENTIALS` environment variable:

```
export GOOGLE_APPLICATION_CREDENTIALS="/home/username/path/to/repository/service-account-file.json"
```

### Usage

Having setup the project you can start the local server:

```
flask run
```

By default the server will start on [http://127.0.0.1:5000](http://127.0.0.1:5000). If you want to run the server in debug mode, run `export FLASK_ENV=development` before starting Flask.

## About

Read Me A Story was created by Minimum Viable Panic as their final project in the [Northcoders](https://northcoders.com) coding bootcamp.

Minimum Viable Panic are [Rob](https://github.com/RobParry6/), [Charlotte](https://github.com/321jellyfish/), [Alex](https://github.com/yangalexyangg/) and [Andy](https://github.com/akflds/).

### Acknowledgements

Thanks to August, Emily and the other Northcoders mentors for their support!
