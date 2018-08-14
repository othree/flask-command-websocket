from flask import Flask, send_from_directory
from flask_sockets import Sockets

import subprocess 


app = Flask(__name__, static_folder='www', static_url_path='/static')
sockets = Sockets(app)


app.add_url_rule(
    app.static_url_path + '/<path:filename>',
    endpoint='static', view_func=app.send_static_file)


@sockets.route('/job')
def echo_socket(ws):
    while not ws.closed:
        ws.receive()
        
        cmd = ["./run.sh"]

        p = subprocess.Popen(cmd,
                             stdout=subprocess.PIPE,
                             stderr=subprocess.STDOUT)

        for line in iter(p.stdout.readline, b''):
            ws.send(">>> " + line.rstrip())

        rc = p.returncode
        ws.send("[return code] %d" % rc)


@app.route('/')
def hello_world():
    return app.send_static_file('index.html')

