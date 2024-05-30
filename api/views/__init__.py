from flask import Blueprint
app_views = Blueprint('app_views', __name__, url_prefix="/api/v1")

from api.views.user import *
from api.views.doctor import *
from api.views.record import *