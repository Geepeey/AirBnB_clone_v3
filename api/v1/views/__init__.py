#!/usr/bin/python3

"""init file for views module"""

from flask import Blueprint
from .index import *

app_views = Blueprint('app_views', __name__, url_prefix='/api/v1')
