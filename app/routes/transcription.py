from flask import Blueprint

transcription_bp = Blueprint('transcription', __name__)

@transcription_bp.route('/upload', methods=['POST'])
def upload_video():
    return {"message": "Transcription feature coming soon!"}
