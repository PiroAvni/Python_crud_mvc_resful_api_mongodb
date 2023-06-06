from flask import Flask
from flask_cors import CORS
from flask_pymongo import PyMongo
from routes import book_routes

app = Flask(__name__)

# Enable CORS
CORS(app)

# Register the book_routes Blueprint
app.register_blueprint(book_routes)

app.config['MONGO_URI'] = 'mongodb://localhost:27017/mydatabase'
mongo = PyMongo(app)