from flask import Flask, jsonify, request
import json

app = Flask(__name__)

@app.route("/<int:numero>", methods=['GET','POST'])
def hello(numero):
    return u'Olá mundo!: {}'.format(numero)

@app.route("/json")
def retornoJson():
    return jsonify({'nome': 'Elaine Cristina', 'sobrenome': 'Rocha de Oliveira'})

#{"valores":[10,11,12]}
@app.route("/soma", methods=['POST'])
def soma():
    dados = json.loads(request.data)
    total = sum(dados['valores'])
    return jsonify({'soma': total})


if __name__ == "__main__":
    app.run(debug=True)