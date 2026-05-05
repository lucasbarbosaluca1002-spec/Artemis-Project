from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    html = '''
<!DOCTYPE html>
<html>
<head>
    <title>Missão Artemis</title>
    <style>
        body { 
            background: #0a0a0a; 
            color: white; 
            font-family: Arial; 
            text-align: center; 
            padding: 50px;
        }
        img { max-width: 300px; margin: 20px; }
        .galeria { display: flex; flex-wrap: wrap; justify-content: center; }
        .foto { margin: 20px; }
    </style>
</head>
<body>
    <h1>🚀 MISSÃO ARTEMIS - NASA</h1>
    <img src="https://www.nasa.gov/wp-content/themes/nasa1999-child/images/artemis-logo.png" alt="Logo Artemis">
    <p>Retorno à Lua em 2026! 1ª mulher na Lua!</p>
    
    <h2>Galeria Artemis</h2>
    <div class="galeria">
        <div class="foto">
            <img src="https://images.unsplash.com/photo-1632854057158-901ae9f83d5b?w=400" alt="Lançamento">
            <p>Artemis I Lançamento</p>
        </div>
        <div class="foto">
            <img src="https://images.unsplash.com/photo-1444080233090-f3f9ca85e4a7?w=400" alt="Lua">
            <p>Destino Lunar</p>
        </div>
        <div class="foto">
            <img src="https://images.unsplash.com/photo-1519345182560-3f2917c472ef?w=400" alt="Astronauta">
            <p>1ª Mulher na Lua</p>
        </div>
    </div>
</body>
</html>
    '''
    return html

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
