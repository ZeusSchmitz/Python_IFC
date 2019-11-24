from flask import Flask, jsonify, render_template, request, redirect
from playhouse.shortcuts import dict_to_model
import requests
from cliente import *
from produto import Produto

app=Flask(__name__, static_url_path='',static_folder='templates')

@app.route("/")
def inicio():
    return redirect('/listarProdutos')

#--------------------------------PRODUTO-------------------------------------------#

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

@app.route("/formIncluirProduto")
def abreIncluirProduto():
    return render_template('incluirProduto.html')

@app.route("/incluirProduto", methods=['post'])
def incluirProduto():
    # obter os parâmetros do formulário
    garrafa = request.form["garrafa"]
    nomProduto = request.form["nomProd"]
    descProduto = request.form["descProd"]
    # elaborar os parâmetros no formato json
    par = {"garrafa":garrafa, "nomProd":nomProduto, "descProd":descProduto}
    # solicitar ao backend a criação da produto
    req = requests.post(url='http://localhost:4999/incluirProduto', json=par)
    # obter a resposta
    resp = req.json()
    if resp['message'] == 'ok':
        msg = "Produto incluído com sucesso"
    else:
        msg = "Erro: "+resp['details']
    # encaminhar a resposta para uma página de exibição de mensagens
    return render_template('exibirMensagem.html', mensagem=msg)

@app.route("/excluirProduto")
def excluirProduto():
    # obter o nome da produto a ser excluída
    id = request.args.get("id")
    # solicitar a exclusão
    req = requests.get('http://localhost:4999/excluirProduto?id='+id)
    # obter a resposta
    resp = req.json()
    if resp['message'] == 'ok':
        return redirect("/listarProdutos")
    else:
        msg = "Erro: "+resp['details']
        # encaminhar a resposta para uma página de exibição de mensagens
        return render_template('exibirMensagem.html', mensagem=msg)

@app.route("/formAlterarProduto")
def formAlterarProduto():
    # obter id da produto a ser alterada
    id = request.args.get("id")
    # obter a produto
    req = requests.get('http://localhost:4999/consultarProduto?id='+id)
    # obter a resposta
    resp = req.json()
    if resp['message'] == 'ok':
        # converter a resposta para a produto
        p = dict_to_model(Produto, resp['data'])
        # encaminhar o fluxo para a página de alteração
        return render_template("alterarProduto.html", produto=p)
    else:
        msg = "Erro: "+resp['details']
        # encaminhar a resposta para uma página de exibição de mensagens
        return render_template('exibirMensagem.html', mensagem=msg)

@app.route("/alterarProduto", methods=['post'])
def alterarProduto():
    # obter os parâmetros do formulário
    id = request.form['id']
    garrafa = request.form["garrafa"]
    nomProduto = request.form["nomProd"]
    descProduto = request.form["descProd"]
    # elaborar os parâmetros no formato json
    par = {"id":id, "garrafa":garrafa, "nomProd":nomProduto, "descProd":descProduto}
    # solicitar ao backend a alteração da produto
    req = requests.post(url='http://localhost:4999/alterarProduto', json=par)
    # obter a resposta
    resp = req.json()
    if resp['message'] == 'ok':
        return redirect("/listarProdutos")
    else:
        msg = "Erro: "+resp['details']
        # encaminhar a resposta para uma página de exibição de mensagens
        return render_template('exibirMensagem.html', mensagem=msg)

#---------------------------------------------------------------------------#

#--------------------------------Cliente------------------------------------#

@app.route('/listarClientes')
def listarClientes():
    #obter do back os dados dos produto;
    clientesDados = requests.get('http://localhost:4999/listarClientes')
    #converter os dados recebidos para json
    jsonClientes = clientesDados.json()
    clientes = []
    #percorrer os cliente em json
    for clienteJson in jsonClientes:
        #converter o cliente em json para cliente peewe;
        p = dict_to_model(Cliente, clienteJson)
        #adiciona o cliente convertido a lista de cliente;
        clientes.append(p)
    #fornecer a lista de cliente para o front exibir os cliente na pagina;
    #return redirect("/")
    return render_template('listarClientes.html', listaCliente = clientes)

@app.route("/formIncluirCliente")
def abreIncluirCliente():
    return render_template('incluirCliente.html')

@app.route("/incluirCliente", methods=['post'])
def incluirCliente():
    # obter os parâmetros do formulário
    nome = request.form["nome"]
    cpf = request.form["cpf"]
    email = request.form["email"]
    # elaborar os parâmetros no formato json
    par = {"nome":nome, "cpf":cpf, "email":email}
    # solicitar ao backend a criação da cliente
    req = requests.post(url='http://localhost:4999/incluirCliente', json=par)
    # obter a resposta
    resp = req.json()
    if resp['message'] == 'ok':
        msg = "Cliente incluído com sucesso"
    else:
        msg = "Erro: "+resp['details']
    # encaminhar a resposta para uma página de exibição de mensagens
    return render_template('exibirMensagem.html', mensagem=msg)

@app.route("/excluirCliente")
def excluirCliente():
    # obter o nome da cliente a ser excluído
    id = request.args.get("cpf")
    # solicitar a exclusão
    req = requests.get('http://localhost:4999/excluirCliente?cpf='+id)
    # obter a resposta
    resp = req.json()
    if resp['message'] == 'ok':
        return redirect("/listarClientes")
    else:
        msg = "Erro: "+resp['details']
        # encaminhar a resposta para uma página de exibição de mensagens
        return render_template('exibirMensagem.html', mensagem=msg)

@app.route("/formAlterarCliente")
def formAlterarCliente():
    # obter id da cliente a ser alterada
    id = request.args.get("cpf")
    # obter a cliente
    req = requests.get('http://localhost:4999/consultarCliente?cpf='+id)
    # obter a resposta
    resp = req.json()
    if resp['message'] == 'ok':
        # converter a resposta para o cliente
        c = dict_to_model(Cliente, resp['data'])
        # encaminhar o fluxo para a página de alteração
        return render_template("alterarCliente.html", cliente=c)
    else:
        msg = "Erro: "+resp['details']
        # encaminhar a resposta para uma página de exibição de mensagens
        return render_template('exibirMensagem.html', mensagem=msg)

@app.route("/alterarCliente", methods=['post'])
def alterarCliente():
    # obter os parâmetros do formulário
    nome = request.form['nome']
    cpf = request.form['cpf']
    email = request.form['email']
    # elaborar os parâmetros no formato json
    par = {"nome":nome, "cpf":cpf, "email":email}
    # solicitar ao backend a alteração da cliente
    req = requests.post(url='http://localhost:4999/alterarCliente', json=par)
    # obter a resposta
    resp = req.json()
    if resp['message'] == 'ok':
        return redirect("/listarClientes")
    else:
        msg = "Erro: "+resp['details']
        # encaminhar a resposta para uma página de exibição de mensagens
        return render_template('exibirMensagem.html', mensagem=msg)

app.run(debug=True)