import requests
import json

# Your application ID and public key from Discord Developer Portal
application_id = "1356755982524485755"
public_key = "f5029ae363369ac1a08695ef4aff4753fa87f24ca2c0a8ba3a4bd57637081d30"

# Set your bot's command endpoint URL for global registration
url = f"https://discord.com/api/v10/applications/1356755982524485755/commands"

# Create the command payload
payload = {
    "name": "flood",
    "description": "Flood the channel with a message",
    "type": 1,  # 1 is for a Slash Command
    "options": [
        {
            "type": 3,  # 3 is for a string option (text)
            "name": "message",
            "description": "The message to flood",
            "required": True,
        },
        {
            "type": 4,  # 4 is for an integer option
            "name": "times",
            "description": "How many times to send the message",
            "required": True,
        }
    ]
}

# Make the POST request to register the command globally
headers = {
    "Authorization": f"Bot {bot_token}",
    "Content-Type": "application/json"
}

response = requests.post(url, headers=headers, data=json.dumps(payload))

if response.status_code == 201:
    print("Slash Command registered successfully!")
else:
    print(f"Error: {response.status_code} - {response.text}")
