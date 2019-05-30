from flask import (Flask, redirect, render_template, request, session, url_for)
from flask_cors import CORS
from flask_restful import (Resource, Api, reqparse, )


app = Flask(__name__)
CORS(app)
api = Api(app)


@app.route('/')
def home():
    return render_template('test2.html')
    
if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True, port=9999)