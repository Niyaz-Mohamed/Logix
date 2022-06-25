from app.models import *

# Define pages
pages = [
    # Preface
    Page(
        "Introduction",
        embed="https://v1.embednotion.com/embed/d15337df9e454f3aa54d824ee24ba1d9",
    ),
    Page(
        "Using the tutorial",
        embed="",
    ),
    Page(
        "Prerequisites",
        embed="",
    ),
    # Logic Gates
    Page(
        "What are Logic Gates?",
        embed="",
    ),
    Page(
        "AND and NOT Gates",
        embed="",
    ),
    Page(
        "Universal Gates",
        embed="",
    ),
    Page(
        "More Complex Gates",
        embed="",
    ),
    # Addition and Subtraction
    Page(
        "Binary numbers",
        embed="",
    ),
    Page(
        "Binary Addition Theory",
        embed="",
    ),
    Page(
        "The 4-Adder",
        embed="",
    ),
    Page(
        "Negative Numbers Theory",
        embed="",
    ),
    Page(
        "The ALU",
        embed="",
    ),
    # Data Storage
    Page(
        "How Computers Remember",
        embed="",
    ),
    Page(
        "The SR Latch",
        embed="",
    ),
    Page(
        "The Register (Maybe exclude?)",
        embed="",
    ),
    # Physical Gates
    Page(
        "TBD",
        embed="",
    ),
]

# Define sections
sections = [
    Section("Preface", [1, 3], Color("#27ADDA")),
    Section("Logic Gates", [4, 7], Color("#F4442E")),
    Section("Addition and Subtraction", [8, 12], Color("#D0DA14")),
    Section("Data Storage", [13, 15], Color("#2EDA36")),
    Section("Physical Gates", 16, Color("#DA29DA")),
]

# Initalize page manager
pageManager = PageManager(pages, sections)
