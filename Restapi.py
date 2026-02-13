from flask import Flask
# from mysql import mysqlConnect

app = Flask(__name__)
@app.route('/home', methods=['GET'])
def getValueFromServer():  
    # data = mysqlConnect()
    # return  jsonify(data)   
    return "Welcome all"

if __name__ == '__main__':
    app.run()