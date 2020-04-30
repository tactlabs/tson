#----------------------------------------------------------------------------#
# Imports
#----------------------------------------------------------------------------#

from flask import Flask, render_template, url_for, request, json
from flask import make_response
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
    data = request.get_json()
    print(data)
    response = {}
    metadata = {}
    i = 0
    for key, values in data.items():
        if type(values) == dict:
            print('dict')
        elif type(values) == list:
            meta = metadata.get(key)
            if(meta is None):
                response[str(i)]=[]
                sub = i
                metadata[key] = i
                i += 1
            else:
                response[str(meta)]=[]
                sub = meta
            list_json={}
            list_json = traverselist(values, list_json, metadata, i)
            response[str(sub)].extend(list_json)
        else:
            meta = metadata.get(key)
            print('meta_{}'.format(meta))
            if(meta is None):
                response[str(i)] = values
                metadata[key] = i
                i += 1
            else:
                response[str(meta)] = values
    response['meta'] = swap_metadata(metadata)
    print(response)
    #res=json.dumps(response).encode('utf-8')
    res = make_response(json.dumps(response, ensure_ascii=False))
    res.headers["Content-Type"] = "application/json; charset=utf-8"
    return res

def swap_metadata(metadata):
    meta_data={}
    for key, value in metadata.items():
        meta_data[str(value)] = str(key)
    return meta_data

def traverselist(listObj, response, metadata, i):
    list_json=[]
    if len(listObj) > 0:
        for value in listObj:
            print ('---------')
            print (value)
            print ('---------')
            if(type(value) is dict):
                dict_json, i = traversedic(value, response, metadata, i)
                print(i)
                list_json.append(dict_json)
                print('list json')
                # print(list_json)
            else:
                print ("-" + str(value))
                print (type(value))
    return list_json
                
def traversedic(dic, response, metadata, i):
    dict_json = {}
    for key, value in dic.items():
        if (type(value) is dict):
            print('dict')
        elif (type(value) is list):
            traverselist(conn, value, url)
        else:
            meta = metadata.get(key)
            print('meta_{}'.format(meta))
            if(meta is None):
                dict_json[str(i)] = value
                metadata[key] = i
                i += 1
            else:
                dict_json[str(meta)] = value
            
    print('dict json')
    # print(dict_json)
    return dict_json, i
#----------------------------------------------------------------------------#
# Launch.
#----------------------------------------------------------------------------#

if __name__ == '__main__':
    #app.debug = True;1
    app.run('127.0.0.1', 4000, True)
