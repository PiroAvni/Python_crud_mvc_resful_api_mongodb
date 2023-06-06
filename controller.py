from flask import Flask, jsonify, request
from flask_pymongo import PyMongo
from models import Book
from app import app

mongo = PyMongo(app)

def get_books():
    books = mongo.db.books.find()
    results = [book.serialize() for book in books]
    return jsonify(results)



def add_book():
    data = request.get_json()
    title = data['title']
    author = data['author']
    book = Book(title, author)
    mongo.db.books.insert_one(book.serialize())
    return jsonify({'message': 'Book added successfully'})



def get_book(book_id):
    book = mongo.db.books.find_one({'_id': book_id})
    if book is None:
        return jsonify({'message': 'Book not found'})
    book_data = Book(book['title'], book['author']).serialize()
    return jsonify(book_data)



def update_book(book_id):
    book = mongo.db.books.find_one({'_id': book_id})
    if book is None:
        return jsonify({'message': 'Book not found'})
    data = request.get_json()
    book['title'] = data['title']
    book['author'] = data['author']
    mongo.db.books.update_one({'_id': book_id}, {'$set': book})
    return jsonify({'message': 'Book updated successfully'})



def delete_book(book_id):
    book = mongo.db.books.find_one({'_id': book_id})
    if book is None:
        return jsonify({'message': 'Book not found'})
    mongo.db.books.delete_one({'_id': book_id})
    return jsonify({'message': 'Book deleted successfully'})


if __name__ == '__main__':
    app.run(debug=True,port=8000)