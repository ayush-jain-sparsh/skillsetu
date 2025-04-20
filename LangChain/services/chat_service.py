from google.genai import types
from LangChain.prompts import chatbot
from app.utils import gemini
from LangChain.utils import get_token
from LangChain.services.get_history import get_history
from LangChain.services.add_user import add_user
from LangChain.services.update_history import update_history

def generate(user_id , prompt):
    client = gemini.client

    history = get_history(user_id)
    if history is None:
        add_user(user_id)
        history = get_history(user_id)

    text = chatbot.get_chat()+""" history : """ + history + """ subtopic : """+prompt
    token = get_token.approx_token_count(text)
    if token > 1000000:
        return '{"error": "Token limit exceeded"}'
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
    
    history = history + "\n" + output['summary']
    update_history(user_id , history)
    return output
