from flask import Blueprint, request, jsonify 
from LangChain.services.chat_service import generate
from app.utils.clean import clean_json

chat_bp = Blueprint('chat_bp', __name__)

@chat_bp.route('/app/chat', methods=['GET' , 'POST'])
def roadmap():
    if request.method == 'GET':
        return "To access SkillSetu API, please use the POST method."
    elif request.method == 'POST':
        data = request.get_json()
        if not data:
            return jsonify({"error": "No input data provided"}), 400
        
        user_id = data.get("user_id")
        prompt = data.get("prompt")
        if not user_id:
            return jsonify({"error": "No user_id provided"}), 400
        if not prompt:
            return jsonify({"error": "No prompt provided"}), 400
        
        try : 
            response = generate(user_id, prompt)
            return jsonify(response), 200
        except Exception as e:
            return jsonify({"error": str(e)}), 500