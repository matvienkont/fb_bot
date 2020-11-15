import re
import json

from ..db_interactions.get_issues_by_userid import get_issues_by_userid, get_issues_by_uid_and_status
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

    KEYWORDS_REGEX = r'^(\/new\s+)|(\/all*)|(\/help*)|(\/examples*)|(\/get*)'
    match = re.match(KEYWORDS_REGEX, message_itself)

    if match:
        sub_command = match.group()
        if 'new' in sub_command:

            message_itself = re.split(r'[ \n]', message_itself, 1)
            print(message_itself)
            save_message(message_itself[1], model_date, sender_id, author, message_id)
            NEW_REPORT_RESPONSE = f"Your report has been taken for consideration."
            respond_message(sender_id, NEW_REPORT_RESPONSE)
        elif 'all' in sub_command:
            results = get_issues_by_userid(sender_id)
            print(results)
            response = ''
            i = 1
            for message in results:
                response += f"№{str(i)} Message:```\n{message['message']}\n```\n\n\n"
                i += 1
            respond_message(sender_id, response)
        elif 'help' in sub_command:
            HELP_RESPONSE = f"Available commands:" \
                            f"\n ```\n/new\n```\n - report issue " \
                            f"\n ```\n/all\n```\n - get all your reports\n " \
                            f"\n ```\n/help\n```\n - to get command list\n " \
                            f"\n```\n/examples\n```\n - get usage examples" \
                            f"\n```\n/get (status here)\n```\n - get reports with a specific status\n" \
                            f"Available statuses: _closed_, _review_, _progress_, _completed_"
            respond_message(sender_id, HELP_RESPONSE)
        elif 'examples' in sub_command:
            HELP_RESPONSE = f"Example messages:\n\n```\n/new I would like to say that ...\n```\nOR```\n/new \nI would like to say that ...\n```\n \n```\n/all\n```"
            respond_message(sender_id, HELP_RESPONSE)
        elif 'get' in sub_command:

            STATUSES = {
                "REVIEW": 'To be reviewed',
                "PROGRESS": 'In progress',
                "COMPLETED": 'Completed',
                "CLOSED": 'Closed'
            }

            USER_INPUT_STATUS = re.split(r'[ \n]', message_itself, 2)[1].upper()
            if USER_INPUT_STATUS in STATUSES:
                results = get_issues_by_uid_and_status(sender_id, STATUSES[USER_INPUT_STATUS])

                if not results:
                    response = f"No reports with this status."
                    respond_message(sender_id, response)
                    return

                response = f"Status: {STATUSES[USER_INPUT_STATUS]}\n"
                i = 1
                for message in results:
                    response += f"№{str(i)} Message:```\n{message['message']}\n```\n\n\n"
                    i += 1
                respond_message(sender_id, response)
            else:
                response = f"Not valid status"
                respond_message(sender_id, response)



    else:
        COMMAND_NOT_FOUND = f"Couldn't find your command, type \n```\n/help\n```\n to get all available commands"
        respond_message(sender_id, COMMAND_NOT_FOUND)
