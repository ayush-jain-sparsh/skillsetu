from flask import Blueprint

calendar_bp = Blueprint('calendar', __name__)

@calendar_bp.route('/sync', methods=['POST'])
def sync_calendar():
    return {"message": "Google Calendar sync coming soon!"}