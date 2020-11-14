import facebook


def get_author(message_id):
    author = ''
    graph = facebook.GraphAPI(access_token="EAAD1ZBiA2cHkBAFNZC7ZBCfi0Ko06jBVvqWf6ET9XuVr2rKvRiYym0ELDfVb6QfLPdDDooUMLlCZCTqPWdhp0MupMhnGnxzWg0FQsyk0lB55uyacCrVB50TACvfaMJWAc7lpBy6quUQO9vIoqAenvL15Bd0nPouEg9hbkItJLpXfEczTrbNg2s9VxZA5DliUZD",
                              version="2.12")

    message = graph.get_object(id="105809648005519", fields="conversations{messages{from{name}}}")

    for conversation_data in message["conversations"]["data"]:
        for message_data in conversation_data["messages"]["data"]:
            if message_data["id"] == message_id:
                author = message_data["from"]["name"]

    return author
