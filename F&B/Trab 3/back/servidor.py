from flask import Flask, jsonify, render_template, request, redirect
from playhouse.shortcuts import model_to_dict
from cliente import *
from produto import *
from pedido import *

listaProdutos = []

app=Flask(__name__)

@app.route('/')
def inicio():
    return 'Servidor de api backend<a href=/listarProdutos>listar</a>'

@app.route('/listarProdutos')
def listarProduto():
    produtos = list(map(model_to_dict, Produto.select()))
    return jsonify(produtos)

@app.route('/listarPedidos')
def listarPedidos():
    pedidos = list(map(model_to_dict, Pedido.select()))
    return jsonify(pedidos)

app.run(debug=True,port=4999)
