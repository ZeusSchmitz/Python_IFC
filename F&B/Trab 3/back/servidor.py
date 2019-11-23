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

@app.route("/incluirProduto", methods=['post'])
def incluirProduto():
    # preparar mensagem de retorno padrão (sucesso)
    msg = jsonify({"message":"ok"})
    # obter os dados
    dados = request.get_json(force=True)
    # obter os valores
    garrafa = dados['garrafa']
    nomProd = dados['nomProd']
    descProd = dados['descProd']
    # criar a nova produto
    Produto.create(garrafa=garrafa, nomProduto=nomProd, descProduto=descProd)
    return msg
    
@app.route("/excluirProduto")
def excluirProduto():
  # preparar mensagem de retorno padrão (sucesso)
  msg = jsonify({"message":"ok"})
  # obter o id
  id = request.args.get("id")
  # exclui
  Produto.delete_by_id(id)
  return msg

@app.route("/alterarProduto", methods=['post'])
def alterarProduto():
    # preparar mensagem de retorno padrão (sucesso)
    msg = jsonify({"message":"ok"})
    # obter os dados
    dados = request.get_json(force=True)
    # obter os dados da produto a ser alterada
    id = dados['id']
    garrafa = dados['garrafa']
    nomProd = dados['nomProd']
    descProd = dados['descProd']
    # obter a produto original
    prod = Produto.get_by_id(id)
    # alterar os dados da produto
    prod.garrafa = garrafa
    prod.nomProduto = nomProd
    prod.descProduto = descProd
    # atualizar os dados
    prod.save()
    return msg

@app.route("/consultarProduto")
def consultarProduto():
    # preparar mensagem de retorno padrão (sucesso)
    msg = jsonify({"message":"error","detail":"iniciando procedimentos"})
    # obter o id
    id = request.args.get("id")
    # obter a pessoa original
    prod = Produto.get_by_id(id)
    # preparar retorno
    msg = jsonify({"message":"ok","detail":"ok","data":model_to_dict(prod)})
    return msg

@app.route('/listarPedidos')
def listarPedidos():
    pedidos = list(map(model_to_dict, Pedido.select()))
    return jsonify(pedidos)

app.run(debug=True,port=4999)
