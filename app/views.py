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
@app.route("/tutorial/")
def load_tutorial():
    print(
        pageManager.getCurrentPage().file,
        pageManager.getCurrentPage().section.theme.hex,
    )
    # pageName = pageManager.getCurrentPage().file
    # Check for page index
    isFirstPage = pageManager.currentPageIndex == 1
    isLastPage = pageManager.currentPageIndex == len(pageManager.pages)

    return render_template(
        "pages.html",
        isFirstPage=isFirstPage,
        isLastPage=isLastPage,
        pageIndex=pageManager.currentPageIndex,
        pageData=pageManager.getCurrentPage(),
    )


# Handle jumps between pages
@app.route("/tutorial/<index>")
def jump_to_index(index):
    pageManager.setCurrentPageIndex(int(index))
    return redirect(url_for("load_tutorial"))
