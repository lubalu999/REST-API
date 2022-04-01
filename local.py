import requests
from main import *

str_req = "http://127.0.0.1:" + str(port_) + "/api/books/"
result = requests.get(str_req + "1")      #valid
print(result.json())
result = requests.get(str_req + "7")      #invalid
print(result.json())

result = requests.delete(str_req + "2")         #valid
print(result.json())
result = requests.delete(str_req + "100")       #invalid
print(result.json())

result = requests.post(str_req + "6", json={"name": "1984", "author": "George Orwell"})                 #valid
result = requests.post(str_req + "7", json={"name": "Brave New World", "author": "Aldous Huxley"})      #valid
result = requests.post(str_req + "1", json={"name": "Pride and Prejudice", "author": "Jane Austen"})    #update
print(result.json())

result = requests.put(str_req + "6", json={"name": "The Great Gatsby", "author": "Francis Scott Key Fitzgerald"})     #valid
print(result.json())
result = requests.put(str_req + "2", json={"name": "Breakfast at Tiffany's", "author": "Truman Garcia Capote"})     #invalid
print(result.json())