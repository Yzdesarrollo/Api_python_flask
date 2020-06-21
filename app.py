from flask import Flask # 1.importando libreria

app = Flask(__name__)   # 2.instanciando flask

# http://127.0.0.1:5000/list
@app.route('/list', methods=['GET']) # 4.Creando endpoint
def getdata():
    return "Hola Mundo"

if __name__ == '__main__': # 3.Creando el servidor
    app.run()