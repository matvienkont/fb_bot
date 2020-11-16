import requests
import os

def respond_message(sender_id, message_text):
    data = {
        "recipient": { "id": sender_id },
        "message": {
            "text": message_text
            }
    }

    headers = {'Content-type': 'application/json'}

    ACCESS_TOKEN = os.environ['ACCESS_TOKEN']
    r = requests.post(
        f'https://graph.facebook.com/v8.0/me/messages?access_token={ACCESS_TOKEN}',
        json=data,
        headers=headers)