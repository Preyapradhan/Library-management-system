from flask import Flask, render_template, jsonify, request
import uuid
from functools import wraps

# Application initialization
app = Flask(__name__)

# Mock databases (books and members)
from models.books import books, add_book, get_book, update_book, delete_book
from models.member import member, add_member, get_member, update_member, delete_member

# Tokens for simple token-based authentication
tokens = {"admin": "12345"}

# Helper functions
def generate_id():
    return str(uuid.uuid4())[:8]

def token_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        token = request.headers.get('Authorization')
        if not token or token not in tokens.values():
            return jsonify({"message": "Unauthorized access"}), 403
        return f(*args, **kwargs)
    return decorated

def paginate(items, page, per_page):
    start = (page - 1) * per_page
    end = start + per_page
    return list(items.values())[start:end]

def search_items(items, query, keys):
    return {k: v for k, v in items.items() if any(query.lower() in v[key].lower() for key in keys)}

# Routes
@app.route('/')
def home():
    return render_template('index.html')

# Books Endpoints
@app.route('/books', methods=['GET'])
def get_books():
    query = request.args.get('search', '')
    page = int(request.args.get('page', 1))
    per_page = int(request.args.get('per_page', 5))

    # Filter and paginate books
    filtered_books = search_items(books, query, ['title', 'author']) if query else books
    paginated_books = paginate(filtered_books, page, per_page)

    return jsonify(paginated_books)

@app.route('/books/<string:book_id>', methods=['GET'])
def get_book(book_id):
    book = get_book(book_id)
    if not book:
        return jsonify({"message": "Book not found"}), 404
    return jsonify(book)

@app.route('/books', methods=['POST'])
@token_required
def add_book():
    data = request.json
    book_id = generate_id()
    book_data = {
        "id": book_id,
        "title": data['title'],
        "author": data['author'],
        "published_date": data['published_date'],
        "category": data['category'],
        "copies_available": data['copies_available']
    }
    add_book(book_id, book_data)
    return jsonify({"message": "Book added", "book": book_data}), 201

@app.route('/books/<string:book_id>', methods=['PUT'])
@token_required
def update_book(book_id):
    data = request.json
    if not get_book(book_id):
        return jsonify({"message": "Book not found"}), 404
    update_book(book_id, data)
    return jsonify({"message": "Book updated", "book": get_book(book_id)})

@app.route('/books/<string:book_id>', methods=['DELETE'])
@token_required
def delete_book(book_id):
    if not get_book(book_id):
        return jsonify({"message": "Book not found"}), 404
    delete_book(book_id)
    return jsonify({"message": "Book deleted"})

# Members Endpoints
@app.route('/members', methods=['GET'])
def get_members():
    query = request.args.get('search', '')
    page = int(request.args.get('page', 1))
    per_page = int(request.args.get('per_page', 5))

    # Filter and paginate members
    filtered_members = search_items(member, query, keys=['name', 'email']) if query else member
    paginated_members = paginate(filtered_members, page, per_page)

    return jsonify(paginated_members)

@app.route('/members/<string:member_id>', methods=['GET'])
def get_member(member_id):
    member = get_member(member_id)
    if not member:
        return jsonify({"message": "Member not found"}), 404
    return jsonify(member)

@app.route('/members', methods=['POST'])
@token_required
def add_member():
    data = request.json
    member_id = generate_id()
    member_data = {
        "id": member_id,
        "name": data['name'],
        "email": data['email'],
        "join_date": data['join_date']
    }
    add_member(member_id, member_data)
    return jsonify({"message": "Member added", "member": member_data}), 201

@app.route('/members/<string:member_id>', methods=['PUT'])
@token_required
def update_member(member_id):
    data = request.json
    if not get_member(member_id):
        return jsonify({"message": "Member not found"}), 404
    update_member(member_id, data)
    return jsonify({"message": "Member updated", "member": get_member(member_id)})

@app.route('/members/<string:member_id>', methods=['DELETE'])
@token_required
def delete_member(member_id):
    if not get_member(member_id):
        return jsonify({"message": "Member not found"}), 404
    delete_member(member_id)
    return jsonify({"message": "Member deleted"})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
