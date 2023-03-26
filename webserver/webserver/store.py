import requests

def get_categories():
    r = requests.get('https://api.escuelajs.co/api/vi/categories')
    print(r.status_code)
    print(r.text)
    print(type(r.text)) #Arroja el resultado de la peticion en formato str
    categories = r.json() #Transforma el resultado a formato json
    return categories

