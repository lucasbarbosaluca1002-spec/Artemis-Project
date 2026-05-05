import os

from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello():
    return """
<h1 style='color:white;background:black;padding:50px;text-align:center;font-family:Arial;font-size:3em'>
🚀 MISSÃO ARTEMIS - FUNCIONANDO 100% NA AZURE! 🌕
</h1>
<p style='text-align:center;font-size:24px'>
NASA retorna à Lua 2026! 1ª mulher lunar! 
<br><br>
<img src='https://www.nasa.gov/sites/default/files/thumbnails/image/artemis_program_logo.jpg' 
     style='max-width:400px;border-radius:20px;box-shadow:0 10px 30px rgba(255,255,255,0.3)'>
<br><br>
✅ Flask + Azure + GitHub = SUCESSO!
</p>
    """.replace('\n', '')

if __name__ == "__main__":
    port = 5000
    if 'PORT' in os.environ:
        port = int(os.environ['PORT'])
    app.run(host='0.0.0.0', port=port)
