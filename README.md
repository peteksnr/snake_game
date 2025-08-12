# Snake Game 🐍

A simple, classic Snake game built with Python and `turtle`. The game saves and loads the **high score** using a plain text file named `data.txt` so your best run sticks between sessions.

## 🎯 Features
- Smooth snake movement and food spawning
- Score and **persistent high score** display
- Game over + automatic reset to play again
- Clean, beginner‑friendly code split across modules

## 🕹️ Controls
- **Arrow Keys** — Move Up/Down/Left/Right

## 📂 Project Structure
```
.
├── main.py            # Entry point: sets up the screen + game loop
├── snake.py           # Snake class: movement, growth, collision with tail
├── food.py            # Food class: random placement + refresh
├── score_board.py     # Scoreboard class: score & high score logic
└── data.txt           # Stores the persistent high score (single integer)
```
> If `data.txt` is missing the game will create it on first run (or you can create it yourself with `0`).

## 💾 High Score Persistence (`data.txt`)
- The file **`data.txt`** holds a single number—the **highest score** ever achieved.
- On game start, the scoreboard **reads** the number and displays it.
- When you beat your high score and the round ends, the scoreboard **writes** the new value back to `data.txt`.
- If the file is empty or corrupted, the code should fall back to `0` (you can also manually fix it by putting `0`).

### Example contents of `data.txt`
```
0
```
> Keep it as a single line containing just a number.

## 🧰 Requirements
- **Python 3.8+** (works great with modern Python versions)
- No third‑party packages are required; uses Python’s built‑in `turtle` module

## 🚀 Run Locally
1. Make sure the files are in the same folder:
   - `main.py`, `snake.py`, `food.py`, `score_board.py`, `data.txt`
2. (Optional) Create and activate a virtual environment:
   ```bash
   python -m venv venv
   # macOS/Linux
   source venv/bin/activate
   # Windows (PowerShell)
   .\venv\Scripts\Activate.ps1
   ```
3. Run the game:
   ```bash
   python main.py
   ```

## ⚙️ Customization
- **Speed:** Look for `screen.tracer()`, `screen.update()`, or a `time.sleep()` delay in `main.py` and tweak the delay between frames.
- **Food color/shape:** Adjust in `food.py` via `shape()`, `color()`, or `shapesize()`.
- **Snake starting size & growth:** Often controlled in `snake.py` via a starting list of segments and a `extend()` method.
- **Edge behavior:** Change from “game over on wall hit” to “wrap-around” by editing the wall boundary checks in `main.py` (or a collision helper).

## 🧪 Common Issues & Fixes
- **The window doesn’t open / crashes immediately**  
  Ensure you’re running `python main.py` in a **desktop** environment (the `turtle` module needs a GUI). It won’t run in a headless server or some online IDEs.
- **Nothing happens when pressing keys**  
  Confirm that `screen.listen()` is called and key bindings like `screen.onkey(snake.up, "Up")` exist in `main.py`.
- **High score not saving**  
  Check write permissions in the project folder and that `score_board.py` writes to **`data.txt`** in the **same directory**. Also verify the file only contains a number.

## 🧑‍💻 Code Entry Points (Typical Flow)
1. `main.py` creates the `Screen`, then instantiates `Snake`, `Food`, and `Scoreboard`.
2. A game loop updates the screen, moves the snake, and checks collisions:
   - **Food collision** → Extend snake + increase score + refresh food
   - **Wall collision** or **Tail collision** → Reset score and snake; update high score if beaten

---

