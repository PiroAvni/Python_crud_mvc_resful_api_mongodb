from flask import Flask
from flask_pymongo import PyMongo
from routes import book_routes
from controller import initialize_app

app = Flask(__name__)
app.config['MONGO_URI'] = 'mongodb://localhost:27017/mydatabase'
mongo = PyMongo(app)

initialize_app(app)

# Register the book_routes Blueprint
app.register_blueprint(book_routes)

if __name__ == '__main__':
    app.run(debug=True, port=8000)




