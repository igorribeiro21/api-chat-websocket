from flask import Flask,render_template
from flask_socketio import SocketIO

app = Flask(__name__)

socketio = SocketIO(app)

@app.route('/render', methods=["GET"])
def render_template_index():
    return render_template(
        'index.html',
    )

@socketio.on('message')
def handle_message(message):
    return socketio.send(message)

if __name__ == "__main__":
    socketio.run(app)

