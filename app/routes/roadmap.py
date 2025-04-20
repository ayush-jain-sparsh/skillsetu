from flask import Blueprint, request, jsonify 
from app.services.roadmap_service import generate
from app.utils.clean import clean_json

roadmap_bp = Blueprint('roadmap_bp', __name__)

@roadmap_bp.route('/app/roadmap', methods=['GET' , 'POST'])
def roadmap():
    if request.method == 'GET':
        return "To access SkillSetu API, please use the POST method."
    elif request.method == 'POST':
        data = request.get_json()
        if not data:
            return jsonify({"error": "No input data provided"}), 400
        
        task = data.get("task")
        duration = data.get("duration")
        if not task:
            return jsonify({"error": "No task provided"}), 400
        if not duration:
            return jsonify({"error": "No duration provided"}), 400
        
        try : 
            response = generate(task, duration)
            response = clean_json(response)
            return jsonify(response), 200
        except Exception as e:
            return jsonify({"error": str(e)}), 500