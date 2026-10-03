# Kid-Friendly Word Search Game

A fun, interactive web-based Word Search game built with Python and Flask as a Capstone project for NCLab.

---

## About the Project

This game was built as part of the NCLab Python and Data Analyst Program. Players visit a welcome screen, choose to start the game, and are given a randomly selected theme. They search for hidden words in a 6x6 letter grid and earn points for each word they find. When all words are found, a final mystery location is revealed.

---

## Features

- Welcome Screen - Players are greeted with a friendly welcome page before the game begins.
- - 3 Theme Categories - Animals, Food, and School words are randomly selected each time a new game starts.
  - - Interactive Word Grid - A 6x6 letter grid with hidden words placed horizontally, vertically, and diagonally.
    - - Letter Highlighting - When a word is found correctly, its letters are highlighted in green directly on the grid.
      - - Score Tracking - Players earn 10 points for every word they find correctly.
        - - Hint System - A riddle-style hint is shown to help players think about the theme.
          - - Words To Find List - The list of words to find is displayed on screen so kids always know what they are looking for.
            - - Scoreboard and Game Over Screen - When the game ends, the final score, all found words, and the mystery location answer are displayed.
              - - Play Again - Players can restart at any time and receive a brand new randomly selected theme.
                - - Bug Fix - Resolved an issue where certain letter placements caused incorrect overlapping on the grid.
                 
                  - ---

                  ## File Structure

                  ```
                  Capstone-Word-Search/
                   static/
                      style.css
                   templates/
                      welcome.html
                      game.html
                   app.py
                   Word_Search_Game.py
                   requirements.txt
                   README.md
                  ```

                  - static/style.css - All styling for the game including the grid, buttons, scoreboard, and welcome screen.
                  - - templates/welcome.html - The welcome screen players see when they first open the game.
                    - - templates/game.html - The main game board showing the grid, words to find, score, hints, and game over screen.
                      - - app.py - All Flask routes and game logic including score tracking, session management, and letter highlighting.
                        - - Word_Search_Game.py - The original terminal version of the word search engine used as the foundation for the web app.
                          - - requirements.txt - Lists all Python packages needed to run the app.
                           
                            - ---

                            ## How to Run

                            1. Clone the repository to your local machine:
                           
                            2. ```
                               git clone https://github.com/michellemprager-python-data-analyst/Capstone-Word-Search.git
                               ```

                               2. Install the required dependencies:
                              
                               3. ```
                                  pip install -r requirements.txt
                                  ```

                                  3. Start the app:
                                 
                                  4. ```
                                     python app.py
                                     ```

                                     4. Open your browser and go to:
                                    
                                     5. ```
                                        http://127.0.0.1:5000
                                        ```

                                        ---

                                        ## Built With

                                        Python 3, Flask, HTML5, CSS3, Jinja2 Templating

                                        ---

                                        ## Author

                                        Michelle Prager - NCLab Python and Data Analyst Program, 2026

                                        ---

                                        ## Training Program

                                        Completed as part of the NCLab Python Developer Training Program
                                        https://www.nclab.com
