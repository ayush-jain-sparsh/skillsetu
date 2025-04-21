from flask import Blueprint, request, jsonify 
from app.services.subtopic_service import generate
from app.utils.clean import clean_json

subtopic_bp = Blueprint('subtopic_bp', __name__)

@subtopic_bp.route('/app/subtopic', methods=['GET' , 'POST'])
def roadmap():
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
            response = clean_json(response)
            response= {'response' : response}
            return jsonify(response), 200
        except Exception as e:
            return jsonify({"error": str(e)}), 500