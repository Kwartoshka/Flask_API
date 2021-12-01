from flask import jsonify, request
from flask.views import MethodView

from app import app, db
from models import User, Advertisement
from schema import USER_CREATE, ADVERTISEMENT_CREATE, ADVERTISEMENT_PUT, ADVERTISEMENT_PATCH
from validator import validate


class UserView(MethodView):

    def get(self, user_id):
        user = User.by_id(user_id)
        return jsonify(user.to_dict())

    @validate('json', USER_CREATE)
    def post(self):
        user = User(**request.json)
        user.set_password(request.json['password'])
        user.add()
        return jsonify(user.to_dict())


class AdvertisementView(MethodView):


    def get(self, advertisement_id):
        advertisement = Advertisement.by_id(advertisement_id)
        return jsonify(advertisement.to_dict())

    @validate('json', ADVERTISEMENT_CREATE)
    def post(self):
        advertisement = Advertisement(**request.json)
        advertisement.add()
        advertisement_dict = advertisement.to_dict()
        advertisement_dict['STATUS'] = 'CREATED'
        return jsonify(advertisement_dict)

    @validate('json', ADVERTISEMENT_PUT)
    def put(self, advertisement_id):
        Advertisement.update(advertisement_id, request.json)
        advertisement = Advertisement.by_id(advertisement_id)
        advertisement_dict = advertisement.to_dict()
        advertisement_dict['STATUS'] = 'FULLY_UPDATED'
        return jsonify(advertisement_dict)

    @validate('json', ADVERTISEMENT_PATCH)
    def patch(self, advertisement_id):
        Advertisement.update(advertisement_id, request.json)
        advertisement = Advertisement.by_id(advertisement_id)
        advertisement_dict = advertisement.to_dict()
        advertisement_dict['STATUS'] = 'PARTIALLY_UPDATED'
        return jsonify(advertisement_dict)

    def delete(self, advertisement_id):
        advertisement = Advertisement.by_id(advertisement_id)
        advertisement.delete_instance()
        advertisement_dict = advertisement.to_dict()
        advertisement_dict['STATUS'] = 'DELETED'
        return jsonify(advertisement_dict)


@app.route('/health/', methods=['GET', ])
def health():
    if request.method == 'GET':
        return jsonify({'status': 'OK'})

    return {'status': 'OK'}


app.add_url_rule('/users/<int:user_id>', view_func=UserView.as_view('users_get'), methods=['GET', ])
app.add_url_rule('/users/', view_func=UserView.as_view('users_create'), methods=['POST', ])
app.add_url_rule('/advertisements/', view_func=AdvertisementView.as_view('Advertisement_create'), methods=['POST', ])
app.add_url_rule('/advertisements/<int:advertisement_id>', view_func=AdvertisementView.as_view('advertisements'),
                 methods=['GET', 'PUT', 'PATCH', 'DELETE'])
