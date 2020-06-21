from flask import Flask # 1.importando libreria
from flask import jsonify

app = Flask(__name__)   # 2.instanciando flask

# http://127.0.0.1:5000/getdata
@app.route('/getdata', methods=['GET']) # 4.Creando endpoint
def getdata():
    return "Hola Mundo"

# http://127.0.0.1:5000/postdata
@app.route('/postdata', methods=['POST']) # 4.Creando endpoint
def postdata():
    return jsonify(response = 'Metodo post OK')

if __name__ == '__main__': # 3.Creando el servidor
    app.run(debug=True)