from openai import OpenAI

# Create client
client = OpenAI(api_key="YOUR_API_KEY_HERE")

# Store conversation history
messages = []

def completion(user_message):
    global messages

    # Add user message
    messages.append({
        "role": "user",
        "content": user_message
    })

    # Create chat completion
    chat_completion = client.chat.completions.create(
        model="gpt-4o-mini",   # you can change model if needed
        messages=messages
    )

    # Get assistant reply
    assistant_message = chat_completion.choices[0].message.content

    # Add assistant message to history
    messages.append({
        "role": "assistant",
        "content": assistant_message
    })

    print("Jarvis:", assistant_message)


# Chat starts here
print("Jarvis: Hi, I am Jarvis. How may I help you?")

while True:
    user_question = input("User: ")

    if user_question.lower() in ["exit", "quit", "bye"]:
        print("Jarvis: Goodbye!")
        break

    completion(user_question)