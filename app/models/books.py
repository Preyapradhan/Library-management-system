books = {
    "1": {
        "id": "1",
        "title": "The Catcher in the Rye",
        "author": "J.D. Salinger",
        "published_date": "1951-07-16",
        "category": "Fiction",
        "copies_available": 5,
        "image": "/static/images/the-catcher-in-the-rye.jpg"
    },
    "2": {
        "id": "2",
        "title": "To Kill a Mockingbird",
        "author": "Harper Lee",
        "published_date": "1960-07-11",
        "category": "Fiction",
        "copies_available": 3,
        "image": "/static/images/images.jpg"
    },
    "3": {
        "id": "3",
        "title": "1984",
        "author": "George Orwell",
        "published_date": "1949-06-08",
        "category": "Dystopian",
        "copies_available": 4,
        "image": "/static/images/1984.jpg"
    },
    "4": {
        "id": "4",
        "title": "The Great Gatsby",
        "author": "F. Scott Fitzgerald",
        "published_date": "1925-04-10",
        "category": "Fiction",
        "copies_available": 2,
        "image": "/static/images/the-great-gatsby.jpg"
    }
}

def add_book(book_id, data):
    books[book_id] = data

def get_book(book_id):
    return books.get(book_id)

def update_book(book_id, data):
    if book_id in books:
        books[book_id].update(data)

def delete_book(book_id):
    if book_id in books:
        del books[book_id]
