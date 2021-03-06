from .models import Conversation

def conversationsOfUser(request):
    if not request.user.is_authenticated():
        return {}
    unread_conversation_count = 0
    conversations = list(Conversation.objects.conversations_of(request.user))

    for conv in conversations:

        if conv.latest_message() is None:
            continue

        if conv.latest_message().sender == request.user:
            continue

        if conv.latest_message().read_by.count() > 0:
            msg_read_by = list(conv.latest_message().read_by.all())
            if not request.user in msg_read_by:
                unread_conversation_count += 1
        else:
            unread_conversation_count += 1

    return {
        'recent_conversations': conversations[:5],
        'unread_conversation_count': unread_conversation_count,
        'conversation_count': len(conversations),
    }
