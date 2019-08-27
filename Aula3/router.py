from flask import Flask, render_template, request, redirect
from cadastro_prod import Produto
app=Flask(__name__, static_url_path='',static_folder='templates')

listaProduto = []

@app.route("/")
def index():
    return render_template('index.html')

@app.route("/cliente")
def cliente():
    return render_template("cliente.html")

@app.route("/fotos")
def fotos():
    return render_template('fotos.html')

@app.route("/pedido")
def pedido():
    return render_template('pedido.html')

@app.route("/listarProdutos")
def listarProdutos():

    return render_template('produto.html', listaProduto = listaProduto)

@app.route("/inserirProduto", methods=['post'])
def produto():
    garrafa = request.form["tGarrafa"]
    nomeProd = request.form["tNome"]
    descProd = request.form["tDesc"]
    produto = Produto(garrafa, nomeProd, descProd)
    listaProduto.append(produto)
    return redirect("/listarProdutos")

@app.route("/excluirProduto")
def excluirProduto():
    nomProdAexcluir = request.args.get("prodExcluir")
    for produtoAexcluir in listaProduto:
        if nomProdAexcluir == produtoAexcluir.nomeProd:
           listaProduto.remove(produtoAexcluir)
    return redirect("/listarProdutos") 

app.run(debug=True)
