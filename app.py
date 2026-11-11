from flask import Flask, render_template_string, request
app = Flask(__name__)
HTML = """
<!DOCTYPE html>
<html lang="es">
<head><meta charset="UTF-8"><meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>RAUDY VIP ORO</title>
<style>
body{background:#000;color:#fff;font-family:Arial;text-align:center;padding:20px}
h1{color:#FFD700;font-size:38px}
.card{background:#111;border:2px solid #FFD700;border-radius:15px;padding:20px;margin:15px auto;max-width:350px}
button{background:#FFD700;color:#000;border:none;padding:15px;font-size:18px;font-weight:bold;border-radius:10px;width:100%}
.price{color:#00FF00;font-size:24px;font-weight:bold}
.wa{background:#25D366;color:#fff;display:block;padding:15px;border-radius:10px;text-decoration:none;font-weight:bold;margin:20px}
</style></head>
<body>
<h1>👑 RAUDY VIP ORO 👑</h1><p>CALIDAD ORO - 100% CONFIABLE</p>
<div class="card"><h2>⌚ RELOJ VIP ORO</h2><p>Reloj Premium Lujo</p><p class="price">$19.99</p>
<form action="/comprar" method="post"><input name="producto" value="RELOJ VIP ORO" hidden><button>🛒 COMPRAR</button></form></div>
<div class="card"><h2>⛓️ CADENA ORO VIP</h2><p>Cadena Dorada Estilo Raudy</p><p class="price">$29.99</p>
<form action="/comprar" method="post"><input name="producto" value="CADENA ORO VIP" hidden><button>🛒 COMPRAR</button></form></div>
<div class="card"><h2>🕶️ LENTES VIP</h2><p>Lentes Premium</p><p class="price">$14.99</p>
<form action="/comprar" method="post"><input name="producto" value="LENTES VIP" hidden><button>🛒 COMPRAR</button></form></div>
<a class="wa" href="https://wa.me/18090000000">💬 PEDIR POR WHATSAPP</a>
<p>© 2026 RAUDY VIP ORO</p>
</body></html>
"""
GRACIAS = """<!DOCTYPE html><html><head><meta charset="UTF-8"><meta name="viewport" content="width=device-width, initial-scale=1.0"><style>body{background:#000;color:#fff;text-align:center;font-family:Arial;padding:40px}h1{color:#FFD700}a{background:#FFD700;color:#000;padding:15px 30px;border-radius:10px;text-decoration:none;font-weight:bold;display:inline-block}</style></head><body><h1>👑 GRACIAS JEFE 👑</h1><h2>Pediste: {prod}</h2><p>Te escribimos por WhatsApp</p><a href="/">VOLVER</a></body></html>"""
@app.route("/")
def home(): return render_template_string(HTML)
@app.route("/comprar", methods=["POST"])
def comprar():
    prod = request.form.get("producto","PRODUCTO VIP")
    return render_template_string(GRACIAS.format(prod=prod))
@app.route("/health")
def health(): return "OK"
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
