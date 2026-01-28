client = OpenAI(api_key="YOUR_API_KEY")


from openai import OpenAI

# Create client with your API key
client = OpenAI(api_key="YOUR_API_KEY")

# Send a request to the model
response = client.chat.completions.create(
    model="gpt-4o",
    messages=[
        {
            "role": "user",
            "content": "Say this is a test"
        }
    ],
    temperature=1,
    max_tokens=2048,
    top_p=1,
    frequency_penalty=0,
    presence_penalty=0
)

# Print the response
print(response.choices[0].message.content)