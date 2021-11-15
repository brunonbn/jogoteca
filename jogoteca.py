from flask import Flask, render_template

app = Flask(__name__)

class Jogo:
    def __init__(self, nome, categoria, console):
        self.nome = nome
        self.categoria = categoria
        self.console = console

@app.route('/inicio')
def ola():
    jogo1 = Jogo('Super Mario', 'Ação', 'SNES')
    jogo2 = Jogo('Pokemon Gold', 'RPG', 'GBA')
    jogo3 = Jogo('Tetris', 'Desafio', 'PC')

    lista = [jogo1, jogo2, jogo3]
    return render_template('lista.html', titulo = "Lista de Jogos", jogos = lista)

@app.route('/novo')
def novo():
    return render_template('novo.html', titulo = 'Novo jogo')

# não colocar essas configurações em produção
app.run(host='127.0.0.1', port=8080)