from flask import Flask
from flask_sockets import Sockets

import subprocess 


app = Flask(__name__)
sockets = Sockets(app)


@sockets.route('/echo')
def echo_socket(ws):
    while not ws.closed:
        ws.receive()
        
        # https://apple.stackexchange.com/questions/98106/how-to-produce-constant-output-in-a-terminal-window
        cmd = ["hexdump", "-C", "/dev/urandom", "|", "GREP_COLOR='1;32'", "grep", "--color=auto", "'ca fe'"]

        p = subprocess.Popen(cmd,
                             stdout=subprocess.PIPE,
                             stderr=subprocess.STDOUT)

        for line in iter(p.stdout.readline, b''):
            ws.send(">>> " + line.rstrip())


@app.route('/')
def hello_world():
    return 'Hello, World!'


if __name__ == "__main__":
    from gevent import pywsgi
    from geventwebsocket.handler import WebSocketHandler
    server = pywsgi.WSGIServer(('', 5000), app, handler_class=WebSocketHandler)
    server.serve_forever()
