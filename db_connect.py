import mysql.connector
from mysql.connector  import Error

def mysqlConnect():
    connection = None
    try:
        connection = mysql.connector.connect(
            host='localhost',
            database='mydatabase',
            user='root',
            password='Yuvasree@24'
        )
        if connection.is_connected():
            print("Connected to MySQL database")
            cursor = connection.cursor()
            selectQuery = "SELECT * FROM employees"
            cursor.execute(selectQuery)
            result = cursor.fetchall()
            print(result)

            insertQuery = """
                INSERT INTO employees(emp_id, emp_name, dept_id)
                VALUES (%s, %s, %s)
                """
            data = (110, 'John Doe', 2)
            cursor.execute(insertQuery, data)
            connection.commit()


    except Error as e:
        print(e)
    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()
            print("MySQL connection is closed")
mysqlConnect()
     
