# Import the Flask library
from flask import Flask, request

# Initialize a new Flask application
app = Flask(__name__)

# Define a route to handle GroupMe's callback
@app.route('/groupme-callback', methods=['GET'])
def groupme_callback():
    # The code parameter is what GroupMe will send after successful OAuth authorization
    # This is a simplified example; in a real-world application, you would validate this code
    auth_code = request.args.get('code')
    
    # Log the code for now; you'd typically use this code to request an access token
    print(f"Received authorization code: {auth_code}")
    
    # Respond to GroupMe to acknowledge receipt of the code
    return "Callback received", 200

# Run the server
if __name__ == '__main__':
    app.run(port=5000)
