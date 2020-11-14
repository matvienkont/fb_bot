from django.contrib import admin
from .models.models import Message

@admin.register(Message)
class MessageAdmin(admin.ModelAdmin):
    fields = ["message", "created_at", "author"]
    readonly_fields = ["message", "created_at", "author"]
    list_display = ["message", "created_at", "author"]
    list_filter = ["created_at"]
