#----------------------------------------------------------------------------#
# Imports
#----------------------------------------------------------------------------#

from flask import Flask, render_template, url_for, request, jsonify, json
import requests
import os.path
import os
from base import encode, decode

#----------------------------------------------------------------------------#
# App Config.
#----------------------------------------------------------------------------#

app = Flask(__name__)

BASE_DIR    = os.path.dirname(os.path.abspath(__file__))

#----------------------------------------------------------------------------#
# Controllers.
#----------------------------------------------------------------------------#

@app.route('/', methods=['POST'])
def index():
    data = request.get_json(force=True)
    print(data)
    response = {}
    metadata = {}
    for key, values in data.items():
        if type(values) == dict:
            print('dict')
        elif type(values) == list:
            s = encode(key)
            response[str(s)]=[]
            metadata[key] = s
            list_json={}
            list_json = traverselist(values, list_json, metadata)
            response[str(s)].extend(list_json)
        else:
            s = encode(key)
            response[str(s)] = values
            print(response)
            metadata[key] = s
    response['meta'] = metadata
    print(response)
    res=json.dumps(response).encode('utf-8')
    return res

def traverselist(listObj, response, metadata):
    list_json=[]
    if len(listObj) > 0:
        for value in listObj:
            print ('---------')
            print (value)
            print ('---------')
            if(type(value) is dict):
                dict_json = traversedic(value, response, metadata)
                list_json.append(dict_json)
                print('list json')
                print(list_json)
            else:
                print ("-" + str(value))
                print (type(value))
    return list_json
                
def traversedic(dic, response, metadata):
    dict_json = {}
    for key, value in dic.items():
        if (type(value) is dict):
            print('dict')
        elif (type(value) is list):
            traverselist(conn, value, url)
        else:
            s = encode(key)
            dict_json[str(s)] = value
            metadata[key] = s
    print('dict json')
    print(dict_json)
    return dict_json
#----------------------------------------------------------------------------#
# Launch.
#----------------------------------------------------------------------------#

if __name__ == '__main__':
    #app.debug = True;1
    app.run('127.0.0.1', 4000, True)
