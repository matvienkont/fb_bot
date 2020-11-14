from django.contrib import admin
from .models.models import Message


@admin.register(Message)
class MessageAdmin(admin.ModelAdmin):
    fields = ["message", "created_at", "author", "status"]
    readonly_fields = ["message", "created_at", "author"]
    list_display = ["message", "created_at", "author", "status"]
    list_filter = ["created_at", "status"]
