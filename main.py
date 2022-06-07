import json

data = []

for x in range(2):
    f = open(f'data/data_{x+1}.json')
    file = json.load(f)
    file = file['message']
    data.append(file)
    f.close()

def get_type(attr):

    # function that returns the type of an attribute
    if (type(attr) == list) and (len(attr) > 0):
        if type(attr[0]) == str:
            return 'enum'
        elif type(attr[0]) == dict:
            return 'array'
    elif type(attr) == str:
        return 'string'
    elif type(attr) == int:
        return 'integer'
    else:
        return 'undefined type'


def main(data):

    result = {}
    for key, value in data.items():
        if isinstance(value, dict):
            new_dict = {}
            for k, v in value.items():
                new_dict[k] = {
                    "type": get_type(v),
                    "tag": "",
                    "description": "",
                    "required": False
                }
            
            new_dict.update({
                "type": 'object',
                "tag": "",
                "description": "",
                "required": False
            })
            result[key] = new_dict

        else:
            result[key] = {
                "type": get_type(value),
                "tag": "",
                "description": "",
                "required": False
            }

    
    return result


if __name__ == '__main__':
    for i in range(len(data)):
        file = main(data=data[i])
        file = json.dumps(file, indent=4)
        w = open(f'schema/schema_{i+1}.json', "w")
        w.write(file)
        w.close()