
from flask import Flask, jsonify, request
from pyswip import Prolog
from flask_cors import CORS  # Permite que o frontend se conecte ao backend

app = Flask(__name__)
CORS(app)  # Habilita o CORS para permitir requisições do frontend

prolog = Prolog()

# Base de Conhecimento do Prolog
base_conhecimento = [
    ('Computador não liga', 'Verifique se o cabo de alimentação está conectado corretamente.'),
    ('Internet lenta', 'Reinicie o modem e o roteador. Verifique se outros dispositivos estão consumindo muita largura de banda.'),
    ('Tela azul', 'Pode ser causado por erro de hardware ou software. Tente reiniciar em modo seguro e atualizar os drivers.'),
    ('Teclado não funciona', 'Verifique a conexão do teclado e certifique-se de que não há sujeira nos conectores.'),
    ('Erro de driver', 'Abra o Gerenciador de Dispositivos e atualize o driver do dispositivo com erro.')
]

# Carregar a base de conhecimento no Prolog
for problema, solucao in base_conhecimento:
    prolog.assertz(f'problema("{problema.lower()}", "{solucao}")')

@app.route('/')
def home():
    return '''
    <!DOCTYPE html>
    <html lang="pt-br">
    <head>
        <meta http-equiv="refresh" content="0; url=/static/index.html" />
    </head>
    <body>
        Redirecionando para a página inicial...
    </body>
    </html>
    '''

@app.route('/diagnostico', methods=['GET'])
def diagnostico():
    # Obter o problema da consulta
    problema = request.args.get('problema', '').strip().lower()
    if not problema:
        return jsonify({"erro": "Parâmetro 'problema' não informado."}), 400

    # Consultar a solução no Prolog
    query = f'problema("{problema}", Solucao)'
    resultados = list(prolog.query(query))
    
    if resultados:
        solucao = resultados[0]['Solucao']
        return jsonify({"problema": problema, "solucao": solucao})
    else:
        return jsonify({"erro": "Problema não encontrado. Tente outra descrição."}), 404

if __name__ == '__main__':
    app.run(debug=True, host='127.0.0.1', port=5000)
