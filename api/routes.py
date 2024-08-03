from flask import Blueprint, jsonify


api_bp = Blueprint('api', __name__)


books = [
    {'id': 1, 'title': 'The Catcher in the Rye'},
    {'id': 2, 'title': 'To Kill a Mockingbird'},
    {'id': 3, 'title': '1984'},
    {'id': 4, 'title': 'The Great Gatsby'},
    {'id': 4, 'title': 'System Design'},
    {'id': 5, 'title': 'Moby Dick'}
]


@api_bp.route('/books', methods=['GET'])
def get_books():
    return jsonify(books)