from flask import Flask
from google.cloud import firestore
from unittest.mock import Mock

from google.auth.credentials import Credentials
from os import environ

app = Flask(__name__)


@app.route("/")
def index():
    if environ.get("FIRESTORE_EMULATOR_HOST"):
        print('EMULATOR CONNECTION')
    dev_creds = Mock(spec=Credentials)
    dev_creds.id_token = ""
    db = firestore.Client(project="dummy-project", credentials=dev_creds)
    data = {u"user_id": 123, u"user_stuff": "slfk"}

    doc_ref = db.collection(u'testcollection').document()
    doc_ref.set(data)

    return "Hello World!"