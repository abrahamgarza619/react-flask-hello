"""
This module takes care of starting the API Server, Loading the DB and Adding the endpoints
"""
from flask import Flask, request, jsonify, url_for, Blueprint
from api.models import db, User, Planets
from api.utils import generate_sitemap, APIException

api = Blueprint('api', __name__)


@api.route('/user', methods=['POST'])
def create_user():
    request_body = request.get_json()
    new_user = User(
        first_name = request_body['first_name'],
        last_name = request_body['last_name'],
        email = response_body['email'],
        password = response_body['password'],
        is_active = True
    )
    db.session.add(new_user)
    db.session.commit()
    return f"A new user has been created! {request_body['email']}"



    return jsonify(response_body), 200

@api.route('/planet', methods=['POST'])
def create_Planet():
    request_body = request.get_json()

