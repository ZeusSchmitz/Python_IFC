from flask import Flask, render_template
from pessoa import Pessoa
app=Flask(__name__, static_url_path='',static_folder='templates')

@app.route("/")
def index():
    return render_template('index.html')

@app.route("/cliente")
def cliente():
    pessoas = [ Pessoa("Zeus","Beco","9898765"),
            Pessoa("Zec","Ponte","9876557")
    ]

    return render_template("cliente.html", lista = pessoas)

@app.route("/fotos")
def fotos():
    return render_template('fotos.html')

@app.route("/pedido")
def pedido():
    return render_template('pedido.html')

@app.route("/produto")
def produto():
    return render_template('produto.html')

app.run(debug=True)
