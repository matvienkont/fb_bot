from ...models.models import Message


def get_issues_by_userid(uid):
    messages = Message.objects.filter(author_id=uid).values()
    return messages
