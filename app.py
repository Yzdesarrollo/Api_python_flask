from flask import Flask, request # 1.importando libreria de Flask
from flask import jsonify # 5. importando JSON
import mysql.connector # 6. importando mysql

mydb = mysql.connector.connect(  # Configuracion 
  host="localhost",
  user="root",
  password="",
  database="taskapp"
)

app = Flask(__name__)   # 2.instanciando flask

# http://127.0.0.1:5000/read
@app.route('/read', methods=['GET']) # 4.Creando endpoint
def read():
    sql = "SELECT * FROM tasks"
    cur = mydb.cursor()
    cur.execute(sql)
    result = cur.fetchall()
    print(result)
    return jsonify(data = result)
    #return render_template('home.html');

# http://127.0.0.1:5000/create
@app.route('/create', methods=['POST']) 
def create():
    data = request.get_json()
    task = data['task']
    date = data['date']
    sql = f"INSERT INTO tasks (task, date) VALUES ('{task}', '{date}')"
    cur = mydb.cursor()
    cur.execute(sql)
    mydb.commit()
    print('task=> ', task, 'date=> ', date)
    return jsonify(response = 'Metodo post OK')

# http://127.0.0.1:5000/update
@app.route('/update', methods=['PUT']) 
def updatedata():
    data = request.get_json()
    id = data['id']
    task = data['task']
    date = data['date']
    sql = f"UPDATE tasks SET task = '{task}', date = '{date}' WHERE id = {id}"
    cur = mydb.cursor()
    cur.execute(sql)
    mydb.commit()
    print(task, date)
    return jsonify(response = 'Metodo put OK')

# http://127.0.0.1:5000/delete
@app.route('/delete', methods=['DELETE']) 
def deletedata():
    data = request.get_json()
    id = data['id']
    sql = f"DELETE FROM tasks WHERE id={id}"
    cur = mydb.cursor()
    cur.execute(sql)
    mydb.commit()
    return jsonify(response = 'Metodo delete OK')

if __name__ == '__main__': # 3.Creando el servidor
    app.run(debug=True)