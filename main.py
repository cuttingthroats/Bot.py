import requests
import json
from dotenv import load_dotenv
import os
from flask import Flask, request, jsonify

# Load environment variables from .env file (for local dev)
load_dotenv()

# Fetch the bot token from the environment
bot_token = os.getenv("BOT_TOKEN")
print(f"Using bot token: {bot_token}")  # This will print the bot token to check if it's correct

# Your Discord Application ID
application_id = "1356755982524485755"  # Replace with your actual Application ID

# URL to register the global slash command
url = f"https://discord.com/api/v10/applications/1356755982524485755/commands"

# Payload for the /flood command
payload = {
    "name": "flood",
    "description": "Flood the channel with a message",
    "type": 1,  # 1 = Slash Command
    "options": [
        {
            "type": 3,  # String input
            "name": "message",
            "description": "The message to flood",
            "required": True,
        },
        {
            "type": 4,  # Integer input
            "name": "times",
            "description": "How many times to send the message",
            "required": True,
        }
    ]
}

# Register the slash command with Discord
headers = {
    "Authorization": f"Bot {os.getenv('BOT_TOKEN')}",
    "Content-Type": "application/json"
}

response = requests.post(url, headers=headers, data=json.dumps(payload))

if response.status_code == 201:
    print("Slash command registered successfully!")
else:
    print(f"Error: {response.status_code} - {response.text}")

# Initialize Flask app
app = Flask(__name__)

@app.route('/interactions', methods=['POST'])
def interactions():
    data = request.json
    print(f"Received interaction data: {data}")  # Debug: log incoming interaction data

    # Discord verification ping response
    if data['type'] == 1:
        return jsonify({'type': 1})  # Respond with type 1 (ping response)
    
    # Slash command execution
    if data['type'] == 2:
        command_name = data['data']['name']
        print(f"Received command: {command_name}")  # Debug: log command name

        if command_name == "flood":
            message = data['data']['options'][0]['value']
            times = int(data['data']['options'][1]['value'])

            print(f"Flooding with message: {message} {times} times")  # Debug: log flooding details

            return jsonify({
                "type": 4,  # Respond in-channel
                "data": {
                    "content": "\n".join([message] * times)  # Repeat message
                }
            })
    
    # If the request is invalid, respond with an error
    return jsonify({"error": "Invalid request"}), 400

if __name__ == '__main__':
    app.run(port=5000)  # Run the Flask app on port 5000
