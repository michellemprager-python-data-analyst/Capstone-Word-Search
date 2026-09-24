Author
Michelle M. Prager
NCLab Python Developer Training — Capstone Project


Word Search Game — Capstone Project
Overview
This project is a kid‑friendly Word Search Game built using Python and Flask.
It generates a 6×6 word search grid, hides themed words (animals, food, school), and allows the user to guess words through a simple web interface.

The game provides:

A randomly selected theme

A hint related to the hidden words

A dynamically generated word search grid

Feedback messages for correct or incorrect guesses

This project demonstrates:

Python functions

Randomized grid generation

Flask routing

HTML templating

Basic CSS styling

Full project structure for a web application

Project Structure
Code
PythonProject_Capstone_Word_Search_Game/
│
├── app.py                 # Main Flask application
│
├── requirements.txt       # Project dependencies
│
├── static/
│   └── style.css          # Styling for the game page
│
└── templates/
    └── game.html          # HTML template for the game interface
How to Run the Project
1. Install dependencies
Run this in your terminal:

Code
pip install -r requirements.txt
2. Start the Flask app
Run:

Code
py app.py
You should see:

Code
 * Running on http://127.0.0.1:5000
3. Open the game
Go to:

Code
http://127.0.0.1:5000
Features
Random theme selection

Random hint selection

Words placed horizontally or vertically

Random letters fill unused spaces

Clean, simple interface

Kid‑friendly feedback messages

Future Improvements
Add diagonal word placement

Add multiple difficulty levels

Add score tracking

Add a “found words” highlight in the grid

Add sound effects or animations