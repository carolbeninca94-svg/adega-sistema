from flask import Flask, render_template, request

app = Flask(__name__)

produtos = []

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        nome = request.form.get("nome")
        tipo = request.form.get("tipo")
        preco = request.form.get("preco")

        produtos.append({
            "nome": nome,
            "tipo": tipo,
            "preco": preco
        })

    return render_template("index.html", produtos=produtos)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)