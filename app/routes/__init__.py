"""Static Page Blueprint"""

from flask import Blueprint, render_template, redirect, url_for

page_blueprint = Blueprint("page", __name__)


@page_blueprint.route("/", methods=["GET"])
async def landing():
    """
    Landing Page
    - redirect to login page if session is expired
    - redirect to dashboard if session is not expired
    """
    return redirect(url_for("page.login"))


@page_blueprint.route("/login", methods=["GET"])
async def login():
    """
    Login Page
    """
    return render_template("login/index.html")


@page_blueprint.route("/register", methods=["GET"])
async def register():
    """Register Page"""
    return render_template("register/index.html")
