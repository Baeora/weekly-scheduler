from openai import OpenAI
import json

import dotenv
dotenv.load_dotenv()

import os

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def get_response(prompt):
    
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[{"role": "user", "content": prompt}],
        max_tokens=16000
    )

    return response.choices[0].message.content.strip()

def write_local_file(content, filename):
    with open(filename, 'w', encoding='utf-8') as f:
        json.dump(content, f, ensure_ascii=False, indent=4)

def upload_to_knowledge(filename):
    # Set up OpenAI client with your API key
    client = OpenAI(
        # This is the default and can be omitted
        api_key=os.environ.get("OPENAI_API_KEY"),
    )

    # Upload the file
    with open(filename, 'rb') as file:
        response = client.files.create(
            file=file,
            purpose='assistants'
        )
    return response