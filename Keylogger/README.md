# Python Keylogger

## Description
This project is a simple Python keylogger that records keyboard inputs.

## Features
- Records keystrokes
- Saves them into a log file
- Built using Python



# 🔑 Python Keylogger

A simple keylogger built with Python using the `pynput` library. Every key you press gets captured and saved to a log file — great for understanding how input monitoring works under the hood.

---

## What It Does

- Listens for every key you press (letters, numbers, special keys — all of it)
- Saves the keystrokes to a file called `log.txt` in real time
- Prints each keystroke to the terminal so you can watch it live
- Stops cleanly when you press `Esc`

---

## Requirements

You just need Python installed and one library:

```bash
pip install pynput
```

---

## How to Run

```bash
python keylogger.py
```

Once it's running, start typing. You'll see each key printed in the terminal, and everything gets saved to `log.txt` automatically.

Press **Esc** whenever you want to stop.

---

## Project Structure

```
keylogger/
│
├── keylogger.py    # Main script
└── log.txt         # Generated automatically when you run the script
```

---

## How It Works (Quick Breakdown)

- `on_press(key)` — fires every time a key is pressed, appends it to a list, then writes to the file
- `write_file(keys)` — opens `log.txt` and writes all captured keys, separated by spaces for readability
- `on_release(key)` — fires on key release; if the key is `Esc`, it stops the listener
- The `Listener` from `pynput` ties everything together and runs in the background
