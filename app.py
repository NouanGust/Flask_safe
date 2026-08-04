from flask import Flask, render_template, redirect, request

# Banco de dados
# No caso apenas uma lista inicialmente, mas no futuro será um banco com sqlite ou SqlAlchemy
filmes: list[str] = ["Batman", "Indiana Jones", "De Volta Para o Futuro", "Barbie"]

# Define o servidor
app = Flask("Lista de Filmes")


# Criação das rotas e regras

# o '@' define um Decorator, que é uma função que dá uma função a mais para quem está embaixo.
@app.route("/") # Entre parenteses definimos a rota que vamos acessar e outros parâmetros dessa rota
def home_page() -> str:
    return render_template("homepage.html",filmes=filmes, pag="Homepage") # O render_template irá renderizar um arquivo html que está na pasta templates!!!! TEM QUE ESTAR NA PASTA TEMPLATES!


@app.route("/filmes")
def lista_filmes() -> str:
    return render_template("filmes.html", filmes=filmes, pag="Filmes") # O segundo parâmetro aqui no render_template é para enviar uma váriavel para o html, do lado esquerdo é o nome da váriavel no html e do lado direito como ela está no python.
    
 
@app.route("/cadastrar_filme", methods=["POST"]) # O segundo parâmetro simboliza o método da rota, nesse caso POST, ela vai enviar uma informação
def add_filme() -> str:
    nf = request.form['titulo']
    if len(nf) >= 5:
        if not nf in filmes:
            filmes.append(nf) 
            return redirect("/filmes")
        else:
            return redirect("/homepage", filmes=filmes, pag="Homepage")
    else:
        return redirect("/homepage", filmes=filmes, pag="Homepage")
    
@app.route("/perfil")
def perfil() -> str:
    return render_template("perfil.html", pag="Perfil")

@app.route("/cadastro")
def cadastro_view() -> str:
    return render_template("cadastro.html", pag="Cadastro")


# Inicializa o servidor
app.run(debug=True) # O 'debug=True' serve para o desenvolvimento, ele ajuda nos testes das rotas e funções. Apagar quando for publicar