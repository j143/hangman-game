# Hangman Game 🎮

A classic word-guessing game implemented in Python.

## Features

- **Random word selection** from categorized word lists (Easy, Medium, Hard)
- **ASCII art hangman** display that progresses with wrong guesses
- **Input validation** to prevent invalid or duplicate guesses
- **Win/lose tracking** with clear game state messages
- **Play again** option after each game

## Prerequisites

- Python 3.8 or higher
- No external dependencies required (uses only Python standard library)

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/j143/hangman-game.git
   cd hangman-game
   ```

2. (Optional) Create a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\\Scripts\\activate
   ```

## How to Play

Run the game:
```bash
python hangman.py
```

### Game Rules

1. A random word is selected from the word list
2. You have 6 attempts to guess the word
3. Enter one letter at a time
4. Correct guesses reveal the letter in its position(s)
5. Wrong guesses add a body part to the hangman
6. Win by guessing all letters before running out of attempts

### Example Session

```
============================================================
                    HANGMAN
============================================================

Welcome to Hangman!

How to play:
  1. A random word has been selected
  2. Guess letters one at a time
  3. Correct guesses reveal the letter
  4. Wrong guesses add to the hangman
  5. You have 6 attempts before game over

Word categories: Easy, Medium, Hard
Good luck!

============================================================

------
|    |
|
|
|
|
--------

Word: _ _ _ _ _ _
Attempts remaining: 6
Guessed letters: None

Enter a letter: a

Good guess! 'a' is in the word.
```

## Project Structure

```
hangman-game/
├── hangman.py          # Main game logic and entry point
├── requirements.txt    # Python dependencies (none required)
├── README.md          # This file
└── .gitignore         # Git ignore patterns
```

## Code Structure

The game is implemented using a `HangmanGame` class with the following key methods:

- `__init__()`: Initialize game state
- `get_display_word()`: Return word with guessed letters revealed
- `guess_letter()`: Process a letter guess and update game state
- `get_hangman_display()`: Return current ASCII art
- `reset_game()`: Start a new game with a new word

## Customization

You can customize the game by modifying:

- **Word list**: Add or remove words in the `WORD_LIST` constant
- **Difficulty**: Adjust word categories or add new ones
- **Max attempts**: Change `max_attempts` parameter in `HangmanGame.__init__()`
- **ASCII art**: Modify the `HANGMAN_ART` list for different visuals

## License

This project is open source and available for educational purposes.

## Contributing

Feel free to:
- Add new word categories
- Improve the ASCII art
- Add features like score tracking or hints
- Create a GUI version

Happy coding! 🚀
