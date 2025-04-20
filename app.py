from flask import Flask 
from flask_cors import CORS
from app.routes.roadmap import roadmap_bp
from app.routes.subtopic import subtopic_bp
from app.routes.mentor import mentor_bp
from LangChain.routes.chatbot import chat_bp
from LangChain.routes.refresh_memory import refresh_bp

app = Flask(__name__)
CORS(app)

app.register_blueprint(roadmap_bp)
app.register_blueprint(subtopic_bp)
app.register_blueprint(mentor_bp)
app.register_blueprint(chat_bp)
app.register_blueprint(refresh_bp)

@app.route('/')
def index():
    return "Welcome to the SkillSetu! to access our service click on the link -> "

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000,debug=True)
