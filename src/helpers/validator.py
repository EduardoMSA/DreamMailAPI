from datetime import datetime
import re
from urllib.request import urlopen

def validateInternetConnection() -> bool:
    try:
        response = urlopen('https://www.google.com/', timeout=10)
        return True
    except: 
        return False


def validateDate(date:str) -> bool:
    try:
        datetime.strptime(date, '%d-%b-%Y').date()
    except ValueError:
        return False
    
    return True

def validateEmail(email:str) -> bool:
    if re.match(r"(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)",email):
        return True
    return False

def validateNewsDate(date:str) -> bool:
    try:
        datetime.strptime(date, '%Y-%m-%d').date()
    except ValueError:
        return False
    
    return True

def validateLanguage(lang:str) -> bool:
    if lang in ['ar','de','en','es','fr','he','it','nl','no','pt','ru','se','ud','zh']:
        return True
    return False

def validateNewsSources(sources:list) -> bool:
    for source in sources:
        if type(source) != str:
            return False
        if not re.match(r"(^[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)",source):
            return False
    return True