$("#btn_listar_produtos").click(function() {
    $.ajax({
        url: 'http://localhost:4999/listarProdutos',
        method: 'GET',
        dataType: 'json',
        success: function(resultado) {
            $('#produto').empty()
            produto = resultado.lista;
            var cabecalho = '<div class="rTableRow">' +
                '<div class="rTableHead">Garrafa</div>' +
                '<div class="rTableHead">Nome</div>' +
                '<div class="rTableHead">Des.Produto</div>' +
                '<div class="rTableHead"></div>' +
                '<div class="rTableHead"></div>' +
                '</div>';
            $('#produto').append(cabecalho);
            for (var i in produto) { //i vale a posição no vetor
                lin = '<div class="rTableRow" id=linha' + produto[i].id + '>'+
                      ajustar_produto_em_linha_de_tabela(
                    produto[i].id, produto[i].garrafa, produto[i].nomProduto, produto[i].descProduto) +
                    '</div>';
                $('#produto').append(lin);
            }
        },
        error: function() {
            alert("ocorreu algum erro na leitura dos dados, verifique o backend");
        }
    });
});

function ajustar_produto_em_linha_de_tabela(id, garrafa, nomProduto, descProduto) {

    var resp = '<div class="rTableCell" id="garrafa' + id + '">' + garrafa + '</div>' +
        '<div class="rTableCell" id="nomProduto' + id + '">' + nomProduto + '</div>' +
        '<div class="rTableCell" id="descProduto' + id + '">' + descProduto + '</div>' +
        '<div class="rTableCell"><img class=form_alterar_produto id=altp_' + id + ' src=img/alterar.png width=20 border=0></div>' +
        '<div class="rTableCell"><img class=excluir_produto id=excp_' + id + ' src=img/excluir.gif width=20 border=0></div>';
    return resp;
}

$("#btn_form_incluir_produto").click(function() {
    $("#html_form_incluir_produto").show();//.css("display", "inline-block");
});

$("#btn_incluir_produto").click(function() {

    // obtém os dados
    var garrafa = $("#garrafa").val();
    var nomProd = $("#nomProd").val();
    var descProd = $("#descProd").val();
    // prepara os dados em json
    var dados = JSON.stringify({ garrafa: garrafa, nomProd: nomProd, descProd: descProd })

    $.ajax({
        url: 'http://localhost:4999/incluirProduto',
        type: 'POST',
        dataType: 'json', // vou receber em json,
        data: dados, //JSON.stringify({ "message": "ok" }), // dados a enviar
        //contentType: "application/json",
        success: function(resultado) {
            var deu_certo = resultado.message == "ok";
            mostrar_resultado_acao(deu_certo);
            if (!deu_certo) {
                alert(resultado.message + ":" + resultado.details);
            }

        },
        error: function() {
            alert("ocorreu algum erro na leitura dos dados, verifique o backend");
        }
    });

});

function mostrar_resultado_acao(sucesso) {
    if (sucesso) {
        $("#success").fadeIn(1000);
    } else {
        $("#error").fadeIn(1000);
    }
}

$(document).on("click", ".excluir_produto", function() {
    // qual link foi clicado? pega o ID da imagem
    var eu = $(this).attr('id');
    // obtém o id da produto
    var id = eu.substring(5);

    $.ajax({
        url: 'http://localhost:4999/excluirProduto',
        type: 'GET',
        dataType: 'json', // vou receber em json,
        data: 'id=' + id,
        //contentType: "application/json",
        success: function(resultado) {
            var deu_certo = resultado.message == "ok"

            if (!deu_certo) {
                alert(resultado.message + ":" + resultado.details);
            } else {
                // remove a linha
                $("#linha" + id).hide(1000);
            }
        },
        error: function() {
            alert("ocorreu algum erro na leitura dos dados, verifique o backend");
        }
    });
});

function ajustar_produto_em_linha_de_tabela_modo_edicao(id_produto) {

    var nome = $("#nome" + id_produto).text();
    var end = $("#endereco" + id_produto).text();
    var tel = $("#telefone" + id_produto).text();

    var resp = '<div class="rTableCell"><input type=text id=novo_nome' + id_produto + ' size=10 value="' + nome + '"></div>' +
        '<div class="rTableCell"><input type=text id=novo_endereco' + id_produto + ' size=10 value="' + end + '"></div>' +
        '<div class="rTableCell"><input type=text id=novo_telefone' + id_produto + ' size=10 value="' + tel + '"></div>' +
        '<div class="rTableCell"><img class=acao_alterar_produto id=alterar' + id_produto + ' src=img/success.gif width=20 border=0></div>' +
        '<div class="rTableCell"><img class=acao_cancelar_alterar_produto id=cancelar' + id_produto + ' src=img/cancelar.png width=20 border=0></div>';

    return resp;
}

$(document).on("click", ".form_alterar_produto", function() {
    // qual link foi clicado? pega o ID da imagem
    var eu = $(this).attr('id');
    // obtém o id da produto
    var id_produto = eu.substring(5); // altp_ID
    // preenche a div da linha com dados editáveis
    $("#linha" + id_produto).html(ajustar_produto_em_linha_de_tabela_modo_edicao(id_produto));
});

$('.muda_estilo').click(function() {
    $('#estilo_tabela').attr('href', 'css/' + $(this).attr('id') + '.css');
});

$(document).on("click", ".acao_alterar_produto", function() {
    // qual link foi clicado? pega o ID da imagem
    var eu = $(this).attr('id');
    // obtém o id da produto
    var id_produto = eu.substring(7); // alterarID
    // obtém os dados
    var nome = $("#novo_nome" + id_produto).val();
    var end = $("#novo_endereco" + id_produto).val();
    var tel = $("#novo_telefone" + id_produto).val();

    // prepara os dados em json
    var dados = JSON.stringify({ id: id_produto, nome: nome, endereco: end, telefone: tel })

    $.ajax({
        url: 'http://localhost:4999/alterar_produto',
        type: 'POST',
        dataType: 'json', // vou receber em json,
        data: dados, //JSON.stringify({ "message": "ok" }), // dados a enviar
        //contentType: "application/json",
        success: function(resultado) {
            var deu_certo = resultado.message == "ok"
            if (!deu_certo) {
                alert(resultado.message + ":" + resultado.details);
            }
            // preenche a div da linha com dados editáveis
            //$("#linha" + id_produto).html(ajustar_produto_em_linha_de_tabela(id_produto, nome, end, tel));
        },
        error: function(request, status, error) {
            alert("ocorreu algum erro na leitura dos dados: ", request.responseText);
        }
    });
});