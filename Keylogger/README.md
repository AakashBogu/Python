 🔍 Python Keyboard Activity Monitor

A lightweight keyboard activity monitor built with Python and `pynput`. Captures and logs keystrokes in real time — built for learning how OS-level input event handling works.

> ⚠️ **Ethical Use Only** — This tool is intended strictly for educational purposes on your own machine. Using it to monitor others without consent is illegal and unethical.

---

## 📸 Demo link here

<!--(https://www.linkedin.com/posts/aakashbogu_python-cybersecurity-ethicalhacking-activity-7440443988161077248-nE0k?utm_source=share&utm_medium=member_desktop&rcm=ACoAAF158sgBMEvNNv423OKBLZmjX0Sso97YsHI)-->


---

## 🧠 How It Works

Your OS exposes a stream of input events. `pynput` taps into that stream via platform-specific APIs:

| Platform | Underlying API |
|----------|----------------|
| Windows  | Win32 API      |
| macOS    | Quartz / Core Graphics |
| Linux    | Xlib           |

The script registers two event callbacks:

- **`on_press(key)`** — fires the moment a key is pressed down; writes the key to a log file
- **`on_release(key)`** — fires when the key comes back up; stops the listener when `ESC` is pressed

Alphanumeric keys carry a `.char` attribute (e.g., `'a'`, `'5'`). Special keys like `Shift`, `Enter`, and `Esc` don't — so they're caught via `AttributeError` and written in bracket notation: `[Key.enter]`.

---

## 🗂️ Project Structure

```
keylogger/
├── keylogger.py   # Main script
├── log.txt        # Output log file (auto-created on first run)
└── README.md
```

---


python keylogger.py
```

Keystrokes are logged to `log.txt` in real time. Press **`ESC`** to stop.

---

## 📄 Sample Output (`log.txt`)

```
hello [Key.space] everyone [Key.enter] this [Key.space] is [Key.space] a [Key.space] test [Key.esc]
```

---

## 💡 What This Teaches

- How operating systems expose input events to user-space programs
- Event-driven programming with callback functions
- Handling exceptions for type-based branching 
- Real-time file I/O with append mode

This is the same core mechanism used in:
- Accessibility tools (screen readers, switch access)
- Hotkey managers (AutoHotkey, Hammerspoon)
- Automation frameworks (PyAutoGUI, Selenium)

---

## 🛠️ Built With

- **Python 3**
- **[pynput](https://pypi.org/project/pynput/)** — cross-platform keyboard/mouse listener
](https://www.linkedin.com/in/aakashbogu/)
---

## 👤 Author

**Aakash** — CS undergrad | AIML enthusiast  
[LinkedIn](https://www.linkedin.com/in/aakashbogu/)) · [GitHub](https://github.com/aakashbogu)
