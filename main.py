from flask import Flask, render_template, session, request

app = Flask(__name__)
app.secret_key = 'senha'


@app.route("/")
def index():
    session['usuario'] = 'Administrador'
    return render_template("base.html", titulo="Página de Início", usuario="ADM")


if __name__ == "__main__":
    app.run(debug=True)
