import random

quotes_db = {
    "motivational": [
        "Keep pushing!",
        "Believe in yourself, anything is possible."
    ],
    "random": [
        "Your friend also doesn't know what they're doing.",
        "Blah"
    ]
}

def random_quote():
    random_category = random.choice(list(quotes_db.keys()))
    return random.choice(quotes_db[random_category])

def quote_by_category(category):
    if category not in quotes_db:
        raise ValueError(f"Category {category} doesn't exist yet.")
    return random.choice(quotes_db[category])

