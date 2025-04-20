from flask import Blueprint, request, jsonify 
from LangChain.services.delete_user import delete_user

refresh_bp = Blueprint('refresh_bp', __name__)

@refresh_bp.route('/app/refresh', methods=['GET' , 'POST'])
def refresh():
    if request.method == 'GET':
        return "To access SkillSetu API, please use the POST method."
    elif request.method == 'POST':
        data = request.get_json()
        if not data:
            return jsonify({"error": "No input data provided"}), 400
        
        user_id = data.get("user_id")
        if not user_id:
            return jsonify({"error": "No user_id provided"}), 400
        
        try :
            delete_user(user_id)
            response = {"message": "Memory refreshed successfully"}
            return jsonify(response), 200
        except Exception as e:
            return jsonify({"error": str(e)}), 500