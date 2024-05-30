from models import storage
from models.doctor import Doctor
from flask import (
                   render_template,
                   make_response,
                   jsonify,
                   request,
                   abort
                   )
from api.views import app_views


@app_views.route("/doctors", methods=['GET'], strict_slashes=False)
def get_docs():
    """get all doctors objects"""
    all_doctors = storage.all(Doctor).values()
    doctors_list = []

    for doctor in all_doctors:
        doctors_list.append(doctor.to_dict())

    return jsonify(doctors_list)

@app_views.route("/doctors/<doc_id>", methods=['GET'], strict_slashes=False)
def get_doc(doc_id):
    """return a doc obj"""
    doc = storage.get(Doctor, doc_id)
    if not doc:
        abort(404, description="not doc found")
    
    return make_response(jsonify(doc.to_dict()), 201)

@app_views.route("/doctors", methods=['POST'], strict_slashes=False)
def post_doc():
    """add a new doctors obj"""
    if not request.get_json():
        abort(400, description="not a JSON")

    doc_data = request.get_json()
    new_doc = Doctor(**doc_data)
    new_doc.save()
    return make_response(jsonify(new_doc.to_dict()), 200)

@app_views.route("/doctors/<doc_id>", methods=['PUT'], strict_slashes=False)
def update_doc(doc_id):
    """update a doc record"""
    doc = storage.get(Doctor, doc_id)

    new_data = request.get_json()
    ignore = ['id', 'email', 'created_at', 'update_at']

    for key, value in new_data.items():
        if key not in ignore:
            setattr(doc, key, value)
    storage.save()
    return make_response(jsonify(doc.to_dict()), 200)

@app_views.route("/doctors/<doc_id>", methods=['DELETE'], strict_slashes=False)
def del_doc(doc_id):
    """delete a doc object"""
    doc = storage.get(Doctor, doc_id)
    if not doc:
        abort(404)

    storage.delete(doc)
    storage.save()
    return make_response(jsonify({}), 201)