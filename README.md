# Mini Vityarthi – Python Learning & Progress Tracker

A menu-driven, command-line application that helps beginners learn Python basics, practise with MCQs, track their progress, and earn a completion certificate. Built using only the Python standard library.

## Features

| Module | Description |
|---|---|
| **Learn Python** | 12 topics, each shown in four steps: Concept, Example, Explanation, Important Points |
| **Practice Problems** | 12 topics x 10 MCQs (120 questions), shuffled each time, with instant feedback and explanations |
| **Question Bank** | 40 MCQs by difficulty: Easy (15), Medium (15), Hard (10) |
| **View Progress** | Overall stats, topic-wise accuracy, mistake analysis, recommendations, bookmarked questions |
| **Report** | Overall report, topic performance, recommendations, and certificate generation |
| **Bookmarks** | Press `B` on any question to save it for later review |

### Topics covered
Variables, Data Types, Input and Output, Operators, If-Else, For Loop, While Loop, Functions, Lists, Tuples, Dictionaries, Modules.

## Project Structure

```
mini-vityarthi/
├── main.py            # Entry point and main menu
├── learn.py           # Learning content and topic viewer
├── practice.py        # Topic-wise practice mode
├── question_bank.py   # Difficulty-wise question bank
├── questions.py       # All MCQ data (PRACTICE_QUESTIONS, QUESTION_BANK)
├── progress_data.py   # File storage: save/read results and bookmarks, statistics
├── analysis.py        # View Progress menu
├── report.py          # Report menu and certificate
└── data/              # Auto-created at runtime
    ├── results.txt
    └── bookmarks.txt
```

## Requirements

- Python 3.6 or higher (uses f-strings)
- No external libraries needed

## How to Run

```bash
python main.py
```

Then choose an option from the main menu (0–5).

## How It Works

1. **Answering questions** – Options are numbered. Enter the option number to answer, `B` to bookmark, or `0` to quit. Each answer is saved immediately, so quitting midway keeps your results.
2. **Storage** – Results and bookmarks are stored in plain text files inside `data/`, with fields separated by `|`. The `clean()` function replaces `|` and newlines in text so the format never breaks.
3. **Statistics** – `get_statistics()` reads all results and computes attempted, correct, wrong, accuracy, and per-topic totals. Both Practice and Question Bank results are included.
4. **Recommendations** – Per-topic accuracy below 60% gives "focus/practice again", 60–79% gives "revise", 80% and above needs no action.
5. **Certificate** – Available after **at least 20 questions attempted** and **at least 60% overall accuracy**. Enter your name and a certificate with the date and accuracy is printed.

## Important Note

`main.py` calls `progress_data.reset_progress()` at startup, so **progress is cleared every time the program starts**. Each run is a fresh session. To keep progress between runs, remove that line from `main()`.

## Sample Menu

```
==================================================
            MINI VITYARTHI
     Python Learning & Progress Tracker
==================================================
1. Learn Python
2. Practice Problems
3. Question Bank
4. View Progress
5. Report
0. Exit
==================================================
```

## Possible Future Improvements

- Persist progress across sessions (optional reset)
- Multiple user profiles
- Timed quizzes and scoring streaks
- More topics (strings, file handling, OOP)
- GUI or web version

## Author

Aarjav
