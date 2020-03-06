from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/<int:numero>", methods=['GET','POST'])
def hello(numero):
    return u'Olá mundo!: {}'.format(numero)

@app.route("/json")
def retornoJson():
    return jsonify({'nome': 'Elaine Cristina', 'sobrenome': 'Rocha de Oliveira'})

if __name__ == "__main__":
    app.run(debug=True)