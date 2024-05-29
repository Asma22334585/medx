from models import storage
from models.user import User
from api.views import app_views
from flask import (
                    jsonify,
                    make_response,
                    request,
                    abort
                    )


@app_views.route('/users', methods=['GET'], strict_slashes=False)
def get_all_users():
    """functions return a list of all the users"""
    all_users = storage.all(User).values()
    list_users = []

    for user in all_users:
        list_users.append(user.to_dict())
    return jsonify(list_users)

@app_views.route("/users/<user_id>", methods=['GET'], strict_slashes=False)
def get_user(user_id):
    """return the record of a particular user"""
    user = storage.get(User, user_id)
    if not user:
        abort(404)
    return jsonify(user.to_dict())

@app_views.route("/users", methods=['POST'], strict_slashes=False)
def post_user():
    """ creating a new user"""

    if not request.get_json():
        abort(400, description="NOT A JSON")

    if 'email' not in request.get_json():
        abort(400, description=("No email found"))
    
    user_data = request.get_json()
    new_user = User(**user_data)
    new_user.save()
    return (make_response(jsonify(new_user.to_dict()), 201))

@app_views.route("/users/<user_id>", methods=['PUT'], strict_slashes=False)
def update_user(user_id):
    """updates a user data"""
    user = storage.get(User, user_id)
    if not user:
        abort(404)
    
    if not request.get_json():
        abort(400, description="Not a valid format")
    
    data = request.get_json()

    ignore = ['id', 'email', 'created_at', 'update_at']

    for key, value in data.items():
        if key not in ignore:
            setattr(user, key, value)
    storage.save()
    return make_response(jsonify(user.to_dict()), 201)

@app_views.route('/users/<user_id>', methods=['DELETE'], strict_slashes=False)
def del_user(user_id):
    """delete a user"""
    user = storage.get(User, user_id)
    if not user:
        abort(400, description="user not found")
    
    storage.delete(user)
    storage.save()
    return make_response(jsonify({}), 200)