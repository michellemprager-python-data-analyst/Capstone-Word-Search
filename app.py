from flask import Flask, render_template, request, session, redirect, url_for
import random
import json

app = Flask(__name__)
app.secret_key = "wordsearch_secret_key_2024"

GRID_SIZE = 6

THEMES = [
    {
        "name": "Animals",
        "location_answer": "the zoo",
        "words": ["cat", "dog", "lion"],
        "hints": ["These are furry friends.", "Some of these roar!", "You might see these at a zoo."]
    },
    {
        "name": "Food",
        "location_answer": "the kitchen",
        "words": ["pie", "milk", "egg"],
        "hints": ["You can eat these.", "You might find these in the fridge.", "Someone cooks these."]
    },
    {
        "name": "School",
        "location_answer": "the school",
        "words": ["pen", "desk", "book"],
        "hints": ["You learn here.", "You sit at one of these.", "You write with one of these."]
    }
]

def create_empty_grid(size):
    return [[" " for _ in range(size)] for _ in range(size)]

def can_place_word(grid, word, row, col, dr, dc):
    size = len(grid)
    for i, ch in enumerate(word):
        r = row + dr * i
        c = col + dc * i
        if r >= size or c >= size:
            return False
        if grid[r][c] not in (" ", ch.upper()):
            return False
    return True

def place_word(grid, word):
    size = len(grid)
    directions = [(0, 1), (1, 0)]
    for _ in range(50):
        dr, dc = random.choice(directions)
        if dr == 0:
            row = random.randint(0, size - 1)
            col = random.randint(0, size - len(word))
        else:
            row = random.randint(0, size - len(word))
            col = random.randint(0, size - 1)
        if can_place_word(grid, word, row, col, dr, dc):
            coords = []
            for i, ch in enumerate(word):
                r = row + dr * i
                c = col + dc * i
                grid[r][c] = ch.upper()
                coords.append([r, c])
            return coords
    return []

def fill_random_letters(grid):
    for r in range(len(grid)):
        for c in range(len(grid[r])):
            if grid[r][c] == " ":
                grid[r][c] = random.choice("ABCDEFGHIJKLMNOPQRSTUVWXYZ")

@app.route("/")
def welcome():
    return render_template("welcome.html")

@app.route("/start", methods=["POST"])
def start():
    theme = random.choice(THEMES)
    words = theme["words"]
    hint = random.choice(theme["hints"])
    grid = create_empty_grid(GRID_SIZE)
    positions = {}
    positions_coords = {}
    for w in words:
        coords = place_word(grid, w)
        if coords:
            positions[w] = coords
            positions_coords[w] = coords
    fill_random_letters(grid)
    session["theme_name"] = theme["name"]
    session["words"] = words
    session["hint"] = hint
    session["grid"] = grid
    session["positions"] = list(positions.keys())
    session["positions_coords"] = positions_coords
    session["found_words"] = []
    session["found_coords"] = []
    session["score"] = 0
    session["location_answer"] = theme["location_answer"]
    return render_template("game.html", grid=grid, words=words, hint=hint,
        message="", found_words=[], found_coords=[], score=0,
        theme_name=theme["name"], game_over=False, location_answer=None,
        positions_json=json.dumps(positions_coords))

@app.route("/guess", methods=["POST"])
def guess():
    guess_word = request.form.get("guess", "").strip().lower()
    grid = session.get("grid", [])
    words = session.get("words", [])
    hint = session.get("hint", "")
    found_words = session.get("found_words", [])
    found_coords = session.get("found_coords", [])
    score = session.get("score", 0)
    positions = session.get("positions", [])
    positions_coords = session.get("positions_coords", {})
    theme_name = session.get("theme_name", "")
    location_answer = session.get("location_answer", "")
    message = ""
    game_over = False
    if guess_word in positions:
        if guess_word not in found_words:
            found_words.append(guess_word)
            if guess_word in positions_coords:
                found_coords.extend(positions_coords[guess_word])
            score += 10
            session["found_words"] = found_words
            session["found_coords"] = found_coords
            session["score"] = score
            message = f"Great job! You found {guess_word.upper()}!"
        else:
            message = f"You already found {guess_word.upper()}!"
    else:
        message = "Not one of the hidden words. Try again!"
    if len(found_words) == len(positions):
        game_over = True
    return render_template("game.html", grid=grid, words=words, hint=hint,
        message=message, found_words=found_words, found_coords=found_coords,
        score=score, theme_name=theme_name, game_over=game_over,
        location_answer=location_answer if game_over else None,
        positions_json=json.dumps(positions_coords))

@app.route("/reset")
def reset():
    session.clear()
    return redirect(url_for("welcome"))

if __name__ == "__main__":
    app.run(debug=True)
