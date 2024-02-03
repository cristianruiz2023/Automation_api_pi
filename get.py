

import requests

# req = requests.get("https://jsonplaceholder.typicode.com/posts/1")
# print("status: del get ")
# print(req.status_code)
# print(req.content)
# data = {'title':'prueba','body':'loren ipsun','userId':1}
# req = requests.post("https://jsonplaceholder.typicode.com/posts/",{'title':'prueba','body':'loren ipsun','userId':1})
# print("status: de la creación de post")
# print(req.status_code)


req = requests.get("https://jsonplaceholder.typicode.com/posts/1")
"""Obtiene la información de un post específico utilizando el servicio JSONPlaceholder."""
print("status: del get ")
print(req.status_code)
"""se requiere el status code"""
print(req.content)
"""devuelve el contenido del GET"""

data = {'title': 'prueba', 'body': 'loren ipsun', 'userId': 1}
"""se crea un diccionario para usar como data de ejemplo"""
req = requests.post("https://jsonplaceholder.typicode.com/posts/", data=data)
"""se crea el post en base al diccionario"""
print("status: de la creación de post")
print(req.status_code)
"""Se requiere devuelva el status code"""

req = requests.head("https://jsonplaceholder.typicode.com/posts/1")
"""Se solicita el head """
print("status code head: ")
print(req.status_code)
"""Se solicita el status code de la petición de HEAD"""
print("content head:")
print(req.content)
"""Se solicita el contenido de HEAD"""