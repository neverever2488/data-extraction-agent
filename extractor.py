import os
import json
from groq import Groq
from dotenv import load_dotenv

load_dotenv()

client = Groq(api_key=os.getenv("GROQ_API_KEY"))

def extract_data(text: str, fields: list[str]) -> dict:
    fields_str = ", ".join(fields)
    
    response = client.chat.completions.create(
        model="llama-3.1-8b-instant",
        messages=[
            {
                "role": "system",
                "content": (
                    "You are a data extraction assistant. "
                    "Extract the requested fields from the provided text. "
                    "Respond ONLY with a valid JSON object. "
                    "If a field is not found, use null as the value. "
                    "Do not include any explanation or markdown."
                )
            },
            {
                "role": "user",
                "content": f"Extract these fields: {fields_str}\n\nText:\n{text[:3000]}"
            }
        ]
    )
    
    raw = response.choices[0].message.content.strip()
    
    try:
        clean = raw.replace("```json", "").replace("```", "").strip()
        # Handle multiple JSON objects
        clean = "[" + clean.replace("}\n{", "},{") + "]"
        parsed = json.loads(clean)
        if isinstance(parsed, list):
            return {"items": parsed}
        return parsed
    except json.JSONDecodeError:
        return {"error": "Failed to parse response", "raw": raw}
