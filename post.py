import requests

data = {'title':'Mi prueba',
        'body':'Este es el body de un blog cualquiera con su contenido',
        'userId':1
        }
req = requests.post("https://jsonplaceholder.typicode.com/posts", data=data)
"""Se crea el post dentro del servidor """
print(f"respuesta en código del servidor : {req.status_code}")
"""Retorna el status code"""


req = requests.get("https://jsonplaceholder.typicode.com/posts")
"""Se listan los posts """
print(req.content)
"""se pide el contenido de la petición"""
print(f"respuesta en código del servidor : {req.status_code}")
"""se hace el requerimiento del status code"""
