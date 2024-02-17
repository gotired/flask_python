"""Authentication Blueprint"""

from http import HTTPStatus

from flask import Blueprint, make_response, request

from app.models.user import Register
from app.models.response import Response

authentication_blueprint = Blueprint("authentication", __name__)


@authentication_blueprint.route("/register", methods=["POST"])
async def register():
    """Register user"""
    user_detail = Register(**request.get_json()).model_dump()
    return make_response(Response(data=user_detail).success, HTTPStatus.CREATED)


@authentication_blueprint.route("/login", methods=["POST"])
async def login():
    """Login user"""
    email = request.form.get("email")
    password = request.form.get("password")
    return make_response(
        {
            "email": email,
            "password": password,
        },
        HTTPStatus.OK,
    )


@authentication_blueprint.route("/access", methods=["POST"])
async def validate_access():
    """Validate access token"""
    return make_response("OK", HTTPStatus.OK)


@authentication_blueprint.route("/refresh", methods=["POST"])
async def refresh_token():
    """refresh token to generate access token"""
    return make_response("OK", HTTPStatus.OK)


@authentication_blueprint.route("/logout", methods=["POST"])
async def logout():
    """Logout user"""
    return make_response("OK", HTTPStatus.OK)
