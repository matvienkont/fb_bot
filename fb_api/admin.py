from django.contrib import admin
from django import forms
from .models.models import Message
from .controllers.fb_api_interactions.respond_message import respond_message


class ResponseForm(forms.ModelForm):
    response_message = forms.CharField(widget=forms.Textarea)

    def processData(self, input, author_id, previous_response_message, user_message):
        if input and (previous_response_message != input):
            FINAL_MESSAGE_RESPONSE = f"```\n{user_message}\n```\n\n{input}"
            respond_message(author_id, FINAL_MESSAGE_RESPONSE)


    def save(self, commit=True):
        response_message = self.cleaned_data.get('response_message', None)

        instance = super(ResponseForm, self).save(commit=commit)

        get_author_id = instance.author_id

        message_info = Message.objects.filter(message_id=instance.message_id).values()[0]
        get_previous_response_message = message_info["response_message"]
        user_message = message_info["message"]


        if commit:
            instance.save()

        instance.description = self.processData(response_message, get_author_id, get_previous_response_message, user_message)

        return instance

    class Meta:
        model = Message
        fields = "__all__"


class MessageAdmin(admin.ModelAdmin):
    fields = ["message", "created_at", "author", "status", "response_message"]
    readonly_fields = ["message", "created_at", "author"]
    list_display = ["message", "created_at", "author", "status"]
    list_filter = ["created_at", "status"]


    form = ResponseForm

admin.site.register(Message, MessageAdmin)

