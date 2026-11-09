"""
Number Guessing Game
A terminal-based number guessing game with difficulty levels, dynamic hints,
score tracking, and input validation.
"""

import random
import sys


class NumberGuessingGame:
    def __init__(self):
        self.games_played = 0
        self.games_won = 0
        self.best_score = None  # Lowest attempts in a winning game

    def get_difficulty_settings(self):
        """Prompt user for difficulty and return (min_val, max_val, max_attempts)."""
        print("\nSelect Difficulty Level:")
        print("  1. Easy   (Range: 1 - 50,  Attempts: 10)")
        print("  2. Medium (Range: 1 - 100, Attempts: 7)")
        print("  3. Hard   (Range: 1 - 200, Attempts: 5)")
        print("  4. Custom (Define your own range & attempts)")

        while True:
            choice = input("\nEnter choice (1-4): ").strip()
            if choice == "1":
                return 1, 50, 10
            elif choice == "2":
                return 1, 100, 7
            elif choice == "3":
                return 1, 200, 5
            elif choice == "4":
                return self.get_custom_settings()
            else:
                print("Invalid choice. Please select 1, 2, 3, or 4.")

    def get_custom_settings(self):
        """Prompt user for custom game parameters with validation."""
        while True:
            try:
                min_val = int(input("Enter minimum number (e.g., 1): ").strip())
                max_val = int(input("Enter maximum number (e.g., 500): ").strip())
                if min_val >= max_val:
                    print("Error: Maximum number must be greater than minimum.")
                    continue

                attempts = int(input("Enter max attempts (e.g., 8): ").strip())
                if attempts <= 0:
                    print("Error: Attempts must be at least 1.")
                    continue

                return min_val, max_val, attempts
            except ValueError:
                print("Invalid input. Please enter whole numbers only.")

    def play_round(self):
        """Execute one complete round of the game."""
        min_val, max_val, max_attempts = self.get_difficulty_settings()
        secret_number = random.randint(min_val, max_val)
        attempts_used = 0

        print(f"\nI'm thinking of a number between {min_val} and {max_val}.")
        print(f"You have {max_attempts} attempts to guess it. Good luck!\n")

        self.games_played += 1

        while attempts_used < max_attempts:
            remaining = max_attempts - attempts_used
            prompt = f"[Attempt {attempts_used + 1}/{max_attempts} | Remaining: {remaining}] Enter your guess: "

            try:
                guess = int(input(prompt).strip())
            except ValueError:
                print("Invalid input. Please enter an integer (no attempts lost).\n")
                continue

            if guess < min_val or guess > max_val:
                print(f"Out of range! Please guess between {min_val} and {max_val} (no attempts lost).\n")
                continue

            attempts_used += 1

            if guess == secret_number:
                print("\n🎉 Congratulations! You guessed the number correctly!")
                print(f"🎯 Secret Number: {secret_number}")
                print(f"⚡ Attempts used: {attempts_used}")

                self.games_won += 1
                if self.best_score is None or attempts_used < self.best_score:
                    self.best_score = attempts_used
                    print("🏆 New personal best score for this session!")
                return True

            diff = abs(secret_number - guess)
            proximity = ""
            if diff <= max(1, (max_val - min_val) // 20):
                proximity = " (🔥 Burning hot! You are super close!)"
            elif diff <= max(2, (max_val - min_val) // 10):
                proximity = " (🌡️ Warm! Getting closer!)"

            if guess < secret_number:
                print(f"📉 Too low!{proximity}\n")
            else:
                print(f"📈 Too high!{proximity}\n")

        print(f"\n❌ Game Over! You've run out of attempts.")
        print(f"💡 The secret number was: {secret_number}\n")
        return False

    def display_stats(self):
        """Display overall session statistics."""
        print("\n" + "=" * 45)
        print("             SESSION STATISTICS              ")
        print("=" * 45)
        print(f"  Games Played : {self.games_played}")
        print(f"  Games Won    : {self.games_won}")
        win_rate = (self.games_won / self.games_played * 100) if self.games_played > 0 else 0
        print(f"  Win Rate     : {win_rate:.1f}%")
        best = str(self.best_score) if self.best_score is not None else "N/A"
        print(f"  Best Score   : {best} attempt(s)")
        print("=" * 45 + "\n")

    def run(self):
        """Main game loop."""
        print("=" * 45)
        print("        🎮 NUMBER GUESSING GAME 🎮          ")
        print("=" * 45)

        while True:
            self.play_round()
            self.display_stats()

            replay = input("Would you like to play another round? (y/n): ").strip().lower()
            if replay not in ("y", "yes"):
                print("\nThanks for playing! See you next time! 👋")
                break


def main():
    game = NumberGuessingGame()
    try:
        game.run()
    except (KeyboardInterrupt, EOFError):
        print("\n\nGame exited. Goodbye!")
        sys.exit(0)


if __name__ == "__main__":
    main()
