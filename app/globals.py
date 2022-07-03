from app.models import *

# Define pages
pages = [
    # Preface
    Page(
        "Introduction",
        embed="https://v1.embednotion.com/embed/929eb485e4514f1ea9d84ea10d1caef8",
    ),
    Page(
        "Prerequisites",
        embed="https://v1.embednotion.com/embed/d10bd89358f64492a2dc7de4f3db6465",
    ),
    Page(
        "Using the tutorial",
        embed="https://v1.embednotion.com/embed/0d0f78205b334c68a0c9278240d4ba3e",
    ),
    # Logic Gates
    Page(
        "What are Logic Gates?",
        embed="https://v1.embednotion.com/embed/a4fa7b307d4a4622b1fdd24c0c3a4e89",
    ),
    Page(
        "AND and NOT Gates",
        embed="https://v1.embednotion.com/embed/59b58afbe65b438095329c02fd67b742",
    ),
    Page(
        "Other Gates",
        embed="https://v1.embednotion.com/embed/b4cfacd16a9a44a58812b153ac45319d",
    ),
    Page(
        "Universal Gates",
        embed="https://v1.embednotion.com/embed/aafa75eb799e4b45a95f352925c2a9a6",
    ),
    # Logical Arithmetic
    Page(
        "Binary numbers",
        embed="https://v1.embednotion.com/embed/b1da3c23cbfa48c2967e9a963aac247b",
    ),
    Page(
        "Binary Addition",
        embed="https://v1.embednotion.com/embed/a7223f63ff5e4941b1b69eb331f2389a",
    ),
    Page(
        "The Half-Adder",
        embed="https://v1.embednotion.com/embed/658901e912ab4bc2a1a4e47e34d750be",
    ),
    Page(
        "The Full Adder",
        embed="https://v1.embednotion.com/embed/afe2b68bdace4bfca907a95b1f4fe884",
    ),
    Page(
        "The 4-bit Adder",
        embed="https://v1.embednotion.com/embed/6a9b9cc5c4574b04ab2bd174255f0c31",
    ),
    # Data Storage
    Page(
        "How Computers Remember",
        embed="https://v1.embednotion.com/embed/e4e182acf6e844db94d71a32838e40c2",
    ),
    # Page(
    #     "Getting an idea of scale",
    #     embed="https://v1.embednotion.com/embed/255ca2663e2b4c3c9975dcef3be3c853",
    # ),
    Page(
        "The SR-Latch",
        embed="https://v1.embednotion.com/embed/f99095cf355547ab921a121efabf65d0",
    ),
    Page(
        "The D-Latch",
        embed="https://v1.embednotion.com/embed/d3e22317c9cf4a9e8f4d379c6e604919",
    ),
    # Physical Gates
    Page(
        "Physical Logic Gates",
        embed="https://v1.embednotion.com/embed/5e377b8b4dc04c539f2522eb8c470ef2",
    ),
    Page(
        "Simple Model",
        embed="https://v1.embednotion.com/embed/08c0cf76e29b476387dbcfddb39e819e",
    ),
    # Page(
    #     "The Transistor",
    #     embed="https://v1.embednotion.com/embed/10b527267e964c49865c7c9d5044023f",
    # ),
    # Page(
    #     "Application",
    #     embed="https://v1.embednotion.com/embed/e5940f9f03d14cd296491c40d07700ad",
    # ),
    # Conclusion
    Page(
        "Conclusion",
        embed="https://v1.embednotion.com/embed/a420f35d77ee453481fe8f9df58fa466",
    ),
]

# Define sections
sections = [
    Section("Preface", [1, 3], Color("#27ADDA")),
    Section("Logic Gates", [4, 7], Color("#F4442E")),
    Section("Addition and Subtraction", [8, 12], Color("#D0DA14")),
    Section("Data Storage", [13, 15], Color("#5ED05B")),
    Section("Physical Gates", [16, 17], Color("#DA29DA")),
    Section("Conclusion", 18, Color("#010203")),
]

# Initalize page manager
pageManager = PageManager(pages, sections)
