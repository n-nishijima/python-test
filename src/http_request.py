import requests

url="http://ecareerjs.jp/selections/direct"
response=requests.get(url)

print(response.text) 
