# Lab 04 — Python Data Structures & Clean Code

## Concepts Practiced

- Lists
- Tuples
- Dictionaries
- Sets
- List comprehensions
- Dictionary comprehensions
- Set comprehensions
- enumerate()
- zip()
- Aliasing
- Shallow copying
- Deep copying
- Sorting
- Data structure selection
- Clean code
- File organization

## Tasks Completed

1. Working with Lists
2. Aliasing vs Copying
3. Tuples for Fixed Data
4. Dictionaries for Structured Records
5. Sets for Unique Labels & Validation
6. Comprehensions
7. enumerate() and zip()
8. Choosing the Right Data Structure
9. Prediction Analysis — Refactor and Extend
10. Per-Label Confidence Report

## Task 1 — Lists

I used a list because the accuracy values were stored in evaluation order.

I used append() to add one value and extend() to add multiple values.

I used sorted() instead of list.sort() because sorted() creates a new
sorted list and keeps the original evaluation order unchanged.

## Task 2 — Aliasing vs Copying

When I assigned:

processed_scores = original_scores

both variables referred to the same list. Therefore, changing one variable
also changed the other.

Using .copy() created a separate outer list.

However, .copy() is a shallow copy. For nested structures, the inner objects
can still be shared.

deepcopy() creates independent copies of nested objects as well.

This is important for data integrity in preprocessing, experiment tracking,
and model evaluation.

## Task 3 — Tuples

Tuples are useful for fixed groups of related values.

An image size such as (224, 224) is a good example because the width and
height represent one fixed pair.

A tuple can be used as a dictionary key because it is immutable and
hashable.

A list cannot be used as a dictionary key because lists are mutable and
unhashable.

## Task 4 — Dictionaries

I used a dictionary for model information because each value has a meaningful
field name such as name, version, accuracy, threshold, and status.

A nested dictionary was used for metrics because accuracy, precision, and
recall belong together.

## Task 5 — Sets

Sets are useful for unique labels and validation.

Set operations such as union, intersection, and difference directly express
the required operations.

Set membership checking is also generally faster than searching through a
list.

## Task 6 — Comprehensions

I used list comprehension for filtering and transforming scores.

I used dictionary comprehension for creating pass/fail status.

I used set comprehension for creating unique normalized labels.

## Task 7 — enumerate() and zip()

enumerate() was used to generate experiment numbers while iterating through
accuracy values.

zip() was used to compare predictions and actual labels at the same time.

## Task 8 — Data Structure Decisions

### Scenario A
List — evaluation order is important.

### Scenario B
Tuple — image size is a fixed pair.

### Scenario C
Dictionary — values have meaningful field names.

### Scenario D
Set — only unique class labels are required.

### Scenario E
List of dictionaries — many structured prediction records are stored.

### Scenario F
Set — set difference directly finds unexpected labels.

## Task 9 — Clean Code

The original code used unclear variable names such as x, y, z, and d.

I replaced them with meaningful names such as prediction_records,
high_confidence_predictions, and label_counts.

The confidence threshold was stored in the named constant MIN_CONFIDENCE.

The program was separated into preprocessing.py, analysis.py, and main.py.

preprocessing.py handles filtering, completeness checking, and label
normalization.

analysis.py handles counting, unique labels, unexpected labels, averages,
and top predictions.

main.py coordinates the workflow and displays the final report.

## Incomplete Records

Incomplete records are reported instead of silently skipped because silently
dropping data could hide a data-quality problem.

In Task 9, record 9 is missing the confidence field, so it is skipped and its
ID is reported.

## Raw Data Integrity

normalize_labels() returns new records instead of modifying the input
records.

Record 8 originally contains the label "Spam". After normalization, the
cleaned version contains "spam", while the original record still contains
"Spam".

## Optional Label Report

I implemented the label confidence grouping using both a normal dictionary
and collections.defaultdict(list).

The defaultdict version is shorter because it automatically creates an empty
list for a new label.

Counter was used to find the most common label.

## Testing

I tested:

- Normal values
- Empty collections
- Duplicate values
- Boundary values
- Unexpected labels
- Missing dictionary fields
- Invalid nested data

## What I Found Difficult

Understanding the difference between aliasing, shallow copying, and deep
copying was initially difficult.

Choosing the correct data structure for each problem also required careful
thinking.

## What I Learned

I learned how to use lists, tuples, dictionaries, sets, comprehensions,
enumerate(), zip(), shallow copies, and deep copies.

I also learned how to organize data-processing code into separate modules
and refactor unclear code into cleaner code.

## AI Engineering Relevance

Data structures are important in AI because datasets, model results,
configuration, labels, and prediction records must be represented clearly.

Clean code makes AI data-processing programs easier to test, maintain, and
extend.

## AI Usage Log

### Tool Used

ChatGPT

### What I Asked

I asked for help understanding and solving Lab 04.

### What I Used

I used explanations and code examples to understand the required Python
data structures and clean-code concepts.

### What I Verified or Changed Myself

I reviewed the code, ran the programs, checked the expected outputs, and
verified the required test cases.