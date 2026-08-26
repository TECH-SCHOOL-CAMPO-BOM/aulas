from flask import Flask, redirect, render_template, request, url_for

from main import ListaDeTarefas


app = Flask(__name__)
lista_de_tarefas = ListaDeTarefas()


@app.route("/")
def index():
    return render_template("index.html", tarefas=lista_de_tarefas.listar())


@app.post("/adicionar")
def adicionar_tarefa():
    titulo = request.form.get("titulo", "").strip()
    if titulo:
        lista_de_tarefas.adicionar(titulo)
    return redirect(url_for("index"))


@app.post("/concluir/<int:indice>")
def concluir_tarefa(indice):
    lista_de_tarefas.concluir(indice)
    return redirect(url_for("index"))


if __name__ == "__main__":
    app.run(debug=True)
