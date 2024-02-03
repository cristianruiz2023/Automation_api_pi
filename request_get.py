

import requests


req = requests.get("https://jsonplaceholder.typicode.com/comments?postId=2")
"""Requerimiento de los post del postId=2"""
print("status get")
print(req.status_code)
"""Retorna el código del servidor"""
# print(req.content.decode("utf-8"))
"""Se le agrega .decode utf-8 para que sea legible"""
# print(req.text)
"""Se obtiene mismo resultado de forma mas simple"""
result = req.json()
"""ponemos el.json dentro de una variable para poder trabajar con el"""
# print(result)
"""retorna el array completo"""
print(result[0]['name'])
"""retorna el nombre del primer diccionario del array"""
