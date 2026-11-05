import random

class AdvancedHangman:
    """An advanced, object-oriented implementation of the classic Hangman game."""
    

    HANGMAN_STAGES = [
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

    def __init__(self):
        # 5 predefined words as required by the internship scope
        self.word_bank = ["python", "developer", "internship", "software", "automation"]
        self.target_word = random.choice(self.word_bank).upper()
        self.guessed_letters = set()
        self.incorrect_guesses = 0
        self.max_incorrect = 6

    def display_game_state(self):
        # Print the corresponding ASCII art based on the error count
        print(self.HANGMAN_STAGES[self.incorrect_guesses])
        
        # Display the word with hidden letters
        display = [letter if letter in self.guessed_letters else "_" for letter in self.target_word]
        print(f"WORD: {' '.join(display)}")
        
        # Display previously guessed letters cleanly
        sorted_guesses = sorted(list(self.guessed_letters))
        print(f"Guessed letters: {', '.join(sorted_guesses) if sorted_guesses else 'None'}")
        print(f"Guesses remaining: {self.max_incorrect - self.incorrect_guesses}\n")

    def play(self):
        print("="*40)
        print("       CODEALPHA HANGMAN PRO")
        print("="*40)

        while self.incorrect_guesses < self.max_incorrect:
            self.display_game_state()
            
           
            if all(letter in self.guessed_letters for letter in self.target_word):
                print(f"🏆 CONGRATULATIONS! You survived. The word was '{self.target_word}'.")
                return
            
            guess = input("Enter a single letter: ").upper()
            
            
            if len(guess) != 1 or not guess.isalpha():
                print("⚠️ Invalid input. Please enter a single alphabetical letter.\n")
                continue
            if guess in self.guessed_letters:
                print("⚠️ You already guessed that letter. Try again.\n")
                continue
                
            self.guessed_letters.add(guess)
            
            if guess not in self.target_word:
                self.incorrect_guesses += 1
                print(f"❌ Incorrect! '{guess}' is not in the word.\n")
            else:
                print(f"✅ Good job! '{guess}' is in the word.\n")

        
        self.display_game_state()
        print(f"💀 GAME OVER! You've been hung. The word was '{self.target_word}'.")


if __name__ == "__main__":
    game = AdvancedHangman()
    game.play()