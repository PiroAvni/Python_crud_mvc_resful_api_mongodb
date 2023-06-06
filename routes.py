from flask import Blueprint
from controllers import book_controller

# Create a Blueprint object for the routes
book_routes = Blueprint('book_routes', __name__)

# Define the routes and map them to the corresponding controller functions
book_routes.route('/books', methods=['GET'])(book_controller.get_books)
book_routes.route('/books', methods=['POST'])(book_controller.add_book)
book_routes.route('/books/<book_id>', methods=['GET'])(book_controller.get_book)
book_routes.route('/books/<book_id>', methods=['PUT'])(book_controller.update_book)
book_routes.route('/books/<book_id>', methods=['DELETE'])(book_controller.delete_book)