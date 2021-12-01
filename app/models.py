import hashlib
from sqlalchemy import exc
import config
import errors
from app import db
# from flask_sqlalchemy import SQLAlchemy
from datetime import date


class BaseModelMixin:

    @classmethod
    def by_id(cls, instance_id):
        instance = cls.query.get(instance_id)
        if instance:
            return instance
        else:
            raise errors.NotFound

    def add(self):
        db.session.add(self)
        try:
            db.session.commit()
        except exc.IntegrityError:
            raise errors.WrongData

    def update(instance_id, params):
        db.session.query(Advertisement).filter(Advertisement.id == instance_id).update(params)
        try:
            db.session.commit()
        except exc.IntegrityError:
            raise errors.WrongData

    def delete_instance(self):
        db.session.delete(self)
        try:
            db.session.commit()
        except exc.IntegrityError:
            raise errors.WrongData



class User (db.Model, BaseModelMixin):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String, nullable=False, unique=True)
    password = db.Column(db.String, nullable=False)
    adverts = db.relation('Advertisement', backref='owner')

    def __str__(self):
        return f'User {self.email}'

    def __repr__(self):
        return str(self)

    def set_password(self, raw_password: str):
        raw_password = f'{raw_password}{config.SALT}'
        self.password = hashlib.md5(raw_password.encode()).hexdigest()

    def check_password(self, raw_password: str):
        raw_password = f'{raw_password}{config.SALT}'
        return self.password == hashlib.md5(raw_password.encode()).hexdigest()

    def to_dict(self):
        user_dict = {
            'id': self.id,
            'email': self.email
        }
        return user_dict


class Advertisement(db.Model, BaseModelMixin):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String, nullable=False)
    creation_date = db.Column(db.DateTime, default=date.today(), nullable=False)
    owner_id = db.Column(db.Integer, db.ForeignKey(User.id), nullable=False)

    def __str__(self):
        return f'Advrt {self.title} by {self.owner_id.email}'

    def to_dict(self):
        owner = User.by_id(self.owner_id)
        print(owner)
        advertisement_dict = {
            'id': self.id,
            'title': self.title,
            'creation_date': self.creation_date,
            'published_by': owner.to_dict()
        }
        return advertisement_dict

    def to_raw_dict(self):
        owner = User.by_id(self.owner_id)
        print(owner)
        advertisement_dict = {
            'id': self.id,
            'title': self.title,
            'creation_date': self.creation_date,
            'owner_id': self.owner_id
        }
        return advertisement_dict
