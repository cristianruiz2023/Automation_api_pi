import requests

data = {'title':'Mi prueba',
        'body':'Este es el body de un blog cualquiera con su contenido',
        'userId':1
        }
req = requests.post("https://jsonplaceholder.typicode.com/posts",data=data)
print(f"respuesta en código del servidor : {req.status_code}")
