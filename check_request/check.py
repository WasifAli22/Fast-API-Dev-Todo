import requests

res = requests.get('http://localhost:8000/')
print(res.text)
print(res.status_code)
print(res.headers)
print(res.headers['content-type'])