from flask import Blueprint, request, jsonify
from dao.user_dao import UserDao


user_bp = Blueprint("users", __name__, url_prefix="/users")


@user_bp.route("/", methods=["POST"])
def create_user():
    data = request.get_json()

    if not data:
        return jsonify({"error": "Invalid input"}), 400

    user = UserDao.create_user(**data)

    if not user:
        return jsonify({"error": "User creation failed"}), 500

    return jsonify({
        "id": user.id,
        "name": user.name,
        "email": user.email
    }), 201


@user_bp.route("/<int:user_id>", methods=["GET"])
def get_user(user_id):
    user = UserDao.get_by_id(user_id)

    if not user:
        return jsonify({"error": "User not found"}), 404

    return jsonify({
        "id": user.id,
        "name": user.name,
        "email": user.email
    }), 200


@user_bp.route("/email/<string:email>", methods=["GET"])
def get_user_by_email(email):
    user = UserDao.get_by_email(email)

    if not user:
        return jsonify({"error": "User not found"}), 404

    return jsonify({
        "id": user.id,
        "name": user.name,
        "email": user.email
    }), 200
