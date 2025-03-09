import os
from openai import OpenAI
#GitHub Models allows rapid prototyping and dev of AI apps
#Easy to swap for production

token = os.environ["GITHUB_TOKEN"]
endpoint = "https://models.inference.ai.azure.com"
model_name = "gpt-4o"

#client allows the generation of completions to the openai model
client = OpenAI(
    base_url=endpoint,
    api_key=token,
)
#characterizing the nature of the assistant
response = client.chat.completions.create(
    messages=[
        {
            "role": "system",
            "content": "You are a helpful assistant who speaks in rhyme.",
        },
        {
            "role": "user",
            "content": "Who was Alexander Hamilton?",
        }
    ],
    model=model_name,
    temperature=1.0, #parameter that expermients with predictions
    max_tokens=1000,
    top_p=1.0
)

print(response.choices[0].message.content)