import os
import openai
from dotenv import load_dotenv

load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")

def analyze_logs(log_text):
    prompt = f"""You are a log analysis expert. Analyze the following logs and provide:
- A summary of what is happening
- Any errors or warnings found
- Possible root cause(s)
- Suggestions to fix or investigate further

Logs:
{log_text}

Your analysis:"""

    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[{"role": "user", "content": prompt}],
        temperature=0.3
    )

    return response.choices[0].message["content"].strip()
