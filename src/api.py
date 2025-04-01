
#pip install openai
#pip install python-dotenv

# did $5 in API credits
from openai import OpenAI
from dotenv import load_dotenv
import os

load_dotenv()
openai_api_key = os.getenv("MY_API_KEY")

client = OpenAI(api_key=openai_api_key)

def analyze_code_snippet(code_snippet: str):
    completion = client.chat.completions.create(
    model="gpt-4o-mini",
    max_completion_tokens=150,
    n=1,
    #reasoning_effort="medium", #the default, could be low or high
    # response_format= "text", #the default, could be json stuffs
    store= False, # not sure if you want to store or not, default false
    temperature=0.5, #takes in 0-2, Higher values like 0.8 will make the output more random, while lower values like 0.2 will make it more focused and deterministic, default 1
    messages=[
            {
                "role": "system",
                "content": "You are a cybersecurity specialist helping a junior developer debug their code for cryptographic API misuses in Python."
            },
            {
                "role": "user",
                "content": f"Here is the code snippet:\n```python\n{code_snippet}\n```"
            }
        ]
    )

    return completion.choices[0].message.content

# Example usage

with open('./test_files/Rule0/HasVuln/testfile550.py', 'r') as file:
    code_snippet = file.read()
    print(analyze_code_snippet(code_snippet))



