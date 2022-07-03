from flask import render_template, redirect, url_for
from werkzeug.exceptions import HTTPException

# Import custom objects
from app import app
from app.globals import pageManager

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
@app.route("/tutorial/<int:pageIndex>")
def load_tutorial(pageIndex):

    # Check for page index
    pageData = pageManager.getPageAtIndex(pageIndex)
    isFirstPage = pageIndex == 1
    isLastPage = pageIndex == len(pageManager.pages)

    return render_template(
        "pages.html",
        isFirstPage=isFirstPage,
        isLastPage=isLastPage,
        pageIndex=pageIndex,
        pageData=pageData,
    )
