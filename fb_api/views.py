import json
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt

from django.http import HttpResponse
from django.views import generic


from .controllers.db_interactions.save_message import save_message
from .controllers.fb_api_interactions.respond_message import respond_message
from .controllers.msg_processing.process_msg import process_msg


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

        process_msg(message_data)

        return HttpResponse("OK")
