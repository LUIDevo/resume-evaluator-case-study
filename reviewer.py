from anthropic import Anthropic

client = Anthropic()

with open("resume_evaluation_system_prompt.txt", "read") as file:
    system_prompt=file.read()

# Create a message request
message = client.messages.create(
    model="claude-sonnet-5",  # Chosen model, ideal for efficiency and intelligence
    max_tokens=1024,
    temperature=0,
    system=system_prompt,
    messages=[
        {"role": "user", "content": ""}
    ]
)
