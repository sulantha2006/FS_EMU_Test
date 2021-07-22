from flask import Flask
from google.cloud import firestore
from unittest import mock
from google.auth.credentials import Credentials

app = Flask(__name__)


@app.route("/")
def index():
    dev_creds = mock.MagicMock(spec=Credentials)
    db = firestore.Client(project="dev", credentials=dev_creds)
    data = {u"user_id": 123, u"user_stuff": "slfk"}

    doc_ref = db.collection(u'testcollection').document()
    doc_ref.set(data)
    return "Hello World!"