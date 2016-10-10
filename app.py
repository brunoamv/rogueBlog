from flask import Flask
app = Flask(__name__)


@app.route('/')
def hello():
    return "<h1 align=center>Espaço Rogue (Rosa Yogue)!</h1><h4 align=center>Em construção</h4><br><br><br><h2 align=center>Acesse: https://www.facebook.com/espacorogue/ </h2> <h4 align=center>Para maiores informações</h4>"

if __name__ == '__main__':
    app.run()