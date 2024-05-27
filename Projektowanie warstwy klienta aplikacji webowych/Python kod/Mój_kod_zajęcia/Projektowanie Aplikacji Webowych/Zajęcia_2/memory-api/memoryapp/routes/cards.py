from flask import jsonify, request
from sqlalchemy import exc

from memoryapp import app
from memoryapp.repository import *


@app.route('/categories/<int:category_id>/cards', methods=['GET'])
def cards(category_id):
    return jsonify(get_cards(category_id))
