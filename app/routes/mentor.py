from flask import Blueprint, request, jsonify 
from app.services.mentor_service import generate

mentor_bp = Blueprint('mentor_bp', __name__)

@mentor_bp.route('/app/mentor', methods=['GET' , 'POST'])
def mentor():
    if request.method == 'GET':
        return "To access SkillSetu API, please use the POST method."
    elif request.method == 'POST':
        data = request.get_json()
        if not data:
            return jsonify({"error": "No input data provided"}), 400
        
        task = data.get("task")
        subtopic = data.get("subtopic")
        if not task:
            return jsonify({"error": "No task provided"}), 400
        if not subtopic:
            return jsonify({"error": "No subtopic provided"}), 400
        
        try : 
            response = generate(task, subtopic)
            response = {'response' : response}
            response['response'] = response['response'].replace("\n", "<br>")
            return jsonify(response), 200
        except Exception as e:
            return jsonify({"error": str(e)}), 500