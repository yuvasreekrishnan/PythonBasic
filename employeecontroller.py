from flask import Flask,jsonify,request
import mysql.connector
from mysql.connector import Error
app=Flask(__name__) 
def mysqlConnect():
    return mysql.connector.connect(
            host="localhost",
            database="mydatabase",   # add your DB name
            user="root",
            password="Yuvasree@24"
        )


@app.route('/getDetails',methods=['GET'])
def empDetails():
    connection=mysqlConnect()
    cursor = connection.cursor(dictionary=True)
    selectQuery = "SELECT * FROM employees"
    cursor.execute(selectQuery)
    result = cursor.fetchall()

    
    cursor.close()
    connection.close()

    return jsonify(result)

@app.route('/postDetails',methods=['POST'])
def insertDetails():
    data=request.json

    connection=mysqlConnect()
    cursor = connection.cursor()

    insertQuery = "INSERT INTO employees(emp_id, emp_name, dept_id) VALUES (%s, %s, %s)"
    emp_data=(data.get('emp_id'),data.get('emp_name'),data.get('dept_id'))
    
    cursor.execute(insertQuery,emp_data) 
    connection.commit()

    cursor.close()
    connection.close()

    
    return jsonify({
        "message":"Employee details inserted successfully ",
        "data":data
    })


if __name__=="__main__":
    app.run(port=8081)