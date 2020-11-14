from ...models.models import Message


def save_message(message_itself, model_date, sender_id, author):
    new_record = Message(message=message_itself, created_at=model_date, author_id=sender_id, author=author)
    new_record.save()