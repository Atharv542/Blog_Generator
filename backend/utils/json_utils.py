import re
import json

def clean_json(response: str):
    # Remove markdown blocks
    response = re.sub(r"```json|```", "", response)

    # Extract JSON only
    match = re.search(r"\{.*\}", response, re.DOTALL)
    if match:
        return match.group(0)

    return response


def safe_parse_json(response: str, fallback: dict):
    try:
        cleaned = clean_json(response)
        return json.loads(cleaned)
    except Exception as e:
        print("❌ JSON PARSE ERROR:\n", response)
        return fallback