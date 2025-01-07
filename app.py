from flask import Flask, render_template
from flask_socketio import SocketIO, send, emit

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your_secret_key'
socketio = SocketIO(app)

# Serve the index page
@app.route('/')
def index():
    return render_template('index.html')

# Handle WebSocket connections
@socketio.on('message')
def handle_message(msg):
    print('Message received: ' + msg)
    send('Message received: ' + msg, broadcast=True)

@socketio.on('custom_event')
def handle_custom_event(json):
    print('Custom event received: ' + str(json))
    emit('custom_response', {'response': 'Custom event received!'})

if __name__ == '__main__':
    socketio.run(app, debug=True)
