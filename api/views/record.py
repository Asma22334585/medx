from models import storage
from models.record import Record
from api.views import app_views
from flask import make_response, request, abort, jsonify

@app_views.route('/records', methods=['GET'],strict_slashes=False)
def get_recs():
    """retrieve all records from Record object"""
    records = storage.all(Record).values()
    rec_list = []

    for record in records:
        rec_list.append(record.to_dict())
    return make_response(jsonify(rec_list))

@app_views.route("/records/<rec_id>", methods=['GET'], strict_slashes=False)
def get_rec(rec_id):
    """get a record obj"""
    record = storage.get(Record, rec_id)
    if not record:
        abort(404)

    return make_response(jsonify(record.to_dict()))

@app_views.route("/records", methods=['POST'], strict_slashes=False)
def new_rec():
    """create a new record"""
    new_data = request.get_json()

    if not new_data:
        abort(400)
    
    new_record = Record(**new_data)
    new_record.save()
    return make_response(jsonify(new_record.to_dict()), 201)

@app_views.route("/records/<rec_id>", methods=['PUT'], strict_slashes=False)
def update_rec(rec_id):
    """ update a new record"""
    record = storage.get(Record, rec_id)

    if not record:
        abort(404)

    ignore = ['id', 'user_id', 'doctor_id', 'created_at', 'update_at']

    new_data = request.get_json()
    if not new_data:
        abort(404, description="not a json")
    for key, value in new_data.items():
        if key not in ignore:
            setattr(record, key, value)
    storage.save()
    return make_response(jsonify(record.to_dict()), 200)

@app_views.route("/records/<rec_id>", methods=['DELETE'], strict_slashes=False)
def del_rec(rec_id):
    """deleting a rec object"""
    record = storage.get(Record, rec_id)
    if not record:
        abort(404)
    storage.delete(record)
    storage.save()
    make_response(jsonify({}), 200) 