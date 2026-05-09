# Number Guessing Game 🎯

A simple Python game with two playing modes:

1. **User Guesses the Number**
2. **Computer Guesses the Number**

This project is designed for beginners to practice Python fundamentals such as loops, conditionals, user input, and the Binary Search algorithm.

---

## Features

* Random number generation using Python's `random` module.
* Two interactive game modes.
* Tracks the number of attempts.
* Computer uses Binary Search to guess efficiently.
* Input validation for incorrect choices.

---

## Game Modes

### 1. User Guesses the Number

The computer selects a random number between 1 and 100.

The player keeps guessing until the correct number is found.

After each guess, the game displays:

* `Too low! Try again.`
* `Too high! Try again.`

When the player guesses correctly, the game shows the total number of attempts.

---

### 2. Computer Guesses the Number

The player thinks of a number between 1 and 100.

The computer guesses the number using the Binary Search algorithm.

The player responds with:

* `h` → The correct number is higher.
* `l` → The correct number is lower.
* `y` → The guess is correct.

The program displays how many attempts the computer needed.

---

## Technologies Used

* Python 3
* `random` module

---

## How to Run

1. Make sure Python is installed.
2. Save the code in a file named `main.py`.
3. Run the program:

```bash id="6f2d1a"
python main.py
```

---

## Example Output

```text id="0wcc3m"
Welcome to the Number Guessing Game!

Who guesses, computer or user? (c for computer, u for user)
enter: u

Guess a number between 1 and 100: 50
Too low! Try again.
Guess a number between 1 and 100: 75
Too high! Try again.
Guess a number between 1 and 100: 63

Congratulations! You guessed the number 63 in 3 attempts.
```

---

## Project Structure

```text id="6h6g8o"
number-guessing-game/
│
├── main.py
└── README.md
```

---

## Concepts Practiced

* Variables
* User input
* `if`, `elif`, `else`
* `while` loops
* Random number generation
* Binary Search
* Counting attempts

---

## Future Improvements

* Add difficulty levels.
* Save the best score.
* Add a graphical interface with Tkinter.
* Handle invalid numeric input with `try/except`.

---

## Author
Shimaa.M.Zakaria
