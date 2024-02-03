

import requests

req = requests.delete("https://jsonplaceholder.typicode.com/posts/1")
print(req.status_code)