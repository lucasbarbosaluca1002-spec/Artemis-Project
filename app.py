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
            background: linear-gradient(135deg, #0a1f3d 0%, #001a3d 100%);
            color:#fff;
            overflow-x:hidden;
            min-height:100vh;
        }
        .stars{position:fixed;top:0;left:0;width:100%;height:100%;pointer-events:none;z-index:-1;}
        .star{position:absolute;background:#fff;border-radius:50%;animation:twinkle 3s infinite;}
        @keyframes twinkle{0%,100%{opacity:0.2;}50%{opacity:1;}}

        .container{max-width:1200px;margin:0 auto;padding:20px;}
        
        header{text-align:center;padding:40px 20px 20px;}
        .logo{max-width:420px;height:auto;margin-bottom:15px;filter: drop-shadow(0 0 30px #ffd700);}
        h1{
            font-size:3.8rem;
            background: linear-gradient(90deg, #ffd700, #fff, #ffd700);
            -webkit-background-clip:text;
            background-clip:text;
            -webkit-text-fill-color:transparent;
            text-shadow: 0 0 30px rgba(255,215,0,0.7);
        }
        .banner{
            background: rgba(0, 50, 120, 0.9);
            border: 2px solid #ffd700;
            border-radius: 20px;
            padding: 25px;
            margin: 30px 0;
            text-align:center;
            box-shadow: 0 10px 30px rgba(0,0,0,0.6);
        }

        .cards{
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(320px, 1fr));
            gap: 25px;
            margin: 40px 0;
        }
        .card{
            background: rgba(255,255,255,0.08);
            border-radius: 18px;
            overflow: hidden;
            transition: all 0.4s;
            border: 1px solid rgba(255,215,0,0.2);
        }
        .card:hover{transform: translateY(-15px); box-shadow: 0 25px 50px rgba(255,215,0,0.25); border-color: #ffd700;}
        .card img{width:100%; height:230px; object-fit: cover;}
        .card-content{padding: 20px; text-align: center;}
        .card h3{color: #ffd700; margin-bottom: 12px; font-size: 1.4em;}

        footer{
            text-align:center;
            padding:40px 20px;
            background: rgba(0,0,0,0.6);
            border-radius: 20px;
            margin-top: 60px;
        }
        @media(max-width:768px){.cards{grid-template-columns: 1fr;} h1{font-size:2.9rem;}}
    </style>
</head>
<body>
    <div class="stars" id="stars"></div>
    
    <div class="container">
        <header>
            <img src="https://upload.wikimedia.org/wikipedia/commons/6/60/Artemis_Logo_NASA.png" 
                 alt="Logo Oficial Artemis II" class="logo">
            <h1>ARTEMIS II</h1>
        </header>

        <div class="banner">
            <strong>PRIMEIRA MISSÃO TRIPULADA!</strong><br><br>
            Artemis II será a primeira missão humana ao redor da Lua desde 1972!<br>
            Lançamento previsto para final de 2025. Quatro astronautas farão um histórico voo de 10 dias 
            a bordo da nave Orion com o foguete SLS. Teste crucial para Artemis III!
        </div>

        <div class="cards">
            <div class="card">
                <img src="https://www.nasa.gov/wp-content/uploads/2023/11/artemis-ii-crew-1.jpg" alt="Tripulação">
                <div class="card-content">
                    <h3>👨‍🚀 Tripulação</h3>
                    <p><strong>Reid Wiseman (Cmd)</strong> • <strong>Victor Glover (Pilot)</strong><br>
                    <strong>Christina Koch</strong> • <strong>Jeremy Hansen</strong><br>
                    <strong>1ª mulher e 1º canadense em voo lunar!</strong></p>
                </div>
            </div>

            <div class="card">
                <img src="https://admin.cnnbrasil.com.br/wp-content/uploads/sites/12/2026/03/artemis-II-imagens-.png?w=419&h=283&crop=0" alt="SLS">
                <div class="card-content">
                    <h3>🚀 Space Launch System</h3>
                    <p>Foguete mais poderoso do mundo! 98 metros de altura.<br>8,8 milhões de libras de empuxo.</p>
                </div>
            </div>

            <div class="card">
                <img src="https://www.nationalgeographicbrasil.com/espaco/2022/08/como-o-programa-artemis-da-nasa-planeja-enviar-novamente-astronautas-a-lua" alt="Nave Orion">
                <div class="card-content">
                    <h3>🌌 Nave Orion</h3>
                    <p>Cápsula para 4 astronautas. Voo de 10 dias.<br>1º flyby lunar desde Apollo!</p>
                </div>
            </div>

            <!-- Imagens corrigidas e estáveis -->
            <div class="card">
                <img src="https://upload.wikimedia.org/wikipedia/commons/8/80/Artemis_II_art002e021278_earthset.jpg" 
                     alt="Earthset - Artemis II">
                <div class="card-content">
                    <h3>🛰️ Trajetória</h3>
                    <p>10 dias • 1,3 milhões de km<br>
                    Kennedy Space Center → Flyby da Lua → Retorno à Terra</p>
                </div>
            </div>

            <div class="card">
                <img src="https://images.unsplash.com/photo-1451187580459-43490279c0fa?w=1200" 
                     alt="Objetivos Artemis II">
                <div class="card-content">
                    <h3>🎯 Objetivos</h3>
                    <p>✅ Testar Orion + SLS com humanos<br>
                    ✅ 1ª mulher e 1º canadense em voo lunar<br>
                    ✅ Preparar Artemis III (pouso lunar)</p>
                </div>
            </div>
        </div>

        <footer>
            <p>🌟 Artemis II - A primeira luz da nova era lunar | NASA</p>
            <p>Desenvolvido com ❤️ | Flask</p>
        </footer>
    </div>

    <script>
        for(let i = 0; i < 200; i++){
            let star = document.createElement('div');
            star.className = 'star';
            star.style.left = Math.random() * 100 + 'vw';
            star.style.top = Math.random() * 100 + 'vh';
            star.style.width = (1 + Math.random() * 3.5) + 'px';
            star.style.height = star.style.width;
            star.style.animationDelay = Math.random() * 3 + 's';
            document.getElementById('stars').appendChild(star);
        }
    </script>
</body>
</html>
    """

if __name__ == "__main__":
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port, debug=True)
