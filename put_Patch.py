import requests

data = {'id':1,
        'title':'Mi prueba',
        'body':'Este es el body de un blog cualquiera con su contenido',
        'userId':1
        }

req = requests.put("https://jsonplaceholder.typicode.com/posts/5",data=data)
"""put modifica el objeto completo los 4 parámetros """
print(f"status code de put {req.status_code}")

mod = {'title':'HolaMundo'}
req = requests.patch("https://jsonplaceholder.typicode.com/posts/5",data=mod)
"""patch modifica un elemento del objeto en particular"""
print(f"status code de patch {req.status_code}")
