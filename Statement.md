# Project Statement

## Project Title
**Mini Vityarthi – Python Learning & Progress Tracker**

## Problem Statement
Beginners learning Python often struggle because study material, practice questions, and feedback are scattered across different places. They cannot easily see which topics they are weak in, review their mistakes, or measure how much they have improved. Without structured practice and clear feedback, learners lose motivation and repeat the same errors.

## Objective
To develop a simple, interactive, console-based application in Python that combines learning, practice, and progress tracking in one place, so a beginner can:

1. Learn core Python concepts in small, easy steps.
2. Practise with multiple-choice questions and get instant feedback.
3. Review mistakes with explanations and bookmark difficult questions.
4. Identify weak topics through accuracy analysis and recommendations.
5. Earn a certificate once a minimum performance level is reached.

## Scope
- **Content:** 12 Python fundamentals topics (Variables to Modules).
- **Practice:** 120 topic-wise MCQs (10 per topic) and a 40-question bank graded Easy, Medium, and Hard.
- **Tracking:** Every answer is stored in text files; statistics are computed per topic and overall.
- **Platform:** Command-line, runs on any system with Python 3.
- **Out of scope:** Graphical interface, online accounts, multi-user support, and persistent progress across sessions (progress resets on each launch).

## Functional Requirements
| # | Requirement |
|---|---|
| 1 | Display a main menu with Learn, Practice, Question Bank, View Progress, Report, and Exit |
| 2 | Present each learning topic as Concept, Example, Explanation, and Key Points |
| 3 | Serve shuffled MCQs and validate user input |
| 4 | Show correct answer and explanation for wrong responses |
| 5 | Allow bookmarking and quitting at any question |
| 6 | Save results and bookmarks to files |
| 7 | Show overall progress, topic-wise accuracy, and mistake analysis |
| 8 | Recommend topics to focus on (below 60%) or revise (60–79%) |
| 9 | Generate a certificate for 20 or more attempts with 60% or higher accuracy |

## Non-Functional Requirements
- Simple, beginner-friendly text interface
- Modular code split across separate files
- Robust input handling (invalid entries do not crash the program)
- No external dependencies

## Technologies Used
- **Language:** Python 3
- **Modules:** `os`, `random`, `datetime` (standard library only)
- **Storage:** Plain text files with `|`-separated fields

## Module Design
| File | Responsibility |
|---|---|
| `main.py` | Main menu and program flow |
| `learn.py` | Learning content and display |
| `practice.py` | Topic-wise practice |
| `question_bank.py` | Difficulty-wise questions |
| `questions.py` | Question data |
| `progress_data.py` | File handling and statistics |
| `analysis.py` | Progress views and mistake analysis |
| `report.py` | Reports and certificate |

## Expected Outcome
A working application that lets a learner study a topic, test themselves, see exactly where they are weak, and receive a certificate, all from a single program, improving both understanding and motivation.

## Conclusion
Mini Vityarthi shows how basic Python concepts such as functions, loops, dictionaries, file handling, and modules can be combined into a practical educational tool that helps beginners learn effectively and track their growth.
