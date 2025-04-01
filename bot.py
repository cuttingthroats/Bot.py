import requests
import json

# Your Discord application details
application_id = "1356755982524485755"
client_id = "RIqDm7SCFV947fThzH3i5BsriUtniOPd"

# URL to register the global slash command
url = f"https://discord.com/api/v10/applications/{application_id}/commands"

# Payload for the /flood command
payload = {
    "name": "flood",
    "description": "Flood the channel with a message",
    "type": 1,  # 1 is for a Slash Command
    "options": [
        {
            "type": 3,  # 3 is for a string (text)
            "name": "message",
            "description": "The message to flood",
            "required": True,
        },
        {
            "type": 4,  # 4 is for an integer (how many times)
            "name": "times",
            "description": "How many times to send the message",
            "required": True,
        }
    ]
}

# Register the slash command with Discord
headers = {
    "Authorization": f"Bot {bot_token}",
    "Content-Type": "application/json"
}

response = requests.post(url, headers=headers, data=json.dumps(payload))

if response.status_code == 201:
    print("Slash command registered successfully!")
else:
    print(f"Error: {response.status_code} - {response.text}")
