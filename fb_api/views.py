import json
from django.utils.decorators import method_decorator, classonlymethod
from django.views.decorators.csrf import csrf_exempt

from django.http import HttpResponse
from django.views import generic
from .models.models import Message
from datetime import datetime
from django.utils.timezone import make_aware
import requests


class SomeView(generic.View):

    def get(self, request):
        if self.request.GET["hub.verify_token"] == "mraA3R3JDTOj8nXXoY8a9D8rPFo1SmWI":
            return HttpResponse(self.request.GET["hub.challenge"])
        else:
            return HttpResponse("Invalid token")

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return generic.View.dispatch(self, request, *args, **kwargs)

    def post(self, request):
        data = json.loads(request.body.decode('utf-8'))
        message_data = data["entry"][0]["messaging"][0]

        sender_id = message_data["sender"]["id"]
        timestamp = message_data["timestamp"]
        model_date = make_aware(datetime.fromtimestamp(timestamp/1000))

        message_id = message_data["message"]["mid"]
        message_itself = message_data["message"]["text"]
        author=get_author(message_id)

        data = {
            "recipient": { "id": sender_id },
            "message": {
                "text": "Your issue has been taken for consideration."
            }
        }

        headers = {'Content-type': 'application/json'}
        r = requests.post('https://graph.facebook.com/v8.0/me/messages?access_token=EAAD1ZBiA2cHkBAFNZC7ZBCfi0Ko06jBVvqWf6ET9XuVr2rKvRiYym0ELDfVb6QfLPdDDooUMLlCZCTqPWdhp0MupMhnGnxzWg0FQsyk0lB55uyacCrVB50TACvfaMJWAc7lpBy6quUQO9vIoqAenvL15Bd0nPouEg9hbkItJLpXfEczTrbNg2s9VxZA5DliUZD',
                        json=data,
                        headers=headers)

        new_record = Message(message=message_itself, created_at=model_date, author=author)
        new_record.save()

        print(sender_id, timestamp, message_itself)
        return HttpResponse("OK")



