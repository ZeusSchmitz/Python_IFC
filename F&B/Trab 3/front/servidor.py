from flask import Flask, jsonify, render_template, request, redirect
from playhouse.shortcuts import dict_to_model
import requests
#from cliente import *
from produto import Produto

app=Flask(__name__, static_url_path='',static_folder='templates')

@app.route("/")
def inicio():
    return redirect('/listarProdutos')

@app.route('/listarProdutos')
def listarProdutos():
    #obter do back os dados dos produto;
    produtosDados = requests.get('http://localhost:4999/listarProdutos')
    #converter os dados recebidos para json
    jsonProdutos = produtosDados.json()
    produtos = []
    #percorrer os produto em json
    for produtoJson in jsonProdutos:
        #converter o produto em json para produto peewe;
        p = dict_to_model(Produto, produtoJson)
        #adiciona o produto convertido a lista de produto;
        produtos.append(p)
    #fornecer a lista de produto para o front exibir os produto na pagina;
    #return redirect("/")
    return render_template('listarProdutos.html', listaProduto = produtos)

@app.route("/incluirProduto")
def incluirProduto():
    return render_template('incluirProduto.html')

app.run(debug=True)