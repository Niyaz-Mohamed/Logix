from app.models import *

# Define pages
pages = [
    Page(
        "preface.html",
        embed="https://v1.embednotion.com/embed/d15337df9e454f3aa54d824ee24ba1d9",
    ),
    Page(
        "logic_gate_i.html",
        embed="https://v1.embednotion.com/embed/d15337df9e454f3aa54d824ee24ba1d9",
    ),
    Page(
        "logic_gate_II.html",
        embed="",
    ),
    Page(
        "logic_gate_II.html",
        embed="",
    ),
]

# Define Section
sections = [
    Section("Preface", 1, Color("#27ADDA")),
    Section("Logic Gates", 2, Color("#F4442E")),
    Section("Data Storage", 3, Color("#2EDA36")),
    Section("Physical Gates", 4, Color("#DA29DA")),
]

#
pageManager = PageManager(pages, sections)
