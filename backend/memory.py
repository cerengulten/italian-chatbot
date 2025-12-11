
conversation_memory = []

def add_message(user, bot):
  conversation_memory.append({"user": user, "bot": bot})

  if len(conversation_memory) > 5:
    conversation_memory.pop(0)


def get_memory_text():
  '''
  Combines past messages into a single string to provide context.
  '''

  history = ""
  for m in conversation_memory:
    history += f"User: {m['user']}\nBot: {m['bot']}\n"
  return history