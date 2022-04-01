import requests

result = requests.get("http://127.0.0.1:8888/api/books/1")      #valid
print(result.json())
result = requests.get("http://127.0.0.1:8888/api/books/7")      #invalid
print(result.json())

result = requests.delete("http://127.0.0.1:8888/api/books/2")     #valid
print(result.json())
result = requests.delete("http://127.0.0.1:8888/api/books/100")     #invalid
print(result.json())

result = requests.post("http://127.0.0.1:8888/api/books/6", json={"name": "1984", "author": "George Orwell"})     #valid
result = requests.post("http://127.0.0.1:8888/api/books/7", json={"name": "Brave New World", "author": "Aldous Huxley"})     #valid
print(result.json())

result = requests.put("http://127.0.0.1:8888/api/books/6", json={"name": "The Great Gatsby", "author": "Francis Scott Key Fitzgerald"})     #valid
print(result.json())
result = requests.put("http://127.0.0.1:8888/api/books/2", json={"name": "Breakfast at Tiffany's", "author": "Truman Garcia Capote"})     #invalid
print(result.json())