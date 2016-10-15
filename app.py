from flask import Flask
app = Flask(__name__)


@app.route('/')
def hello():
    return "<h1 align=center>Espaço Rogue (Rosa Yogue)!</h1><h4 align=center>Em construção<br>Assim como nós em constante construção</h4><br><br><br><h2 align=center>Acesse: <a href=https://www.facebook.com/espacorogue/>Face Aqui</a> </h2> <h4 align=center>Para maiores informações</h4>"

if __name__ == '__main__':
    app.run()