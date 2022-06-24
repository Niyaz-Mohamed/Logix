from flask import render_template
from werkzeug.exceptions import HTTPException

# Import custom objects
from app import app
from app.models import *

# Title page
@app.route("/")
@app.route("/start")
def title():
    return render_template("title.html")


@app.route("/<generic>/")
def show_user_profile(generic):
    # Show route-based template
    return f"Generic {generic}"


# Catch errors
@app.errorhandler(HTTPException)
def handle_exception(e):
    return render_template("error.html", error=e)
