from flask import Blueprint, jsonify, request
import requests

from models import ClassroomBooking, db

classroom_blueprint = Blueprint('classroom_api_routes', __name__, url_prefix="/api/classroom")

USER_API_URL = 'http://127.0.0.1:5001/api/user'

def get_user(api_key):
    headers = {
        'Authorization': api_key
    }

    response = requests.get(USER_API_URL, headers=headers)
    if response.status_code != 200:
        return {'message': 'Not Authorized'}

    user = response.json()
    return user


