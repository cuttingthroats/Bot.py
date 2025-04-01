import requests
import json
from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()

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
