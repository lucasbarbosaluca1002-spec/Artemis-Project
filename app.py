import os
from flask import Flask

app = Flask(__name__)

@app.route("/")
def artemis():
    return """
<!DOCTYPE html>
<html lang="pt-BR">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Missão Artemis - NASA</title>
    <style>
        *{margin:0;padding:0;box-sizing:border-box;}
        body{font-family:Arial,sans-serif;background:linear-gradient(135deg,#0c0c0c 0%,#1a1a2e 50%,#16213e 100%);color:#fff;min-height:100vh;}
        .container{max-width:1200px;margin:0 auto;padding:20px;}
        header{text-align:center;padding:40px 0;background:rgba(255,255,255,0.1);backdrop-filter:blur(10px);border-radius:20px;margin-bottom:40px;box-shadow:0 20px 40px rgba(0,0,0,0.3);}
        .logo{width:250px;height:auto;filter:drop-shadow(0 15px 30px rgba(255,255,255,0.4));margin-bottom:20px;transition:transform 0.3s ease;}
        .logo:hover{transform:scale(1.05);}
        h1{font-size:3.5em;text-shadow:3px 3px 6px rgba(0,0,0,0.7);margin-bottom:20px;background:linear-gradient(45deg,#fff,#e0e0e0);-webkit-background-clip:text;-webkit-text-fill-color:transparent;background-clip:text;}
        .mission-text{font-size:1.4em;max-width:900px;margin:0 auto;padding:0 20px;line-height:1.8;}
        .gallery{display:grid;grid-template-columns:repeat(auto-fit,minmax(320px,1fr));gap:25px;margin-top:60px;}
        .gallery-item{background:rgba(255,255,255,0.1);border-radius:20px;overflow:hidden;transition:all 0.4s ease;border:1px solid rgba(255,255,255,0.2);backdrop-filter:blur(10px);}
        .gallery-item:hover{transform:translateY(-15px) scale(1.02);box-shadow:0 30px 60px rgba(0,0,0,0.4);}
        .gallery-item img{width:100%;height:280px;object-fit:cover;}
        .gallery-caption{padding:25px;text-align:center;font-weight:bold;font-size:1.1em;}
        footer{text-align:center;margin-top:80px;padding:30px;color:#aaa;font-size:0.9em;}
    </style>
</head>
<body>
<div class="container">
    <header>
        <img src="https://www.nasa.gov/sites/default/files/thumbnails/image/artemis_program_logo.jpg" alt="Logotipo Artemis NASA" class="logo">
        <h1>🚀 MISSÃO ARTEMIS</h1>
        <p class="mission-text">
            <strong>Artemis</strong> retorna humanos à Lua! <strong>Artemis I (2022):</strong> órbita OK. 
            <strong>Artemis II (2025):</strong> tripulação. <strong>Artemis III (2026):</strong> 
            1ª mulher + próximo homem na Lua! Mars em breve!
            <br><br><em>"Não voltamos à Lua. FICAMOS lá!" - NASA</em>
        </p>
    </header>
    
    <section class="gallery">
        <div class="gallery-item">
            <img src="https://images.unsplash.com/photo-1632854057158-901ae9f83d5b?w=800&auto=format&fit=crop" alt="Lançamento SLS">
            <div class="gallery-caption">🛫 Artemis I - Space Launch System</div>
        </div>
        <div class="gallery-item">
            <img src="https://images.unsplash.com/photo-1444080748397-f442aa95c9e5?w=800&auto=format&fit=crop" alt="Orion">
            <div class="gallery-caption">🌌 Nave Orion - Órbita Lunar</div>
        </div>
        <div class="gallery-item">
            <img src="https://images.unsplash.com/photo-1444080233090-f3f9ca85e4a7?w=800&auto=format&fit=crop" alt="Lua">
            <div class="gallery-caption">🌕 Destino: Superfície Lunar</div>
        </div>
        <div class="gallery-item">
            <img src="https://images.unsplash.com/photo-1519345182560-3f2917c472ef?w=800&auto=format&fit=crop" alt="Astronauta">
            <div class="gallery-caption">👩‍🚀 1ª Mulher na Lua - Artemis III</div>
        </div>
        <div class="gallery-item">
            <img src="https://images.unsplash.com/photo-1578662996442-48f60103fc96?w=800&auto=format&fit=crop" alt="Rocket">
            <div class="gallery-caption">🚀 SLS - 98m de Potência</div>
        </div>
    </section>
    
    <footer>
        <p>© 2024 NASA Artemis | Desenvolvido com ❤️ | Flask + Azure + GitHub</p>
    </footer>
</div>
</body>
</html>
    """

if __name__ == "__main__":
    port = 5000
    if 'PORT' in os.environ:
        port = int(os.environ['PORT'])
    app.run(host='0.0.0.0', port=port)
