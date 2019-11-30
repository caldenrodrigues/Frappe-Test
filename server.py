from flask import Flask
from flask import request
from flask import jsonify
from flask_cors import CORS, cross_origin
import json

app = Flask(__name__)
CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'

@app.route('/addProduct', methods = ['POST'])
def addProduct():
    print(request.get_json())
    return "gg"

if __name__ == '__main__':
	app.run(debug = True)
