import requests
import json
from dotenv import load_dotenv
import os
from flask import Flask, request, jsonify
import gunicorn
# Load environment variables from .env file

# Access the environment variable
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

app = Flask(__name__)

@app.route('/interactions', methods=['POST'])
def interactions():
    data = request.json
    
    if data['type'] == 1:  # Discord's verification ping
        return jsonify({'type': 1})  
    
    if data['type'] == 2:  # Slash command execution
        command_name = data['data']['name']
        
        if command_name == "flood":
            message = data['data']['options'][0]['value']
            times = int(data['data']['options'][1]['value'])

            return jsonify({
                "type": 4,  # Respond in-channel
                "data": {
                    "content": "\n".join([message] * times)  # Repeat message
                }
            })
    
    return jsonify({"error": "Invalid request"}), 400

if __name__ == '__main__':
    app.run(port=5000)

