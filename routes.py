from flask import Blueprint
from controller import get_books, add_book,get_book,update_book,delete_book



# Create the book_routes Blueprint
book_routes = Blueprint('book_routes', __name__)

# # Import the controller after defining the Blueprint
# from controller import book_controller

# Define the routes using the book_routes Blueprint
@book_routes.route('/books', methods=['GET'])
def get_books():
    return get_books()

@book_routes.route('/books', methods=['POST'])
def add_book():
    return add_book()

@book_routes.route('/books/<book_id>', methods=['GET'])
def get_book(book_id):
    return get_book(book_id)

@book_routes.route('/books/<book_id>', methods=['PUT'])
def update_book(book_id):
    return update_book(book_id)

@book_routes.route('/books/<book_id>', methods=['DELETE'])
def delete_book(book_id):
    return delete_book(book_id)