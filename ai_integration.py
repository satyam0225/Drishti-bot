from openai import OpenAI
from dotenv import load_dotenv
import os
load_dotenv("key.env")

api_key=os.getenv("OPENAI_API_KEY")


def ai_setup(api_key):
    global client
    client= OpenAI(api_key=api_key)


def get_answerfrom_model(prompt,model="gpt-3.5-turbo"):
    messages = [{"role": "user", "content": prompt}]
    response = client.chat.completions.create(
        model=model,
        messages=messages,
        temperature=0, # this is the degree of randomness of the model's output
    )
    return  response.choices[0].message.content

ai_setup(api_key)
r=get_answerfrom_model(prompt="how are you  ")
print(r)