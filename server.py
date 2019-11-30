from flask import Flask
from flask import request
from flask import jsonify
from flask_cors import CORS, cross_origin
import json
import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  passwd="root",
  database="FrappeTest"
)
cur = mydb.cursor()

app = Flask(__name__)
CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'


@app.route('/addProduct', methods = ['POST'], endpoint='addProduct')
def addProduct():
    req = request.get_json()
    cur.execute("INSERT INTO Product(name,description) values(%s,%s)",(req["name"],req["description"]))
    mydb.commit()
    return getProduct()


@app.route('/getProduct', methods = ['POST'], endpoint='getProduct')
def getProduct():
    cur.execute("SELECT * FROM Product")
    res = cur.fetchall()
    mydb.commit()
    jsonArr = []
    for i in res:
        jsonArr.append({"id":i[0],"name":i[1],"description":i[3]})
    jsonRes = {}
    jsonRes["products"] = jsonArr
    return jsonify(jsonRes)


@app.route('/editProduct', methods = ['POST'], endpoint='editProduct')
def editProduct():
    req = request.get_json()
    cur.execute("UPDATE Product set name = %s, description = %s where id = %s",(req["name"],req["description"],req["id"]))
    mydb.commit()
    return getProduct()


@app.route('/delProduct', methods = ['POST'], endpoint='delProduct')
def delProduct():
    req = request.get_json()
    print(req)
    cur.execute("DELETE FROM Product WHERE id = %s",(int(req["id"]),))
    mydb.commit()
    return getProduct()

#Locations
@app.route('/addLocation', methods = ['POST'], endpoint='addLocation')
def addLocation():
    req = request.get_json()
    cur.execute("INSERT INTO Location(name) values(%s)",(req["name"],))
    mydb.commit()
    return getLocation()


@app.route('/getLocation', methods = ['POST'], endpoint='getlocation')
def getLocation():
    cur.execute("SELECT * FROM Location")
    res = cur.fetchall()
    mydb.commit()
    jsonArr = []
    for i in res:
        jsonArr.append({"id":i[0],"name":i[1]})
    jsonRes = {}
    jsonRes["locations"] = jsonArr
    return jsonify(jsonRes)


@app.route('/editLocation', methods = ['POST'], endpoint='editLocation')
def editLocation():
    req = request.get_json()
    cur.execute("UPDATE Location set name = %s where id = %s",(req["name"],req["id"]))
    mydb.commit()
    return getLocation()


@app.route('/delLocation', methods = ['POST'], endpoint='delLocation')
def delLocation():
    req = request.get_json()
    print(req)
    cur.execute("DELETE FROM Location WHERE id = %s",(int(req["id"]),))
    mydb.commit()
    return getLocation()


if __name__ == '__main__':
    app.run(debug = True)
