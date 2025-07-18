import os
import openai
from dotenv import load_dotenv

load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")

def explain_code(code_snippet):
    prompt = f"""You are an expert developer. Explain the following code in simple, clear language:\n\n{code_snippet}\n\nExplanation:"""

    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[{"role": "user", "content": prompt}],
        temperature=0.5
    )

    return response.choices[0].message["content"].strip()
