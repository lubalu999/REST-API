from flask import Flask
from flask_restful import Api, Resource, reqparse

books = {
    1: {"name": "Harry Potter", "author": "Joanne Rowling"},
    2: {"name": "Gone with the Wind", "author": "Margaret Mitchell"},
    3: {"name": "Death on the Nile", "author": "Agatha Mary Clarissa"},
    4: {"name": "The Green Mile", "author": "Stephen King"},
    5: {"name": "1408", "author": "Stephen King"}
}

class Main(Resource):
    def get(self, id_book):
        if id_book not in books:
            return books
        else:
            return books[id_book]

    def delete(self, id_book):
        if id_book not in books:
            return "You entered invalid id_book!"
        else:
            del books[id_book]
            return books

    def post(self, id_book):
        parser = reqparse.RequestParser()
        parser.add_argument("name", type = str)
        parser.add_argument("author", type = str)
        books[id_book] = parser.parse_args()
        return books

    def put(self, id_book):
        if id_book in books:
            parser = reqparse.RequestParser()
            parser.add_argument("name", type = str)
            parser.add_argument("author", type = str)
            books[id_book] = parser.parse_args()
            return books
        else:
            return "You entered invalid id_book!"


app = Flask("__name__")
api = Api()
api.add_resource(Main, "/api/books/<int:id_book>")
api.init_app(app)
port_ = 2222

if __name__ == "__main__":
    app.run(debug = True, port = port_, host = "127.0.0.1")

