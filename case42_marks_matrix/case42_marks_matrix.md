# Case Study 42: Student Marks Matrix Analysis

## 1. Problem Statement
Marks of several students in several subjects are stored as a matrix (nested list). The program must validate the matrix, compute row-wise and column-wise statistics, find top performer(s) and identify subjects whose class average is low.

## 2. Objectives
- Represent a table as a nested list and access elements with marks[row][col].
- Use nested loops for row-wise and column-wise calculations.
- Find highest, lowest, totals and averages without built-in helper functions.
- Handle ties for the top performer.
- Skip invalid rows and report the problem.

## 3. Assumptions
- Valid marks are integers from 0 to 100.
- Pass mark is 40 per subject.
- A subject has LOW AVERAGE if the class average is below 65.
- Rows with any invalid mark are excluded from every statistic.
- Top performer(s) = all students whose total equals the highest total.

## 4. Algorithm
1. Store student names, subject names and the marks matrix.
2. Check every mark; remember the indexes of rows that are fully valid and report the others.
3. For each valid row compute total, average and number of failed subjects; keep the best total.
4. For each subject column compute average, highest and lowest over the valid rows.
5. If the column average is below the limit mark the subject LOW AVERAGE.
6. Print every student whose total equals the best total.
7. Print the list of low-average subjects.

## 5. Pseudocode
```text
START
READ names, subjects, marks matrix
FOR each row r
    IF any marks[r][c] < 0 OR > 100 THEN report ; ELSE add r to valid_rows
END FOR
best <- -1
FOR each r in valid_rows
    total <- 0 ; failed <- 0
    FOR each column c
        total <- total + marks[r][c]
        IF marks[r][c] < 40 THEN failed <- failed + 1
    END FOR
    save total ; IF total > best THEN best <- total
    PRINT name, total, total / number of subjects, failed
END FOR
FOR each column c
    average, highest, lowest over valid rows
    IF average < 65 THEN add subject to low list
END FOR
PRINT all students with total = best
PRINT low-average subjects
END
```

## 6. Flowchart
![Flowchart for Case Study 42](images/case42_flowchart.png)

## 7. Python Source Code
File: `programs/case42_marks_matrix.py`

```python
# Case Study 42: Student Marks Matrix Analysis
# Uses: nested lists, nested loops, conditionals, lists

students = ["Anil", "Bhavna", "Charan", "Divya", "Eswar", "Farah"]
subjects = ["Maths", "Physics", "Python", "English"]
marks = [
    [78, 65, 90, 70],
    [92, 88, 95, 85],
    [45, 38, 52, 60],
    [92, 88, 95, 85],
    [60, 42, 48, 55],
    [101, 70, 80, 75],     # invalid: mark above 100
]
PASS = 40
LOW_AVG = 65

# --- validate matrix ---
valid_rows = []
for r in range(len(marks)):
    ok = True
    for c in range(len(subjects)):
        if marks[r][c] < 0 or marks[r][c] > 100:
            print("Invalid mark", marks[r][c], "for", students[r], "in", subjects[c], "-> row skipped")
            ok = False
    if ok:
        valid_rows.append(r)

# --- row-wise statistics ---
print("\n=== STUDENT-WISE ===")
print("Name     Total  Average  Failed subjects")
best_total = -1
totals = []
for r in valid_rows:
    total = 0
    failed = 0
    for c in range(len(subjects)):
        total += marks[r][c]
        if marks[r][c] < PASS:
            failed += 1
    totals.append(total)
    if total > best_total:
        best_total = total
    print(students[r].ljust(8), str(total).rjust(5), str(round(total / len(subjects), 2)).rjust(8), "   ", failed)

# --- column-wise statistics ---
print("\n=== SUBJECT-WISE ===")
print("Subject   Average  Highest  Lowest  Status")
low_subjects = []
for c in range(len(subjects)):
    s = 0
    high = marks[valid_rows[0]][c]
    low = marks[valid_rows[0]][c]
    for r in valid_rows:
        s += marks[r][c]
        if marks[r][c] > high:
            high = marks[r][c]
        if marks[r][c] < low:
            low = marks[r][c]
    avg = round(s / len(valid_rows), 2)
    if avg < LOW_AVG:
        status = "LOW AVERAGE"
        low_subjects.append(subjects[c])
    else:
        status = "OK"
    print(subjects[c].ljust(9), str(avg).rjust(7), str(high).rjust(8), str(low).rjust(7), " ", status)

# --- top performers (all students sharing the best total) ---
print("\nHighest total:", best_total)
print("Top performer(s):", end=" ")
for k in range(len(valid_rows)):
    if totals[k] == best_total:
        print(students[valid_rows[k]], end="  ")
print()
print("Subjects with low average:", low_subjects)
```

## 8. Test Cases
| ID | Input / Scenario | Expected Output |
|----|------------------|-----------------|
| T1 | Farah has a mark of 101 | Row skipped; message printed |
| T2 | Anil: 78, 65, 90, 70 | Total 303, average 75.75, 0 failed |
| T3 | Bhavna and Divya both score 360 | Both printed as top performers |
| T4 | Charan has Physics 38 | 1 failed subject |
| T5 | Maths column (valid rows) | Average 73.4, highest 92, lowest 45 |
| T6 | Physics column | Average 64.2 -> LOW AVERAGE |
| T7 | Subjects with low average | ['Physics'] |

*Run the program and type the input shown. For the data-driven programs, the test data is already stored in the program as lists/tuples; edit those lists to try your own cases.*

## 9. Sample Output
Full output saved in `outputs/case42_marks_matrix_output.txt`.

```text
Invalid mark 101 for Farah in Maths -> row skipped

=== STUDENT-WISE ===
Name     Total  Average  Failed subjects
Anil       303    75.75     0
Bhavna     360     90.0     0
Charan     195    48.75     1
Divya      360     90.0     0
Eswar      205    51.25     0

=== SUBJECT-WISE ===
Subject   Average  Highest  Lowest  Status
Maths        73.4       92      45   OK
Physics      64.2       88      38   LOW AVERAGE
Python       76.0       95      48   OK
English      71.0       85      55   OK

Highest total: 360
Top performer(s): Bhavna  Divya  
Subjects with low average: ['Physics']
```

## 10. Output Screenshot
> Add your own terminal screenshot as `docs/screenshots/case42_marks_matrix_output.png` and the image below will appear:
>
> `![Output screenshot](screenshots/case42_marks_matrix_output.png)`

## 11. Conclusion
The program shows how a matrix can be analysed both by rows and by columns using nested loops. Handling invalid rows and ties makes the results trustworthy, and the low-average check highlights the subject that needs attention.
