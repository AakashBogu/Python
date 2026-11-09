# 🎮 Number Guessing Game

An interactive, feature-rich command-line number guessing game built in Python. The computer randomly picks a secret number, and you attempt to guess it within a limited number of tries using directional and proximity clues.

---

## ✨ Features

- **Difficulty Levels**:
  - **Easy**: Range `1 - 50` | 10 Attempts
  - **Medium**: Range `1 - 100` | 7 Attempts
  - **Hard**: Range `1 - 200` | 5 Attempts
  - **Custom**: Customize minimum, maximum, and allowed attempts
- **Smart Feedback**:
  - Direct feedback: Tells you if your guess is `Too high!` or `Too low!`
  - Proximity clues: Alerts when you are `🌡️ Warm` or `🔥 Burning hot!` (super close)
- **Input Validation**:
  - Handles non-numeric inputs and out-of-range guesses without penalizing or consuming your attempts.
- **Session Statistics**:
  - Tracks total games played, wins, win rate percentage, and your personal best score (fewest attempts).
- **Replayability**:
  - Play as many consecutive rounds as you want without restarting the program.

---

## 🗂️ Project Structure

```
NumberGuessingGame/
├── number_guessing_game.py   # Main executable game script
└── README.md                 # Project documentation
```

---

## ⚙️ Setup & How to Run

### 1. Requirements
- Python 3.6 or higher (uses standard library `random` and `sys`; zero external dependencies).

### 2. Run the Game

Navigate to the project folder and start the script:

```bash
python number_guessing_game.py
```

---

## 📄 Sample Gameplay

```text
=============================================
        🎮 NUMBER GUESSING GAME 🎮          
=============================================

Select Difficulty Level:
  1. Easy   (Range: 1 - 50,  Attempts: 10)
  2. Medium (Range: 1 - 100, Attempts: 7)
  3. Hard   (Range: 1 - 200, Attempts: 5)
  4. Custom (Define your own range & attempts)

Enter choice (1-4): 2

I'm thinking of a number between 1 and 100.
You have 7 attempts to guess it. Good luck!

[Attempt 1/7 | Remaining: 7] Enter your guess: 50
📉 Too low!

[Attempt 2/7 | Remaining: 6] Enter your guess: 75
📈 Too high! (🌡️ Warm! Getting closer!)

[Attempt 3/7 | Remaining: 5] Enter your guess: 68
🎉 Congratulations! You guessed the number correctly!
🎯 Secret Number: 68
⚡ Attempts used: 3
🏆 New personal best score for this session!

=============================================
             SESSION STATISTICS              
=============================================
  Games Played : 1
  Games Won    : 1
  Win Rate     : 100.0%
  Best Score   : 3 attempt(s)
=============================================
```

---

## 👤 Author

**Aakash Bogu**  
[GitHub](https://github.com/AakashBogu) · [LinkedIn](https://www.linkedin.com/in/aakashbogu/)
