#!/usr/bin/env python
#
# Run the server with
# $ export FLASK_APP=side-channel-monitor.py
# $ flask run --host=0.0.0.0
# or (if using uwsgi under virtualenv),
# ./bin/uwsgi --wsgfile ./side-channel-monitor.py --callable app --processes 4 --threads 2 --uid nobody --gid nogroup --http 127.0.0.1:7071 --logto log/side-channel-monitor.log
#
from flask import Flask, abort, request, Response, redirect
import os
import requests

app = Flask(__name__)

@app.route('/side-channel-monitor/healthcheck', methods=["GET"])
def heartbeat():
    resp = Response(response = "OK", status = 200, content_type = "text/plain")

    # Check for the maintenance file and signal graceful failure
    if(os.path.isfile("maintenance")):
        resp.status = "Under maintenance. Remove maintenance file when complete"
        resp.status_code = 503

    # Now check for the node statuses - A failure of one of these will
    # override the maintenance
    for node in ( "inbound", "outbound", "stats" ):
        try:
            req = requests.get("http://localhost:8080/" + node + "/isalive")

            if(req.status_code != 200):
                resp.status = "FAILED" 
                resp.status_code = req.status_code
        except requests.exceptions.ConnectionError as ce:
            resp.status_code = 400
            print("Connection refused. Check %s service" % node)

    return(resp)

if __name__ == "__main__":
    app.run()
