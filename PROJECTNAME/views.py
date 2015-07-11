from flask import render_template, request, redirect, url_for, flash
from flask.ext.login import login_user, logout_user, login_required, current_user
from werkzeug.security import check_password_hash, generate_password_hash

from PROJECTNAME import app
from .models import User
from .database import session, get_one_or_create

@app.route("/", methods=["GET"])
def home_get():
	""" Main page of the site """
	return render_template("home.html")

@app.route("/login", methods=["GET"])
def login_get():
  return render_template("login.html")

@app.route("/login", methods=["POST"])
def login_post():
  email = request.form["email"]
  password = request.form["password"]
  user = session.query(User).filter_by(email=email).first()
  if not user or not check_password_hash(user.password, password):
    flash("Incorrect username or password", "danger")
    return redirect(url_for("login_get"))
  
  login_user(user)
  return redirect(request.args.get('next') or url_for("home_get"))

@app.route("/logout", methods=["GET"])
def logout_get():
  logout_user()
  return redirect(url_for("home_get"))