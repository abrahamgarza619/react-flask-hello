"""
This module takes care of starting the API Server, Loading the DB and Adding the endpoints
"""
from flask import Flask, request, jsonify, url_for, Blueprint
from api.models import db, User, Planets
from api.utils import generate_sitemap, APIException

api = Blueprint('api', __name__)

# user

@api.route('/user', methods=['POST'])
def create_user():
    request_body = request.get_json()
    new_user = User(
        first_name = request_body['first_name'],
        last_name = request_body['last_name'],
        email = request_body['email'],
        password = request_body['password'],
        is_active = True
    )
    db.session.add(new_user)
    db.session.commit()
    return f"A new user has been added! {request_body['email']}"

@api.route('/user', methods=['GET'])
def get_users():
    allUsers = User.query.all()
    user_list = list(map(lambda x: x.serialize(), allUsers))
    return jsonify(user_list, 200)

@api.route('/user/<int:user_id>', methods=['DELETE'])
def delete_user(user_id):
    user = User.query.get(user_id)
    if user is None:
        raise APIException("User not found!", status_code=405)
        db.session.delete(user)
    db.session.delte(user)
    db.session.commit()
    return f"A user has been deleted! {user.email}"

@api.route('/user/<int:user_id>', methods=['PUT'])
def update_user(user_id):
    request_body = request.get_json()
    user = User.query.get(user_id)
    if user is None:
        raise APIException("User not found!", status_code=405)
    if "email" in request_body:
        user.email = request_body['email']
    if 'first_name' in request_body:
        user.first_name = request_body['first_name']
    db.session.commit()
    return jsonify(user.serialize()), 200

#planet 

@api.route('/planet', methods=['POST'])
def create_planet():
    request_body = request.get_json()
    planet = Planets(
        name = request_body['name'],
        terrain = request_body['terrain'],
        population = request_body['population'],
        climate = request_body['climate']
    )
    db.session.add(planet)
    db.session.commit()
    return f"A new planet has been added! {request_body['name']}"


@api.route('/planet', methods=['GET'])
def get_planets():
    allPlanets = Planets.query.all()
    planet_list = list(map(lambda x: x.serialize(), allPlanets))
    return jsonify(planet_list, 200)

@api.route('/planet', methods=['PUT'])
def update_planet(user_id):
    request_body = request.get_json()
    planet = Planet.query.get(user_id) 
    if planet is None:
        raise APIException("Planet not found!", status_code=405)
    if "terrain" in request_body:
        planet.terrain = request_body['terrain']
    if 'population' in request_body:
        planet.population = request_body['population']
    if 'name' in request_body:
        planet.name = request_body['name']
    db.session.commit()
    return jsonify(planet.serialize()), 200    

@api.route('/planet/<int:user_id>', methods=['DELETE'])
def delete_planet(user_id):
    planet = Planets.query.get(user_id)
    if planet is None:
        raise APIException("User not found!", status_code=405)
    db.session.delete(planet)
    db.session.commit()
    return f"A planet has been deleted! {planet.name}"

