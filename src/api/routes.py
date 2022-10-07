"""
This module takes care of starting the API Server, Loading the DB and Adding the endpoints
"""
from flask import Flask, request, jsonify, url_for, Blueprint
from api.models import db, User, Planets, People
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

@api.route('/planet', methods=['POST'])
def create_planet():
    request_body = request.get_json()
    planet = Planets(
        name = request_body['name'],
        rotation_period = request_body['rotation_period'],
        orbital_period = request_body['orbital_period'],
        climate = request_body['climate'],
        terrain = request_body['terrain'],
        population = request_body['population']
    )
    db.session.add(planet)
    db.session.commit()
    return f"A new planet has been added! {request_body['name']}"


@api.route('/planet', methods=['GET'])
def get_planets():
    allPlanets = Planets.query.all()
    planet_list = list(map(lambda x: x.serialize(), allPlanets))
    return jsonify(planet_list, 200)

@api.route('/planet/<int:planet_id>', methods=['GET'])
def get_planet(planet_id):
    request_body = request.get_json()
    planet = Planets.query.get(planet_id)
    return jsonify(planet.serialize()), 200  

@api.route('/planet/<int:planet_id>', methods=['PUT'])
def update_planet(planet_id):
    request_body = request.get_json()
    planet = Planets.query.get(planet_id) 
    if planet is None:
        raise APIException("Planet not found!", status_code=405)
    if "name" in request_body:
        planet.name = request_body['name']
    if 'rotation_period' in request_body:
        planet.rotation_period = request_body['rotation_period']
    if 'orbital_period' in request_body:
        planet.orbital_period = request_body['orbital_period']
    if 'climate' in request_body:
        planet.climate = request_body['climate']
    if 'terrain' in request_body:
        planet.terrain = request_body['terrain']
    if 'population' in request_body:
        planet.population = request_body['population']
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

# people

@api.route('/people', methods=['POST'])
def create_person():
    request_body = request.get_json()
    person = People(
        name = request_body['name'],
        height = request_body['height'],
        mass = request_body['mass'],
        hair_color = request_body['hair_color'],
        skin_color = request_body['skin_color'],
        eye_color = request_body['eye_color'],
        birth_year = request_body['birth_year'],
        gender = request_body['gender'],
    )
    db.session.add(person)
    db.session.commit()
    return f"A new person has been added! {request_body['name']}"

@api.route('/people', methods=['GET'])
def get_people():
    allPeople = People.query.all()
    people_list = list(map(lambda x: x.serialize(), allPeople))
    return jsonify(people_list, 200)

@api.route('/people/<int:person_id>', methods=['GET'])
def get_person(person_id):
    request_body = request.get_json()
    person = People.query.get(person_id)
    return jsonify(person.serialize()), 200  

@api.route('/people/<int:person_id>', methods=['PUT'])
def update_person(person_id):
    request_body = request.get_json()
    person = People.query.get(person_id) 
    if person is None:
        raise APIException("Person not found!", status_code=405)
    if "name" in request_body:
        person.name = request_body['name']
    if 'height' in request_body:
        person.height = request_body['height']
    if 'mass' in request_body:
        person.mass = request_body['mass']
    if 'hair_color' in request_body:
        person.hair_color = request_body['hair_color']
    if 'skin_color' in request_body:
        person.skin_color = request_body['skin_color']
    if 'eye_color' in request_body:
        person.eye_color = request_body['eye_color']
    if 'birth_year' in request_body:
        person.birth_year = request_body['birth_year']
    if 'gender' in request_body:
        person.gender = request_body['gender']
    db.session.commit()
    return jsonify(person.serialize()), 200    

@api.route('/people/<int:person_id>', methods=['DELETE'])
def delete_person(person_id):
    person = People.query.get(person_id)
    if person is None:
        raise APIException("Person not found!", status_code=405)
    db.session.delete(person)
    db.session.commit()
    return f"A person has been deleted! {person.name}"

