#!/usr/bin/env python3
"""
Hangman Game - A classic word-guessing game implementation.

This module provides a complete Hangman game with:
- Random word selection from a predefined list
- Letter guessing with validation
- ASCII art hangman display
- Win/lose condition tracking
- Input validation and duplicate guess prevention
"""

import random
from typing import Set, List


class HangmanGame:
    """Main game logic for Hangman."""
    
    # ASCII art for each wrong guess (0-6)
    HANGMAN_ART = [
        """
        ------
        |    |
        |
        |
        |
        |
        --------
        """,
        """
        ------
        |    |
        |    O
        |
        |
        |
        --------
        """,
        """
        ------
        |    |
        |    O
        |    |
        |
        |
        --------
        """,
        """
        ------
        |    |
        |    O
        |   /|
        |
        |
        --------
        """,
        """
        ------
        |    |
        |    O
        |   /|\\
        |
        |
        --------
        """,
        """
        ------
        |    |
        |    O
        |   /|\\
        |   /
        |
        --------
        """,
        """
        ------
        |    |
        |    O
        |   /|\\
        |   / \\
        |
        --------
        """
    ]
    
    # Word list categorized by difficulty
    WORD_LIST = [
        # Easy (5-6 letters)
        "apple", "beach", "chair", "dance", "eagle",
        "flame", "grape", "house", "image", "juice",
        # Medium (7-8 letters)
        "keyboard", "monitor", "python", "server", "network",
        "database", "cloud", "terminal", "function", "variable",
        # Hard (9+ letters)
        "kubernetes", "infrastructure", "architecture", "distributed",
        "microservices", "container", "deployment", "observability"
    ]
    
    def __init__(self, max_attempts: int = 6):
        """Initialize a new Hangman game.
        
        Args:
            max_attempts: Maximum number of wrong guesses allowed (default: 6)
        """
        self.max_attempts = max_attempts
        self.word = random.choice(self.WORD_LIST).lower()
        self.guessed_letters: Set[str] = set()
        self.wrong_guesses: int = 0
        self.game_won: bool = False
        self.game_over: bool = False
    
    def get_display_word(self) -> str:
        """Return the word with guessed letters revealed and others as underscores."""
        display = []
        for letter in self.word:
            if letter in self.guessed_letters:
                display.append(letter)
            else:
                display.append('_')
        return ' '.join(display)
    
    def is_letter_guessed(self, letter: str) -> bool:
        """Check if a letter has already been guessed."""
        return letter.lower() in self.guessed_letters
    
    def guess_letter(self, letter: str) -> tuple[bool, str]:
        """Process a letter guess.
        
        Args:
            letter: The letter being guessed
            
        Returns:
            Tuple of (is_valid_guess, message)
        """
        # Validate input
        if len(letter) != 1 or not letter.isalpha():
            return False, "Please enter a single letter (a-z)."
        
        letter = letter.lower()
        
        if self.is_letter_guessed(letter):
            return False, f"You already guessed '{letter}'. Try another letter."
        
        # Add to guessed letters
        self.guessed_letters.add(letter)
        
        # Check if letter is in word
        if letter in self.word:
            message = f"Good guess! '{letter}' is in the word."
            # Check win condition
            if all(l in self.guessed_letters for l in self.word):
                self.game_won = True
                self.game_over = True
                message += " Congratulations! You won!"
        else:
            self.wrong_guesses += 1
            message = f"Sorry, '{letter}' is not in the word."
            # Check lose condition
            if self.wrong_guesses >= self.max_attempts:
                self.game_over = True
                message += f" Game over! The word was '{self.word}'."
        
        return True, message
    
    def get_hangman_display(self) -> str:
        """Return the current hangman ASCII art based on wrong guesses."""
        return self.HANGMAN_ART[self.wrong_guesses]
    
    def get_remaining_attempts(self) -> int:
        """Return the number of attempts remaining."""
        return self.max_attempts - self.wrong_guesses
    
    def reset_game(self):
        """Reset the game to play again with a new word."""
        self.word = random.choice(self.WORD_LIST).lower()
        self.guessed_letters.clear()
        self.wrong_guesses = 0
        self.game_won = False
        self.game_over = False


def print_welcome():
    """Print welcome message and instructions."""
    print("=" * 60)
    print(" " * 20 + "HANGMAN")
    print("=" * 60)
    print("\nWelcome to Hangman!")
    print("\nHow to play:")
    print("  1. A random word has been selected")
    print("  2. Guess letters one at a time")
    print("  3. Correct guesses reveal the letter")
    print("  4. Wrong guesses add to the hangman")
    print("  5. You have 6 attempts before game over")
    print("\nWord categories: Easy, Medium, Hard")
    print("Good luck!\n")
    print("=" * 60)


def get_player_guess() -> str:
    """Get and validate player's letter guess."""
    while True:
        guess = input("\nEnter a letter: ").strip()
        if guess:
            return guess
        print("Please enter a letter.")


def play_game():
    """Main game loop."""
    game = HangmanGame()
    print_welcome()
    
    while not game.game_over:
        # Display current state
        print(game.get_hangman_display())
        print(f"\nWord: {game.get_display_word()}")
        print(f"Attempts remaining: {game.get_remaining_attempts()}")
        print(f"Guessed letters: {', '.join(sorted(game.guessed_letters)) if game.guessed_letters else 'None'}")
        
        # Get player's guess
        guess = get_player_guess()
        
        # Process guess
        is_valid, message = game.guess_letter(guess)
        print(f"\n{message}")
    
    # Game over - show final state
    if game.game_won:
        print(game.get_hangman_display())
        print(f"\n🎉 YOU WON! The word was '{game.word}'")
    else:
        print(game.get_hangman_display())
        print(f"\n😔 GAME OVER! The word was '{game.word}'")
    
    # Ask to play again
    play_again = input("\nWould you like to play again? (y/n): ").strip().lower()
    if play_again == 'y':
        print("\n" + "=" * 60 + "\n")
        play_game()
    else:
        print("\nThanks for playing! Goodbye! 👋")


if __name__ == "__main__":
    play_game()
