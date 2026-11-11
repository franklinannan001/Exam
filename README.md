# Student Performance & Attendance Evaluator

A lightweight Python command-line application that evaluates student academic performance based on exam scores and class attendance. It validates user inputs, categorizes results, and provides automated feedback.

---

## Features

- **Input Validation:** Ensures scores and attendance percentages fall within valid bounds (`0` to `100`) and handles non-numeric entries gracefully.
- **Attendance Enforcement:** Automatically flags students who fail to meet the minimum `75%` attendance threshold.
- **Automated Grading:** Categorizes student results into **Distinction**, **Pass**, **Fail**, or **Disqualified**.
- **Contextual Remarks:** Generates tailored feedback messages based on the student's final result category.

---

## Grading & Attendance Criteria

The application evaluates student standing using the following rules in order of priority:

| Category | Attendance Requirement | Score Requirement | Automated Remark |
| :--- | :--- | :--- | :--- |
| **Disqualified** | `< 75%` | Any valid score | *Attendance requirement not met* |
| **Distinction** | `>= 75%` | `80 – 100` | *Outstanding work!* |
| **Pass** | `>= 75%` | `60 – 79` | *Solid effort* |
| **Fail** | `>= 75%` | `0 – 59` | *Needs improvement* |

> **Note:** Any score or attendance input outside the `0–100` range, or non-numeric input, causes the program to exit cleanly without producing output.

---

## Requirements

- **Python 3.10+** (Required for structural pattern matching via `match` / `case` statements)

---

## Getting Started

### 1. Clone the Repository
```bash
git clone https://github.com
cd your-repo-name
```

### 2. Run the Application
Replace `main.py` with your actual filename if different:
```bash
python main.py
```

---

## Usage Example

```text
What's your name: jane doe
What's your score: 85
What's your percentage attendance: 92.5
Jane Doe scored 85 with 92.5% attendance — Distinction. Outstanding work!
```

### Disqualified Example
```text
What's your name: john smith
What's your score: 90
What's your percentage attendance: 68
John Smith scored 90 with 68.0% attendance — Disqualified. Attendance requirement not met
```

---

## Project Structure

```text
.
├── main.py        # Core application logic and CLI prompts
└── README.md      # Project documentation
```

---
