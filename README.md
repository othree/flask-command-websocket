# flask-command-websocket

Run

```sh
gunicorn -k flask_sockets.worker server:app
```

ps. Flask-Sockets don't support uwsgi. Use Flask-uWSGI-WebSocket.
