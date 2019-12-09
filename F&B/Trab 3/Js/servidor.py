from flask import Flask, json, jsonify
from flask import request
from modelo import Produto
from playhouse.shortcuts import model_to_dict

# inicializa o servidor
app = Flask(__name__)


@app.route('/', methods=['GET'])
def inicio():
    return "backend do sistema de pessoas; <a href=/listarProdutos>API listar produtos</a>"


@app.route('/listarProdutos')
def listar():
    # converte para pessoa para inserir em uma lista json
    produtos = list(map(model_to_dict, Produto.select()))
    # adiciona à lista json um nome
    response = jsonify({"lista": produtos})
    # informa que outras origens podem acessar os dados desde servidor/serviço
    response.headers.add('Access-Control-Allow-Origin', '*')
    # retorno!
    return response

@app.route('/incluirProduto', methods=['post'])
def incluirProduto():
    # prepara a resposta padrão otimista
    response = jsonify({"message": "ok", "details": "ok"})
    try:
        # pega os dados informados
        dados = request.get_json(force=True)
        garrafa = dados['garrafa']
        nomProd = dados['nomProd']
        descProd = dados['descProd']
        # criar a nova produto
        Produto.create(garrafa=garrafa, nomProduto=nomProd, descProduto=descProd)
 
    except Exception as e:
       # resposta de erro
       response = jsonify({"message": "error", "details": str(e)})

    # informa que outras origens podem acessar os dados desde servidor/serviço
    response.headers.add('Access-Control-Allow-Origin', '*')
    # retorno!
    return response

@app.route('/excluirProduto')
def excluirProduto():
    id_pessoa = request.args.get('id')
    Produto.delete_by_id(id_pessoa)
    response = jsonify({"message": "ok"})
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response

app.run(debug=True, port=4999)