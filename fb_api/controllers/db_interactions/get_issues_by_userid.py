from ...models.models import Message


def get_issues_by_userid(uid):
    messages = Message.objects.filter(author_id=uid).values()
    return messages

def get_issues_by_uid_and_status(uid, status):
    messages = Message.objects.filter(author_id=uid, status=status).values()
    return messages
