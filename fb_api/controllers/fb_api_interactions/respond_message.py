import requests

def respond_message(sender_id, message_text):
    data = {
        "recipient": { "id": sender_id },
        "message": {
            "text": message_text
            }
    }

    headers = {'Content-type': 'application/json'}
    r = requests.post(
        'https://graph.facebook.com/v8.0/me/messages?access_token=EAAD1ZBiA2cHkBAFNZC7ZBCfi0Ko06jBVvqWf6ET9XuVr2rKvRiYym0ELDfVb6QfLPdDDooUMLlCZCTqPWdhp0MupMhnGnxzWg0FQsyk0lB55uyacCrVB50TACvfaMJWAc7lpBy6quUQO9vIoqAenvL15Bd0nPouEg9hbkItJLpXfEczTrbNg2s9VxZA5DliUZD',
        json=data,
        headers=headers)