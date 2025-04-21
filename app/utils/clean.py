import json
def clean_json(output):
    cleaned_json_string = output.replace("```json", "").replace("```", "").strip()

    json_data = json.loads(cleaned_json_string)
    return json_data