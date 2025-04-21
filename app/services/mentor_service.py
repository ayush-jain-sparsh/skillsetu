from google.genai import types
from app.prompts import mentor
from app.utils import gemini

def generate(task , subtopic):
    client = gemini.client

    text = mentor.get_mentor()+" Task : " + task + " subtopic : "+subtopic
    
    model = gemini.model
    contents = [
        types.Content(
            role="user",
            parts=[
                types.Part.from_text(text=text),
            ],
        ),
    ]
    generate_content_config = types.GenerateContentConfig(
        response_mime_type="text/plain",
    )


    output = ""
    for chunk in client.models.generate_content_stream(
        model=model,
        contents=contents,
        config=generate_content_config,
    ): 
        if isinstance(chunk.text, str):
            output = output + chunk.text
        else:
            raise ValueError("chunk.text is not a string!")

    return output