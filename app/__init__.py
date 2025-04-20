from flask import Flask

def create_app():
    app = Flask(__name__)

    from .routes.roadmap import roadmap_bp
    from .routes.calendar import calendar_bp
    from .routes.mentor import mentor_bp
    from .routes.transcription import transcription_bp

    app.register_blueprint(roadmap_bp, url_prefix='/roadmap')
    app.register_blueprint(calendar_bp, url_prefix='/calendar')
    app.register_blueprint(mentor_bp, url_prefix='/mentor')
    app.register_blueprint(transcription_bp, url_prefix='/transcription')

    return app
