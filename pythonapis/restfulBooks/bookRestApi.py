from flask import Flask, request, jsonify

app = Flask(__name__)

books = [
    {"id": 1, "title": "1984", "author": "George Orwell"},
    {"id": 2, "title": "To Kill a Mockingbird", "author": "Harper Lee"}
]

@app.route('/books', methods=['GET'])
def get_books():
    return jsonify(books)


@app.route('/books/<int:book_id>', methods=['GET'])
def get_book_by_id(book_id):
    book = next((book for book in books if book["id"] == book_id), None)
    if book:
        return jsonify(book)
    return jsonify({"error", "Book not found"}), 404

@app.route('/books', methods=['POST'])
def store_new_book():
    data = request.get_json()
    title = data.get("title")
    author = data.get("author")
    book = {"id": len(books)+1, "title": title, "author": author}
    books.append(book)
    return jsonify(book)

@app.route('/books/<int:book_id>', methods=['PUT'])
def update_book(book_id):
    book = next ((book for book in books if book["id"] == book_id), None)
    if not book:
        return jsonify({"error", "Book not found"}), 404

    data = request.get_json()
    book["title"] = data.get("title")
    book["author"] = data.get("author")

    return jsonify(book)

@app.route('/books/<int:book_id>', methods=['DELETE'])
def delete_book(book_id):
    book = next((book for book in books if book["id"] == book_id), None)
    if not book:
        return jsonify({"error", "Book not found"}), 404

    books.remove(book)
    return "Success", 200

if __name__ == '__main__':
    app.run(debug=True)