#----------------------------------------------------------------------------#
# Imports
#----------------------------------------------------------------------------#

from flask import Flask, render_template, url_for, request, json
from flask import make_response
import requests
import os.path
import os
from core import convert_json_to_tson, convert_tson_to_json

#----------------------------------------------------------------------------#
# App Config.
#----------------------------------------------------------------------------#

app = Flask(__name__)

BASE_DIR    = os.path.dirname(os.path.abspath(__file__))

#----------------------------------------------------------------------------#
# Controllers.
#----------------------------------------------------------------------------#

@app.route('/convert_to_tson', methods=['POST'])
def convert_to_tson():
    data = request.get_json()
    print(data)
    res = convert_json_to_tson(data)
    return res

@app.route('/convert_to_json', methods=['POST'])
def convert_to_json():
    tson = request.get_json()
    print(tson)
    res = convert_tson_to_json(tson)
    return res

#----------------------------------------------------------------------------#
# Launch.
#----------------------------------------------------------------------------#

if __name__ == '__main__':
    #app.debug = True;1
    app.run('127.0.0.1', 4000, True)
