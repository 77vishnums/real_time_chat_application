from flask import Flask, render_template
from flask_socketio import SocketIO, send

# Initialize the Flask application
# The template_folder and static_folder arguments tell Flask where to find the HTML and CSS/JS files.
app = Flask(__name__, template_folder='.', static_folder='.')

# It's good practice to have a secret key for security
app.config['SECRET_KEY'] = 'your-very-secret-key'

# Initialize SocketIO for real-time communication
socketio = SocketIO(app)

# Define the route for the main chat page
@app.route('/')
def index():
    """Serves the main HTML file for the chat application."""
    return render_template('index.html')

# Define the event handler for receiving messages from clients
@socketio.on('message')
def handle_message(msg):
    """
    Handles a message sent from a client.
    It prints the message to the console for logging and then
    broadcasts the message to all connected clients so everyone sees it.
    """
    print('Message received: ' + msg)
    # The 'send' function from SocketIO sends a 'message' event to all clients.
    # broadcast=True ensures the message is sent to every client, not just the sender.
    send(msg, broadcast=True)

# Main entry point for the application
if __name__ == '__main__':
    # Run the app with SocketIO support.
    # host='0.0.0.0' makes the server accessible from other devices on your network.
    # debug=True enables auto-reloading when you save changes.
    print("Starting Flask server with SocketIO on http://127.0.0.1:5000")
    socketio.run(app, host='0.0.0.0', port=5000, debug=True)