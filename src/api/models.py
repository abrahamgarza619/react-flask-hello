from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

db.metadata.clear()

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(20), nullable=False)
    last_name = db.Column(db.String(20), nullable=False)
    email = db.Column(db.String(200), unique=True, nullable=False)
    password = db.Column(db.String(200), nullable=False)
    salt = db.Column(db.String(200), nullable=False)
    is_active = db.Column(db.Boolean(), nullable=False)
    child = db.relationship('Favorite', backref='parent', uselist=False)

    def __repr__(self):
        return f'<User {self.email}>'

    def serialize(self):
        return {
            "id": self.id,
            "first_name": self.first_name,
            "last_name": self.last_name,
            "email": self.email,
            "is_active": self.is_active
            # do not serialize the password, its a security breach
        }

# planets

class Planets(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(20), unique=True, nullable=False)
    rotation_period = db.Column(db.String(20), unique=True, nullable=False)
    orbital_period = db.Column(db.String(20), unique=True, nullable=False)
    climate = db.Column(db.String(20), nullable=False)
    terrain = db.Column(db.String(20), nullable=False)
    population = db.Column(db.String(20), nullable=False)

    def serialize(self):
        return {
            "id": self.id,
            "name": self.name,
            "rotation_period": self.rotation_period,
            "orbital_period": self.orbital_period,
            "climate": self.climate,
            "terrain": self.terrain,
            "population": self.population
        }

class People(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(20), nullable=False)
    height = db.Column(db.String(20), nullable=False)
    mass = db.Column(db.String(20), nullable=False)
    hair_color = db.Column(db.String(20), nullable=False)
    skin_color = db.Column(db.String(20), nullable=False)
    eye_color = db.Column(db.String(20), nullable=False)
    birth_year = db.Column(db.String(20), nullable=False)
    gender = db.Column(db.String(20), nullable=False)

    def serialize(self):
        return {
            "id": self.id,
            "name": self.name,
            "height": self.height,
            "mass": self.mass,
            "hair_color": self.hair_color,
            "skin_color": self.skin_color,
            "eye_color": self.eye_color,
            "birth_year": self.birth_year,
            "gender": self.gender
        }

# favorites model

class Favorite(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    person = db.Column(db.String(20), nullable=False)
    planet = db.Column(db.String(20), nullable=False)

    def serialize(self):
        return {
            "id": self.id,
            "person": self.person,
            "planet": self.planet
        }



class Favorite(db.Model):
    __table_args__ = {'extend_existing': True}
    id = db.Column(db.Integer, primary_key=True)
    person = db.Column(db.String(20), nullable=False)
    planet = db.Column(db.String(20), nullable=False)
    parent_id = db.Column(db.Integer, db.ForeignKey("user.id"))

    def serialize(self):
        return {
            "id": self.id,
            "person": self.person,
            "planet": self.planet,
            "parent_id": self.parent_id
        }

 