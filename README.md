# Python Practice Assignment

This repository contains solutions to two Python practice problems.

## Problem 1: Personal Information & Simple Calculator

**File:** `personal_calculator.py`

This program:
- Asks the user for their name and age.
- Takes two numbers as input.
- Calculates addition, subtraction, multiplication, and division.
- Displays the personal information and calculation results using f-strings.

### Example output

```text
Enter your name: Rahim
Enter your age: 22
Enter first number: 20
Enter second number: 10

Hello, Rahim!
Your age is 22.
Addition: 30
Subtraction: 10
Multiplication: 200
Division: 2.0
```

> Note: The program should handle division by zero to avoid a `ZeroDivisionError`.

## Problem 2: Student Grade Calculator

**File:** `grade_calculator.py`

This program:
- Takes the student's name as input.
- Takes marks for Math, English, and Python.
- Checks that each subject's marks are between 0 and 100.
- Calculates the average marks.
- Assigns a grade based on the average.
- Displays the student's name, average marks (to two decimal places), and final grade.

### Grade scale

| Average marks | Grade |
|---|---|
| 80–100 | A+ |
| 70–79 | A |
| 60–69 | A- |
| 50–59 | B |
| 40–49 | C |
| Below 40 | F |

### Example output

```text
Enter student name: Rahim
Enter Math marks: 85
Enter English marks: 75
Enter Python marks: 90

Student Name: Rahim
Average Marks: 83.33
Final Grade: A+
```

## Repository structure

```text
python-practice-assignment/
├── personal_calculator.py
├── grade_calculator.py
└── README.md
```

## How to run

Make sure Python 3 is installed. Open a terminal in the repository folder and run:

```bash
python personal_calculator.py
```

To run the student grade calculator:

```bash
python grade_calculator.py
```

## GitHub submission

1. Create a **public** GitHub repository named `python-practice-assignment`.
2. Upload `personal_calculator.py`, `grade_calculator.py`, and this `README.md` file.
3. Copy the repository URL and submit it in the assignment submission box.