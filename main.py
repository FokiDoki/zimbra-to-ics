import os
from flask import Flask, request, abort, Response
import requests
from pykeepass import PyKeePass
from gevent import pywsgi

app = Flask(__name__)

KEEPASS_DB_PATH = os.getenv('KEEPASS_DB_PATH')
KEEPASS_PASS = os.getenv('KEEPASS_PASS')
ZIMBRA_URL = os.getenv('ZIMBRA_URL')
SSL_CERT = os.getenv("SSL_CERT")
SSL_KEY = os.getenv("SSL_KEY")

AUTH_PATH = "https://{zimbra_url}/home/{user}/Calendar?fmt=ics&icalAttach=inline&filename=t&emptyname=no&charset=UTF-8&callback=ZmImportExportController.exportErrorCallback__export2"

kp = PyKeePass(KEEPASS_DB_PATH, password=KEEPASS_PASS)


def getUserByToken(token):
    entries = kp.entries
    for entry in entries:
        if entry.notes!= None and entry.notes.strip() == token:
            return {'login': entry.username, 'password': entry.password, 'token': token}

@app.route('/<token>/calendar.ics', methods=['GET'])
def calendar(token):
    user = getUserByToken(token)
    if (user==None):
        return Response(status=404)
    calendar_data = getCalendar(user)
    return Response(calendar_data, mimetype='text/calendar')

def getCalendar(user):
    path = AUTH_PATH.format(zimbra_url=ZIMBRA_URL, user=user['login'])
    calendar = requests.get(path, auth=(user["login"], user["password"]))
    return calendar.text
    

if __name__ == '__main__':
    http_server = pywsgi.WSGIServer(('0.0.0.0', 4443), app, keyfile=SSL_KEY, certfile=SSL_CERT)
    http_server.serve_forever()