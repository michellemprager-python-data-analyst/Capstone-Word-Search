from flask import Flask, render_template, request
import random

app = Flask(__name__)

GRID_SIZE = 6

THEMES = [
    {
        "name": "animals",
        "location_answer": "the zoo",
        "words": ["cat", "dog", "lion"],
        "hints": [
            "These are furry friends.",
            "Some of these roar!",
            "You might see these at a zoo."
        ]
    },
    {
        "name": "food",
        "location_answer": "the kitchen",
        "words": ["pie", "milk", "egg"],
        "hints": [
            "You can eat these.",
            "You might find these in the fridge.",
            "Someone cooks these."
        ]
    },
    {
        "name": "school",
        "location_answer": "the school",
        "words": ["pen", "desk", "book"],
        "hints": [
            "You learn here.",
            "You sit at one of these.",
            "You write with one of these."
        ]
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
    directions = [(0, 1), (1, 0)]  # right or down
    word = word.lower()

    for _ in range(50):
        dr, dc = random.choice(directions)
        if dr == 0:  # horizontal
            row = random.randint(0, size - 1)
            col = random.randint(0, size - len(word))
        else:  # vertical
            row = random.randint(0, size - len(word))
            col = random.randint(0, size - 1)

        if can_place_word(grid, word, row, col, dr, dc):
            coords = []
            for i, ch in enumerate(word):
                r = row + dr * i
                c = col + dc * i
                grid[r][c] = ch.upper()
                coords.append((r, c))
            return coords

    return []


def fill_random_letters(grid):
    for r in range(len(grid)):
        for c in range(len(grid[r])):
            if grid[r][c] == " ":
                grid[r][c] = random.choice("ABCDEFGHIJKLMNOPQRSTUVWXYZ")


@app.route("/", methods=["GET", "POST"])
def game():
    theme = random.choice(THEMES)
    words = theme["words"]
    hint = random.choice(theme["hints"])
    answer = theme["location_answer"]

    grid = create_empty_grid(GRID_SIZE)
    positions = {}

    for w in words:
        coords = place_word(grid, w)
        if coords:
            positions[w] = coords

    fill_random_letters(grid)

    found_words = []
    message = ""

    if request.method == "POST":
        guess = request.form.get("guess", "").lower()

        if guess in words:
            if guess not in found_words:
                found_words.append(guess)
                message = f"Great job! You found {guess.upper()}!"
            else:
                message = "You already found that word!"
        else:
            message = "Not one of the hidden words. Try again!"

    return render_template(
        "game.html",
        grid=grid,
        words=words,
        hint=hint,
        message=message,
        found_words=found_words,
        answer=answer
    )


if __name__ == "__main__":
    app.run(debug=True)
