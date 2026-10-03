# Lab 03 — Functions, Modules, Exceptions, Debugging & OOP

## Concepts Practiced

- Functions
- Parameters and return values
- Local and global scope
- Modules and imports
- `__name__ == "__main__"`
- Exception handling
- `try`, `except`, `else`, and `finally`
- Debugging
- Classes and objects
- Attributes and methods
- Refactoring
- Separation of concerns

## Tasks Completed

1. Function Design & Reuse
2. Scope & Hidden State
3. Create and Use Your Own Module
4. Exception Handling
5. Debugging Challenge
6. ScoreAnalyzer Class
7. Refactor Procedural Script into Modules + Class
8. Threshold Classifier Challenge

## Task 2 — Scope

The variable inside the function is local, while the variable outside the
function is global.

The local variable exists only inside the function. The global variable is
defined outside the function and can be accessed from the broader program.

Explicit parameters make functions easier to reuse and test because required
values are passed directly to the function.

## Task 4 — Exception Handling Test Cases

| Case | Input | Expected Result | Actual Result |
|---|---|---|---|
| Valid | 80, 100 | 80% | 80% |
| Negative | -5, 100 | Error | Error |
| Obtained greater than total | 120, 100 | Error | Error |
| Zero total | 80, 0 | Error | Error |
| Non-numeric | abc, 100 | Error | Error |

## Task 5 — Debugging Notes

### Bug 1

The original code used:

`total = score`

This replaced the previous total instead of adding each score.

It was changed to:

`total += score`

### Bug 2

The conditions in `classify()` were in the wrong order.

The program checked `average >= 50` before `average >= 85`.
Therefore, an excellent score would be classified as Pass.

The condition for Excellent was moved before the condition for Pass.

### Corrected Output

Average: 75.0

Result: Pass

## Task 6 — Design Decisions

A class was used because the score data and operations on that data belong
together.

The `ScoreAnalyzer` object stores the scores in `self.scores` and provides
methods for cleaning, calculating the average, counting values above a
threshold, and creating a summary.

## Task 7 — Design Decisions

The program was divided into separate responsibilities.

`preprocessing.py` is responsible for cleaning the raw scores.

`analyzer.py` contains the ScoreAnalyzer class and analysis operations.

`main.py` coordinates the complete workflow.

This separation makes the program easier to understand, test, and maintain.

## What I Found Difficult

Understanding the difference between functions, modules, and classes was
initially difficult.

Debugging the incorrect average calculation and condition order also required
careful tracing.

## What I Learned

I learned how to create reusable functions, organize code into modules,
handle exceptions, debug logic errors, and create classes and objects.

I also learned how to separate different responsibilities into different
files.

## AI Engineering Relevance

Functions, modules, exceptions, debugging, and object-oriented programming
help make larger AI programs easier to understand, test, reuse, and maintain.

## AI Usage Log

### Tool Used

ChatGPT

### What I Asked

I asked for explanations and help understanding and solving the Week 3 tasks.

### What I Used

I used explanations and code examples to understand functions, modules,
exceptions, debugging, classes, and refactoring.

### What I Verified or Changed Myself

I reviewed the code, ran the programs, checked the outputs, and verified the
required test cases.