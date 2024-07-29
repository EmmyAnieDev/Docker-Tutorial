from flask import Flask, jsonify
from api.routes import api_bp

app = Flask(__name__)

app.register_blueprint(api_bp, url_prefix='/api')


@app.route('/', methods=['GET'])
def get_books():
    return jsonify('welcome to my docker app.')


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=4000, debug=True)