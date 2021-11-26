import json

def writeData(data:dict, name:str = 'data') -> None:
    with open('./mails/{}.json'.format(name), 'w',  encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=4)

def readData(name:str = 'data') -> dict:
    with open('./mails/{}.json'.format(name), 'r',  encoding='utf-8') as f:
        data = json.load(f)
    return data