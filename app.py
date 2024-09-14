from flask import Flask, render_template, request, url_for
import json
from flask import flash, redirect


app = Flask(__name__)
app.config['SECRET_kEY'] = 'aluno123'

@app.route('/')
def index():
    return render_template('paginaInicial.html')

@app.route('/login')
def login ():
    return render_template('login.html')

@app.route('/novo-usuario')
def novoUsuario ():
    return render_template('cadastroUsuario')

@app.route('/cadastro-capitais')
def cadastroCapitais():
    return render_template('cadastroCapitais.html')

@app.route('/confirmar-cadastro')
def confirmaCadastro():
    return render_template('resultadocadastro.html')

@app.route('/exibir-capitais')
def exibirCapitais():
    return render_template('exibirCapitais.html')

@app.route('/autenticar', methods=['POST'])
def autenticar():
    usuario = request.form.get("usuario")
    senha = request.form.get("senha")
    if usuario != 'admin' or senha != 'senha123':
       flash("Login ou senha incorretos")
       return redirect("/login")
    else:
       	 return "Os dados recebidos foram: usuario = {} e senha = {}".format(usuario, senha)


if __name__ == '__main__':
    app.run(debug=True)
