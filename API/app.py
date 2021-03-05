from flask import Flask, request
from flask_restplus import Resource, Api

app = Flask(__name__)
api = Api(app, prefix="/api")

@api.route('/novo-jogo')
class NovoJogo(Resource):   
    def post(self):
        
        dados = request.get_json()
        nome = dados["nome"]
        classe = dados["classe"]

        return { 
            "NPC Marvin" : 
            f"Bem-vindo ao jogo {nome}, você escolheu bem! Será um {classe}" 
        }

if __name__ == '__main__':
   app.run('0.0.0.0', port=5000)