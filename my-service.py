#!/usr/bin/env python
#
# Run the server with
# $ export FLASK_APP=my-service.py
# $ flask run --host=0.0.0.0
#
# or by creating an eps-service.ini
# uwsgi --ini eps-service.ini
# or (by just using uwsgi),
# ./bin/uwsgi --wsgfile ./my-service.py --callable app --processes 4 --threads 2 --uid nobody --gid nogroup --http 0.0.0.0:8080
#
from flask import Flask, abort, request, Response, redirect

app = Flask(__name__)

@app.route('/inbound/isalive', methods=["GET"])
def inboundIsAlive():
    return "OK"

@app.route('/outbound/isalive', methods=["GET"])
def outboundIsAlive():
    return "OK"

@app.route('/stats/isalive', methods=["GET"])
def statsIsAlive():
    return "OK"

if __name__ == "__main__":
    app.run()
