import os
from flask import Flask

app = Flask(__name__, static_folder='static', template_folder='templates')

@app.route('/')
def home():
    try:
        return """
        <h1>🚀 MISSÃO ARTEMIS ONLINE! 🥳</h1>
        <p>Flask rodando perfeitamente na Azure!</p>
        <img src="/static/logo-artemis.png" alt="Logo" style="max-width:300px;">
        """
    except Exception as e:
        return f"Erro: {str(e)}", 500

@app.errorhandler(404)
def not_found(e):
    return home()

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port, debug=False)
