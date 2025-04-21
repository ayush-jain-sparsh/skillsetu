import json
def clean_json(output):
    cleaned_json_string = output.replace("```json", "").replace("```", "").strip()
    #cleaned_json_string = cleaned_json_string.replace("\n","<br>")
    json_data = json.loads(cleaned_json_string)
    return json_data
