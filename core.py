from flask import Flask, render_template, url_for, request, json
from flask import make_response


def convert_json_to_tson(json_):
    response = {}
    metadata = {}
    i = 0
    for key, values in json_.items():
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
    tson_response = {}
    tson_response['result'] = response
    tson_response['meta'] = swap_metadata(metadata)
    res = make_response(json.dumps(tson_response, ensure_ascii=False))
    res.headers["Content-Type"] = "application/json; charset=utf-8"
    print(res)
    return res

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
    # print('dict json')
    # print(dict_json)
    return dict_json, i

def traverselist(listObj, response, metadata, i):
    list_json=[]
    if len(listObj) > 0:
        for value in listObj:
            print ('list value')
            print (value)
            print ('---------')
            if(type(value) is dict):
                dict_json, i = traversedic(value, response, metadata, i)
                print(i)
                list_json.append(dict_json)
                # print('list json')
                # print(list_json)
            else:
                print ("-" + str(value))
                print (type(value))
    return list_json

def swap_metadata(metadata):
    meta_data={}
    for key, value in metadata.items():
        meta_data[str(value)] = str(key)
    return meta_data

def convert_tson_to_json(tson):
    response = {}
    try:
        meta_data = tson['meta']
        print(meta_data)
        json_ = tson['result']
        for key, values in json_.items():
            if type(values) == dict:
                print('dict')
            elif type(values) == list:
                meta = meta_data.get(key)
                if(meta is not None):
                    response[str(meta)]=[]
                else:
                    raise KeyError(key)
                list_json={}
                list_json = traverse_to_list(values, list_json, meta_data)
                response[str(meta)].extend(list_json)
            else:
                meta = meta_data.get(key)
                if(meta is not None):
                    response[str(meta)] = values
                else:
                    print('metadata not found for {}'.format(key))
        print(response)
        res = make_response(json.dumps(response, ensure_ascii=False))
        res.headers["Content-Type"] = "application/json; charset=utf-8"
        return res
    except KeyError as e:
        print(e)
        failure_response = {}
        failure_response['message'] = 'No Metadata or result object found for {}'.format(str(e))
        res = make_response(json.dumps(failure_response, ensure_ascii=False), 400)
        res.headers["Content-Type"] = "application/json; charset=utf-8"
        return res


def traverse_to_dic(dic, response, metadata):
    dict_json = {}
    for key, value in dic.items():
        if (type(value) is dict):
            print('dict')
        elif (type(value) is list):
            traverselist(conn, value, url)
        else:
            meta = metadata.get(key)
            if(meta is not None):
                dict_json[str(meta)] = value
            else:
                print('metadata not found for {}'.format(key))
    return dict_json

def traverse_to_list(listObj, response, metadata):
    list_json=[]
    if len(listObj) > 0:
        for value in listObj:
            print ('list value')
            print (value)
            print ('---------')
            if(type(value) is dict):
                dict_json= traverse_to_dic(value, response, metadata)
                list_json.append(dict_json)
            else:
                print ("-" + str(value))
                print (type(value))
    return list_json