from flask import Flask, render_template, url_for, request, json
from flask import make_response


STR_RESULT  =   'result'
STR_META    =   'meta'

def convert_json_to_tson(json_):

    response = {}
    metadata = {}
    unique_key = 0


    for key, values in json_.items():

        if type(values) == dict:

            print('dict')

        elif type(values) == list:

            meta = metadata.get(key)

            if(meta is None):

                response[str(unique_key)]=[]
                sub = unique_key
                metadata[key] = unique_key
                unique_key += 1

            else:

                response[str(meta)]=[]
                sub = meta

            list_json={}

            list_json, unique_key = traverselist(values, list_json, metadata, unique_key)

            response[str(sub)].extend(list_json)

        else:

            meta = metadata.get(key)
            print('meta_{}'.format(meta))

            if(meta is None):

                response[str(unique_key)] = values
                metadata[key] = unique_key
                unique_key += 1

            else:

                response[str(meta)] = values

    tson_response = {}

    tson_response[STR_RESULT] = response

    tson_response[STR_META] = swap_metadata(metadata)

    res = make_response(json.dumps(tson_response, ensure_ascii = False))

    res.headers["Content-Type"] = "application/json; charset=utf-8"

    return res, tson_response

def traversedic(dic, response, metadata, unique_key):

    dict_json = {}

    for key, value in dic.items():

        if (type(value) is dict):

            print('dict')

        elif (type(value) is list):

            traverselist(conn, value, url)

        else:

            print(key)
            meta = metadata.get(key)
            print('meta_{}'.format(meta))

            if(meta is None):

                dict_json[str(unique_key)] = value
                metadata[key] = unique_key
                unique_key += 1

            else:

                dict_json[str(meta)] = value

    # print('dict json')
    # print(dict_json)

    return dict_json, unique_key

def traverselist(listObj, response, metadata, unique_key):

    list_json=[]

    if len(listObj) > 0:

        for value in listObj:

            print ('list value')
            print (value)
            print ('---------')

            if(type(value) is dict):

                dict_json, unique_key = traversedic(value, response, metadata, unique_key)
                print(unique_key)
                list_json.append(dict_json)

                # print(list_json)
            else:

                print ("-" + str(value))
                print (type(value))

    return list_json, unique_key

def swap_metadata(metadata):

    meta_data = {}

    for key, value in metadata.items():

        meta_data[str(value)] = str(key)

    return meta_data

def convert_tson_to_json(tson):

    response = {}

    try:

        meta_data = tson[STR_META]
        print(meta_data)
        json_ = tson[STR_RESULT]

        for key, values in json_.items():

            if type(values) == dict:

                print('dict')

            elif type(values) == list:

                meta = meta_data.get(key)

                if(meta is not None):

                    response[str(meta)]=[]

                else:

                    raise KeyError(key)

                list_json = {}

                list_json = traverse_to_list(values, list_json, meta_data)

                response[str(meta)].extend(list_json)

            else:

                meta = meta_data.get(key)

                if(meta is not None):

                    response[str(meta)] = values

                else:

                    print('metadata not found for {}'.format(key))

        print(response)

        res = make_response(json.dumps(response, ensure_ascii = False))

        res.headers["Content-Type"] = "application/json; charset=utf-8"

        return res

    except KeyError as e:

        print(e)

        failure_response = {}

        failure_response['message'] = 'No Metadata or result object found for {}'.format(str(e))

        res = make_response(json.dumps(failure_response, ensure_ascii = False), 400)

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

    list_json = []

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