from flask import Flask, render_template
from flask_socketio import SocketIO, emit
from flask_cors import CORS

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret'
socket_io = SocketIO(app)
CORS(app, resources={r"/*": {"origins": '*'}})

@app.route("/")
def index():
    """load landing page"""
    return render_template("index.html")

@socket_io.on("message")
def handle_message(message):
    """Handle messgae event"""
    print("recieved: " + message)
    emit('message', message, broadcast=True)

if __name__ == "__main__":
    socket_io.run(app, debug=True)