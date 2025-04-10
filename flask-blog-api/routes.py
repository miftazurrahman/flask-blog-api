from flask import Blueprint, jsonify
from flask_jwt_extended import jwt_required
from models import posts

bp = Blueprint('routes', __name__)

@bp.route('/posts', methods=['GET'])
@jwt_required()
def get_posts():
    return jsonify(posts)
