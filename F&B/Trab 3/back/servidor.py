from flask import Flask, jsonify, render_template, request, redirect, json
from playhouse.shortcuts import model_to_dict
from cliente import *
from produto import *
from pedido import *

listaProdutos = []

app=Flask(__name__)

@app.route('/')
def inicio():
    return 'Servidor de api backend<a href=/listarPedidos>listar</a>'

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

@app.route('/listarClientes')
def listarClientes():
    clientes = list(map(model_to_dict, Cliente.select()))
    return jsonify(clientes)

@app.route("/incluirCliente", methods=['post'])
def incluirCliente():
    # preparar mensagem de retorno padrão (sucesso)
    msg = jsonify({"message":"ok"})
    # obter os dados
    dados = request.get_json(force=True)
    # obter os valores
    nome = dados['nome']
    cpf = dados['cpf']
    email = dados['email']
    # criar o novo cliente
    Cliente.create(nome=nome, cpf=cpf, email=email)
    return msg
    
@app.route("/excluirCliente")
def excluirCliente():
  # preparar mensagem de retorno padrão (sucesso)
  msg = jsonify({"message":"ok"})
  # obter o id
  id = request.args.get("cpf")
  # exclui
  Cliente.delete_by_id(id)
  return msg

@app.route("/alterarCliente", methods=['post'])
def alterarCliente():
    # preparar mensagem de retorno padrão (sucesso)
    msg = jsonify({"message":"ok"})
    # obter os dados
    dados = request.get_json(force=True)
    # obter os dados da cliente a ser alterada
    nome = dados['nome']
    cpf = dados['cpf']
    email = dados['email']
    # obter a cliente original
    cliente = Cliente.get_by_id(cpf)
    # alterar os dados da cliente
    cliente.nome = nome
    cliente.cpf = cpf
    cliente.email = email
    # atualizar os dados
    cliente.save()
    return msg

@app.route("/consultarCliente")
def consultarCliente():
    # preparar mensagem de retorno padrão (sucesso)
    msg = jsonify({"message":"error","detail":"iniciando procedimentos"})
    # obter o id
    id = request.args.get("cpf")
    # obter a pessoa original
    cliente = Cliente.get_by_id(id)
    # preparar retorno
    msg = jsonify({"message":"ok","detail":"ok","data":model_to_dict(cliente)})
    return msg

@app.route('/listarPedidos')
def listarPedidos():
    pedidos = list(map(model_to_dict, Pedido.select()))
    return jsonify(pedidos)

@app.route("/efetuarPedido", methods=['post'])
def efetuarPedido():
    msg = jsonify({"message":"ok"})
    dados = request.get_json(force=True)
    cliente = dados['cliente']
    produto = dados['produto']
    qtdProd = dados['qtdProd']
    Pedido.create(cliente=cliente, produto=produto, qtdProd=qtdProd)
    return msg
    
@app.route("/alterarPedido", methods=['post'])
def alterarPedido():
    msg = jsonify({"message":"ok"})
    dados = request.get_json(force=True)
    id = dados['id']
    cliente = dados['cliente']
    produto = dados['produto']
    qtdProd = dados['qtdProd']
    pedido = Pedido.get_by_id(id)
    # alterar os dados da cliente
    pedido.cliente = cliente
    pedido.produto = produto
    pedido.qtdProd = qtdProd
    # atualizar os dados
    pedido.save()
    return msg
    
@app.route("/consultarPedido")
def consultarPedido():
    # preparar mensagem de retorno padrão (sucesso)
    msg = jsonify({"message":"error","detail":"iniciando procedimentos"})
    # obter o id
    id = request.args.get("id")
    # obter a pessoa original
    pedido = Pedido.get_by_id(id)
    # preparar retorno
    msg = jsonify({"message":"ok","detail":"ok","data":model_to_dict(pedido)})
    return msg

@app.route("/excluirPedido")
def excluirPedido():
  # preparar mensagem de retorno padrão (sucesso)
  msg = jsonify({"message":"ok"})
  # obter o id
  id = request.args.get("id")
  # exclui
  Pedido.delete_by_id(id)
  return msg

app.run(debug=True,port=4999)
