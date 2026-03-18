from flask import Flask, render_template, request, redirect

app = Flask(__name__)

produtos = []

@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        nome = request.form['nome']
        tipo = request.form['tipo']
        preco = request.form['preco']

        produtos.append({
            'nome': nome,
            'tipo': tipo,
            'preco': preco
        })

        return redirect('/')

    return render_template('index.html', produtos=produtos)

if __name__ == '__main__':
    app.run(debug=True)