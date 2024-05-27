from flask import jsonify, request
from sqlalchemy import exc

from memoryapp import app
from memoryapp.repository import *


@app.route('/categories/<int:category_id>/cards', methods=['GET'])
def cards(category_id):
    return jsonify(get_cards(category_id))


@app.route('/categories/<int:category_id>/cards', methods=['POST'])
def add_card(category_id):
    request_body = request.json

    term = request_body['term']
    definition = request_body['definition']

    try:
        return jsonify(create_card(category_id, term, definition)), 201
    except exc.IntegrityError:
        return '', 404


@app.route('/categories/<int:category_id>/cards/<card_id>', methods=['DELETE'])
def remove_card(category_id, card_id):
    delete_card(category_id, card_id)

    return '', 204
