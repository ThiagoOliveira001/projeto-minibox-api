from flask import Flask,request
from flask_cors import CORS, cross_origin
from flask_restful import Resource, Api
from json import dumps
from flask_jsonpify import jsonify
from Principal import Main

main = Main()
app = Flask(__name__)
api = Api(app)
CORS(app)

@app.route("/")
def hello():
    return jsonify({"text":"HELLO"})

@app.route("/produto", methods=['POST'])
def inserir():
    main.cadastrarProduto(request.json)
    return jsonify({"message":"Ok"})
    

if __name__ == '__main__':
    app.run(port=5002)
