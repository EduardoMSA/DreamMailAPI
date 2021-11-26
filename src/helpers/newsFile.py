import json

def readSources() -> str:
    with open('./news/sources.txt', 'r') as f:
        data = f.read()
    return data

def writeSources(sources_list:list) -> None:
    sources=','.join(sources_list)
    with open('./news/sources.txt', 'w') as f:
        f.write(sources)

def writeData(data:dict) -> None:
    with open('./news/articles.json', 'w',  encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=4)

def readData() -> dict:
    with open('./news/articles.json', 'r',  encoding='utf-8') as f:
        data = json.load(f)
    return data