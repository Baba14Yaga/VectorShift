import json
def json_resolver(json_string):
    print(json_string,type(json_string))
    data_dict = json.loads(json_string)
    print(data_dict,type(data_dict))
    return data_dict
json_resolver("{\"state\": \"wdO_l9qtA5YzbbqmbFhMlF0tDU79WmifFGjsKOd6Vd8\", \"user_id\": \"TestUser\", \"org_id\": \"TestOrg\"}") 
