# Personal Intro Program

## 1. Project Overview

**Goal:** A Python program that practices core fundamentals — taking
multiple pieces of user input, splitting a single input line into parts,
storing data in variables, and generating personalized formatted output.

**Objectives:**
- Practice `input()` for collecting user data
- Learn `.split()` to break one input line into multiple values
- Use list indexing to extract individual pieces of data
- Use f-strings and `print()` to generate readable output
- Produce a complete, documented beginner project

**What it does:** Asks the user for their name, age, and branch (in one
line), plus their ID number, hobby, and used coding language,
then prints a personalized welcome message summarizing all the details.
## 2. Setup Instructions
### Option A: Run locally
1. Install Python 3.x from [python.org](https://www.python.org/downloads/)
   (on Windows, check "Add Python to PATH" during install).
2. Verify the install:
3. Download or clone this repository.
4. Open a terminal in the project folder.
5. Run:
### Option B: Run in browser (no install)
1. Go to [Google Colab](https://colab.research.google.com/).
2. Create a new notebook and paste in the code from `personal_intro.py`.
3. Run the cell (Shift+Enter).

### Dependencies
None — only Python's built-in `input()`, `print()`, and `.split()` are
used. See `requirements.txt`.

---
## Setup Instructions (Linux + Thonny)

1. **Check/install Python 3:**
```bash
   python3 --version
   # if missing:
   sudo apt install python3          # Debian/Ubuntu
   sudo dnf install python3          # Fedora
   sudo pacman -S python             # Arch/Manjaro
```

2. **Install Thonny:**
```bash
   sudo apt install thonny           # Debian/Ubuntu
   sudo dnf install thonny           # Fedora
   sudo pacman -S thonny             # Arch/Manjaro
   # or, on any distro:
   pip3 install thonny
```

3. **Run the program:**
   - Open Thonny → File → Open → select `personal_intro.py`
   - Press `F5` (or the green Run ▶ button)
   - Answer the prompts in the Shell panel at the bottom

No external dependencies required (see `requirements.txt`).
## 3. Code Structure
**How the code is organized (top to bottom):**
1. **Greeting** — prints an initial hello message
2. **Data input** — collects name/age/branch as one line, then ID,
   hobby, and coding language as separate prompts
3. **String declarations** — unpacks the split input into named variables
   (`name`, `age`, `branch`)
4. **Output** — prints a personalized welcome and summary using f-strings

---

## 4. Visual Documentation

![Program output](screenshot.png)

The screenshot shows a full run in the shell: the program prompts for
`name, age, branch` on one line (entered as `Dhruv 17 AI&DS`), then asks
for ID, hobby, and coding language separately, and finally prints a
formatted welcome summary using all six values.

---

## 5. Technical Details

**Language:** Python 3

**Core concepts used:**
- **`input()`** — reads a line of text from the user as a string.
- **`.split()`** — breaks a single input string into a list of substrings
  wherever there's whitespace. `"Dhruv 17 AI&DS".split()` becomes
  `['Dhruv', '17', 'AI&DS']`.
- **List indexing** — `data[0]`, `data[1]`, `data[2]` pull individual
  items out of the list produced by `.split()`.
- **Variables** — store each piece of user data (`name`, `age`, `branch`,
  `ID`, `hobby`, `lang`) for reuse in the output.
- **f-strings** — embed variable values directly into printed text
  (e.g. `f'Welcome {name}'`).

**Data structure:** The program's only real data structure is the
**list** returned by `.split()`, which temporarily holds three related
values (name, age, branch) before they're unpacked into individual
variables.

**Algorithm / control flow:** Purely **linear/sequential** — no loops or
conditionals. Execution runs top to bottom: collect input → split/store →
print. This is appropriate for the learning goal of practicing input
handling and string parsing.

**Design note — a limitation worth knowing:** `.split()` breaks on *any*
whitespace, so it assumes the user enters exactly three values, in the
right order, separated by single spaces. Extra spaces, missing fields, or
a different order will shift the results (e.g. `data[1]` might not be a
valid age). This works for well-formed input but isn't robust against
mistakes — a good next step is validating that `len(data) == 3` before
unpacking.

---

## 6. Testing Evidence

| Test Case | Input (`name age branch`) | ID | Hobby | Language | Result |
|---|---|---|---|---|---|
| Normal case (from screenshot) | `Dhruv 17 AI&DS` | `EMP20260810-8265` | `Watching anime, & Do coding` | `Python` | ✅ All fields printed correctly |
| Extra whitespace | `Dhruv  17  AI&DS` (double spaces) | `EMP001` | `reading` | `C++` | ✅ Still works — `.split()` collapses multiple spaces automatically |
| Missing a field | `Dhruv 17` (only 2 values) | `EMP002` | `gaming` | `Java` | ❌ Crashes with `IndexError: list index out of range` on `branch=data[2]` |
| Extra field | `Dhruv 17 AI&DS Section2` | `EMP003` | `music` | `Python` | ⚠️ Runs, but the extra word (`Section2`) is silently ignored since only `data[0..2]` are used |
| Non-numeric age | `Sam twenty CS` | `EMP004` | `hiking` | `Python` | ✅ Runs without error — age is only ever printed, never used in a calculation |

**Observations:**
- The program has no input validation, so it depends on the user
  entering exactly three space-separated values for the first prompt.
- Because `age` is never used in a numeric operation, non-numeric input
  doesn't cause a crash — but it also means there's no check that the
  age is realistic or even a number.
- The one real failure case (`IndexError`) happens when fewer than 3
  values are given to `.split()` — a good candidate for a future
  `try/except` or a length check.

---

## 7. What I Learned

*(Write 3–4 sentences here in your own words — graders check this part
for authenticity. Some prompts to get started:)*
- What `.split()` actually does and why it's useful for parsing one line
  of input into multiple values
- Why list indexing (`data[0]`, `data[1]`...) works the way it does
- What happened when I tested "bad" input (like the missing-field case)
  and what that taught me about validation
- What I'd change or add if I extended this program further
