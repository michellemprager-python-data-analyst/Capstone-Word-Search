import random
from colorama import Fore, Style, init

init(autoreset=True)

GRID_SIZE = 6  # smaller grid for kids

# Kid-friendly themes
THEMES = [
    {
        "name": "animals",
        "location_answer": "the zoo",
        "words": ["cat", "dog", "lion"],
        "hints": [
            "HINT: These are furry friends.",
            "HINT: Some of these roar!",
            "HINT: You might see these at a zoo."
        ]
    },
    {
        "name": "food",
        "location_answer": "the kitchen",
        "words": ["pie", "milk", "egg"],
        "hints": [
            "HINT: You can eat these.",
            "HINT: You might find these in the fridge.",
            "HINT: Someone cooks these."
        ]
    },
    {
        "name": "school",
        "location_answer": "the school",
        "words": ["pen", "desk", "book"],
        "hints": [
            "HINT: You learn here.",
            "HINT: You sit at one of these.",
            "HINT: You write with one of these."
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
    directions = [(0, 1), (1, 0)]  # only right + down
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


def print_grid(grid, found):
    size = len(grid)
    border = "+" + "---+" * size
    print(border)
    for r in range(size):
        row = "|"
        for c in range(size):
            ch = grid[r][c]
            if (r, c) in found:
                row += f" {Fore.GREEN}{ch}{Style.RESET_ALL} |"
            else:
                row += f" {ch} |"
        print(row)
        print(border)


def main():
    print("WELCOME TO THE KID-FRIENDLY WORD SEARCH!")
    print("Find the hidden words, then solve the final mystery!")
    print()

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

    print(f"There are {len(positions)} hidden words!")
    print(hint)
    print()

    # ⭐ SHOW WORDS TO FIND (kid-friendly fix)
    print("WORDS TO FIND:")
    for w in words:
        print(f"- {w.upper()}")
    print()

    print("Here is your puzzle:\n")
    found = set()
    print_grid(grid, found)
    print()

    found_words = set()

    while len(found_words) < len(positions):
        guess = input("Type a word you found (or 'quit'): ").strip().lower()

        if guess == "quit":
            print("Thanks for playing!")
            return

        if guess in positions:
            if guess in found_words:
                print("You already found that one!")
            else:
                found_words.add(guess)
                print(f"Great job! You found {guess.upper()}!")

                for r, c in positions[guess]:
                    found.add((r, c))

                print()
                print_grid(grid, found)
        else:
            print("Not one of the hidden words. Try again!")
        print()

    print("You found all the words!")
    print("FINAL MYSTERY:")
    print("Where are you?")
    print()

    while True:
        final = input("Your answer: ").strip().lower()
        if final == answer or theme["name"] in final:
            print(f"Correct! You were at {answer.upper()}!")
            break
        else:
            print("Not quite — try again!")


if __name__ == "__main__":
    main()
