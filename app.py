import os
from flask import Flask

app = Flask(__name__)

@app.route("/")
def artemis2():
    return """
<!DOCTYPE html>
<html lang="pt-BR">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Artemis II - Primeira Missão Tripulada à Lua</title>
    <style>
        *{margin:0;padding:0;box-sizing:border-box;}
        body{
            font-family:'Segoe UI',Arial,sans-serif;
            background:linear-gradient(135deg,#000428 0%,#004e92 50%,#000428 100%);
            color:#fff;
            overflow-x:hidden;
        }
        .stars{position:fixed;top:0;left:0;width:100%;height:100%;pointer-events:none;z-index:-1;}
        .star{position:absolute;background:#fff;border-radius:50%;animation:twinkle 2s infinite;}
        @keyframes twinkle{0%,100%{opacity:0.3;}50%{opacity:1;}}
        
        .container{max-width:1300px;margin:0 auto;padding:20px;}
        header{
            text-align:center;
            padding:60px 20px;
            background:linear-gradient(145deg,rgba(255,255,255,0.1),rgba(255,255,255,0.05));
            backdrop-filter:blur(20px);
            border-radius:30px;
            margin:20px 0;
            box-shadow:0 25px 50px rgba(0,0,0,0.5);
            border:1px solid rgba(255,255,255,0.1);
        }
        .logo{max-width:280px;height:auto;filter:drop-shadow(0 20px 40px rgba(255,215,0,0.5));margin-bottom:30px;animation:pulse 3s infinite;}
        @keyframes pulse{0%,100%{transform:scale(1);}50%{transform:scale(1.05);}}
        
        h1{
            font-size:clamp(2.5em,8vw,5em);
            background:linear-gradient(45deg,#ffd700,#fff,#ffd700);
            -webkit-background-clip:text;
            background-clip:text;
            -webkit-text-fill-color:transparent;
            margin-bottom:25px;
            text-shadow:0 0 30px rgba(255,215,0,0.5);
        }
        .info{
            font-size:1.3em;
            line-height:1.7;
            max-width:900px;
            margin:0 auto 40px;
            text-align:center;
            background:rgba(255,255,255,0.05);
            padding:30px;
            border-radius:20px;
            border-left:4px solid #ffd700;
        }
        .gallery{
            display:grid;
            grid-template-columns:repeat(auto-fit,minmax(350px,1fr));
            gap:30px;
            margin:50px 0;
        }
        .card{
            background:linear-gradient(145deg,rgba(255,255,255,0.15),rgba(255,255,255,0.05));
            border-radius:25px;
            overflow:hidden;
            transition:all 0.5s ease;
            border:1px solid rgba(255,255,255,0.2);
            backdrop-filter:blur(15px);
        }
        .card:hover{
            transform:translateY(-20px) scale(1.02);
            box-shadow:0 40px 80px rgba(255,215,0,0.3);
            border-color:#ffd700;
        }
        .card img{width:100%;height:300px;object-fit:cover;}
        .card-content{padding:30px;text-align:center;}
        .card h3{font-size:1.4em;margin-bottom:15px;color:#ffd700;}
        .card p{line-height:1.6;color:#ddd;}
        
        .footer{
            text-align:center;
            padding:50px 20px;
            background:rgba(0,0,0,0.5);
            margin-top:80px;
            border-radius:20px;
            font-size:1.1em;
        }
        @media(max-width:768px){.gallery{grid-template-columns:1fr;}}
    </style>
</head>
<body>
    <div class="stars" id="stars"></div>
    
    <div class="container">
        <header>
            <img src="https://www.nasa.gov/wp-content/uploads/2023/11/artemis-ii-logo.jpg" 
                 alt="Logo Artemis II NASA" 
                 class="logo"
                 onerror="this.src='https://via.placeholder.com/280x200/004e92/ffffff?text=ARTEMIS+II'">
            <h1>ARTEMIS II</h1>
            <div class="info">
                <strong>SUCESSO HISTÓRICO!</strong><br>
                Primeira missão tripulada ao redor da Lua desde 1972.<br>
                Lançada em <strong>1º de abril de 2026</strong>. Quatro astronautas a bordo da <strong>Orion</strong> com o foguete <strong>SLS</strong>.<br>
                <strong>Christina Koch</strong> — a primeira mulher em voo lunar — e <strong>Jeremy Hansen</strong> — o primeiro canadense.
            </div>
        </header>

        <section class="gallery">
            <div class="card">
                <img src="https://www.nasa.gov/wp-content/uploads/2023/11/artemis-ii-crew-1.jpg" 
                     alt="Tripulação Artemis II"
                     onerror="this.src='https://images.unsplash.com/photo-1507003211169-0a1dd7228f2d?w=800'">
                <div class="card-content">
                    <h3>👨‍🚀👩‍🚀 Tripulação</h3>
                    <p><strong>Reid Wiseman (Comandante)</strong> • <strong>Victor Glover (Piloto)</strong><br>
                    <strong>Christina Koch (Especialista)</strong> • <strong>Jeremy Hansen (Especialista)</strong><br>
                    <strong>1ª mulher e 1º canadense em voo lunar!</strong></p>
                </div>
            </div>

            <div class="card">
                <img src="https://www.nasa.gov/wp-content/uploads/2023/11/sls-artemis-i-liftoff-1.jpg" 
                     alt="Lançamento SLS"
                     onerror="this.src='https://images.unsplash.com/photo-1632854057158-901ae9f83d5b?w=800'">
                <div class="card-content">
                    <h3>🚀 Space Launch System</h3>
                    <p>Foguete mais poderoso do mundo! 98 metros de altura e 8,8 milhões de libras de empuxo.</p>
                </div>
            </div>

            <div class="card">
                <img src="https://www.nasa.gov/wp-content/uploads/2023/11/orion-lunar-flyby-1.jpg" 
                     alt="Orion na Lua"
                     onerror="this.src='https://images.unsplash.com/photo-1444080233090-f3f9ca85e4a7?w=800'">
                <div class="card-content">
                    <h3>🌌 Nave Orion</h3>
                    <p>Cápsula para 4 astronautas. Missão de ~10 dias com flyby lunar histórico.</p>
                </div>
            </div>

            <div class="card">
                <img src="https://www.nasa.gov/wp-content/uploads/2023/11/artemis-ii-mission-1.jpg" 
                     alt="Trajetória Artemis II"
                     onerror="this.src='https://images.unsplash.com/photo-1451187580459-43490279c0fa?w=800'">
                <div class="card-content">
                    <h3>🛰️ Trajetória</h3>
                    <p>~1,3 milhão de km. Lançamento do Kennedy Space Center → Flyby da Lua → Retorno com sucesso!</p>
                </div>
            </div>

            <div class="card">
                <img src="https://www.nasa.gov/wp-content/uploads/2023/11/artemis-ii-art-1.jpg" 
                     alt="Arte Artemis II"
                     onerror="this.src='https://images.unsplash.com/photo-1506905925346-21bda4d32df4?w=800'">
                <div class="card-content">
                    <h3>🎯 Objetivos Cumpridos</h3>
                    <p>✅ Teste da Orion + SLS com tripulação<br>
                    ✅ 1ª mulher e 1º canadense em voo lunar<br>
                    ✅ Preparação para Artemis III (pouso lunar)</p>
                </div>
            </div>
        </section>

        <footer class="footer">
            <p>🌟 <strong>Artemis II</strong> - Sucesso da nova era lunar | NASA 2026</p>
            <p>Desenvolvido com ❤️ | Flask</p>
        </footer>
    </div>

    <script>
        // Estrelas animadas
        for(let i=0; i<150; i++){
            let star = document.createElement('div');
            star.className = 'star';
            star.style.left = Math.random()*100 + 'vw';
            star.style.top = Math.random()*100 + 'vh';
            star.style.width = 1.5 + Math.random()*3.5 + 'px';
            star.style.height = star.style.width;
            star.style.animationDelay = Math.random()*2 + 's';
            document.getElementById('stars').appendChild(star);
        }
    </script>
</body>
</html>
    """

if __name__ == "__main__":
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port, debug=True)
