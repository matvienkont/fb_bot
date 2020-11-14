import re
import json

from ..db_interactions.get_issues_by_userid import get_issues_by_userid
from ..fb_api_interactions.respond_message import respond_message
from ..db_interactions.save_message import save_message

from datetime import datetime
from django.utils.timezone import make_aware

from ..fb_api_interactions.get_author import get_author


def process_msg(message_data):
    sender_id = message_data["sender"]["id"]
    timestamp = message_data["timestamp"]
    model_date = make_aware(datetime.fromtimestamp(timestamp / 1000))

    message_id = message_data["message"]["mid"]
    message_itself = message_data["message"]["text"]
    author = get_author(message_id)

    KEYWORDS_REGEX = r'^(\/new\s+)|(\/all*)|(\/help*)|(\/examples*)'
    match = re.match(KEYWORDS_REGEX, message_itself)

    if match:
        command = match.group()
        if 'new' in command:

            message_itself = re.split(r'[ \n]', message_itself, 1)
            print(message_itself)
            save_message(message_itself[1], model_date, sender_id, author)
            respond_message(sender_id, "New")
        elif 'all' in command:
            results = get_issues_by_userid(sender_id)
            print(results)
            response = ''
            i = 1
            for message in results:
                response += f"№{str(i)} Message:```\n{message['message']}\n```\n\n\n"
                i += 1
            respond_message(sender_id, response)
        elif 'help' in command:
            HELP_RESPONSE = f"Available commands:\n ```\n/new\n```\n - report issue \n ```\n/all\n```\n - get all your reports\n \n ```\n/help\n```\n - to get command list\n \n```\n/examples\n```\n - get usage examples"
            respond_message(sender_id, HELP_RESPONSE)
        elif 'examples' in command:
            HELP_RESPONSE = f"Example messages:\n\n```\n/new I would like to say that ...\n```\nOR```\n/new \nI would like to say that ...\n```\n \n```\n/all\n```"
            respond_message(sender_id, HELP_RESPONSE)
    else:
        COMMAND_NOT_FOUND = f"Couldn't find your command, type \n```\n/help\n```\n to get all available commands"
        respond_message(sender_id, COMMAND_NOT_FOUND)
