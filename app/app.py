from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy
import config
from flask_migrate import Migrate

app = Flask('my_app')
app.config.from_mapping(SQLALCHEMY_DATABASE_URI=config.POSTGRE_URI)
db = SQLAlchemy(app)



# def base():
#     return jsonify({'statusik': 'ok'})
#
#
# def add_advertisement(data):
#     pass


# def advertisements():
#     method = request.method
#     if method == 'POST':
#         pass
#
#         add_advertisement(request.json)
#     elif method == 'GET':
#         pass
#         return jsonify()
#     elif method == 'PUT':
#         pass
#     elif method == 'DELETE':
#         pass
#     else:
#         response = jsonify({'data': 'Wrong method'})
#         response.status_code = 400
#         return response
#     if request.headers.get('token') == 'sasa':
#         return jsonify({'statusik': 'ok'})
#     else:
#         response = jsonify({'statusik': 'error'})
#         response.status_code = 401
#         return response

#
# app.run()
