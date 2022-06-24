from flask import render_template, redirect, url_for
from werkzeug.exceptions import HTTPException

# Import custom objects
from app import app
from app.models import *

# Initialize globals
pages = [
    Page("preface.html"),
    Page("logic_gate_i.html"),
    Page("logic_gate_II.html"),
]
sections = [
    Section("Preface", [1, 1], Color("#114B5F")),
    Section("LGates", [2, 3], Color("#F4442E")),
]
pageManager = PageManager(pages, sections)

# Title page
@app.route("/")
@app.route("/start")
def title():
    return render_template("title.html")


# Catch errors
@app.errorhandler(HTTPException)
def handle_exception(e):
    return render_template("error.html", error=e)


# Page handler
@app.route("/tutorial/")
def load_tutorial():
    file = "pages/" + pageManager.getCurrentPage().file
    return render_template(file)


# Handle jumps between pages
@app.route("/tutorial/<index>")
def jump_to_index(index):
    pageManager.setCurrentPageIndex(index)
    return redirect(url_for("show_tutorial_page"))
