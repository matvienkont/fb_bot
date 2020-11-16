import facebook
import os

def get_author(message_id):
    author = ''
    ACCESS_TOKEN = os.environ['ACCESS_TOKEN']
    APP_ID = os.environ['APP_ID']

    graph = facebook.GraphAPI(access_token=ACCESS_TOKEN,
                              version="2.12")

    message = graph.get_object(id=APP_ID, fields="conversations{messages{from{name}}}")

    for conversation_data in message["conversations"]["data"]:
        for message_data in conversation_data["messages"]["data"]:
            if message_data["id"] == message_id:
                author = message_data["from"]["name"]

    return author
