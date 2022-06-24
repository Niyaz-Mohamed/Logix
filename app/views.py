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
    Section("Preface", [1, 1], Color("#00ff99")),
    Section("LGates", [2, 3], Color("#00ff99")),
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
def show_tutorial_page():
    file = pageManager.getCurrentPage().file
    pageIndex = pageManager.currentPageIndex
    return render_template(pageManager.getCurrentPage().file)


# Handle jumps between pages
@app.route("/tutorial/jumpTo/<index>")
def jump_to_index(index):
    pageManager.setIndex(index)
    return redirect(url_for("show_tutorial_page"))
