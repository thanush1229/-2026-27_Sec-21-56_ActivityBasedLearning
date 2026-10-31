# Case Study 98: University Academic Progression Audit

## 1. Problem Statement
At the end of a semester, each student's marks, attendance and completed prerequisite courses are audited to decide whether the student can progress to the next semester. The report must name every outstanding requirement.

## 2. Objectives
- Combine tuples, lists and strings in one record-processing program.
- Apply three groups of conditions: subject marks, attendance and prerequisites.
- Use the in operator on tuples to check completed courses.
- Classify students as ELIGIBLE, CONDITIONAL or NOT ELIGIBLE.
- List every pending requirement and show summary counts.

## 3. Assumptions
- Pass mark per subject is 40; attendance must be at least 75%.
- Required prerequisites: MA101, PH101 and CS101.
- ELIGIBLE = no pending items. CONDITIONAL = attendance and prerequisites satisfied but one or two failed subjects (backlogs).
- Every other combination is NOT ELIGIBLE.
- Marks outside 0-100 are data errors and the record is not classified.

## 4. Algorithm
1. Store the subject names, the required courses and the student tuples.
2. For each student unpack (id, marks, attendance, completed courses).
3. If any mark is outside 0-100, print DATA ERROR and continue with the next student.
4. Collect failed subjects, missing prerequisites and attendance shortage into a pending list.
5. If pending is empty, status is ELIGIBLE.
6. Else if attendance is OK, no prerequisite is missing and failed subjects are at most 2, status is CONDITIONAL.
7. Otherwise status is NOT ELIGIBLE; print the status, the pending items, and the final summary counts.

## 5. Pseudocode
```text
START
FOR each student (id, marks, att, done)
    IF any mark < 0 OR > 100 THEN PRINT DATA ERROR ; CONTINUE
    failed <- subjects where mark < 40
    missing <- required courses not in done
    pending <- empty list
    IF att < 75 THEN add attendance message
    IF missing not empty THEN add prerequisite message
    IF failed not empty THEN add backlog message
    IF pending is empty THEN status <- ELIGIBLE
    ELSE IF att >= 75 AND missing is empty AND count(failed) <= 2 THEN status <- CONDITIONAL
    ELSE status <- NOT ELIGIBLE
    PRINT id, status, every pending item
END FOR
PRINT counts of each status
END
```

## 6. Flowchart
![Flowchart for Case Study 98](images/case98_flowchart.png)

## 7. Python Source Code
File: `programs/case98_progression_audit.py`

```python
# Case Study 98: University Academic Progression Audit
# Uses: tuples, lists, nested lists, loops, conditionals, strings, unpacking
# Rules: a subject is passed with >= 40; attendance must be >= 75;
#        all required prerequisite courses must be completed.
#   ELIGIBLE     : no failed subject, attendance OK, prerequisites OK
#   CONDITIONAL  : attendance OK, prerequisites OK, but 1-2 failed subjects (backlog)
#   NOT ELIGIBLE : anything else

PASS_MARK = 40
MIN_ATT = 75
MAX_BACKLOG = 2
subjects = ["Maths", "Physics", "Python", "English"]
required = ("MA101", "PH101", "CS101")

# (id, (marks per subject), attendance, (completed courses))
students = [
    ("R01", (72, 65, 80, 70), 90, ("MA101", "PH101", "CS101")),
    ("R02", (55, 35, 60, 48), 82, ("MA101", "PH101", "CS101")),
    ("R03", (70, 75, 68, 72), 70, ("MA101", "PH101", "CS101")),
    ("R04", (65, 70, 80, 75), 88, ("MA101", "CS101")),
    ("R05", (30, 28, 35, 60), 91, ("MA101", "PH101", "CS101")),
    ("R06", (80, 45, 39, 70), 60, ("MA101",)),
    ("R07", (40, 40, 40, 40), 75, ("CS101", "PH101", "MA101")),
    ("R08", (70, 80, 90, 101), 85, ("MA101", "PH101", "CS101")),   # invalid mark
]

count_e = 0
count_c = 0
count_n = 0

for st in students:
    sid, marks, att, done = st                 # unpacking
    pending = []                               # outstanding requirements

    # validate marks
    valid = True
    for m in marks:
        if m < 0 or m > 100:
            valid = False
    if not valid:
        print(sid, "-> DATA ERROR: marks must be 0-100")
        continue

    failed = []
    for k in range(len(marks)):
        if marks[k] < PASS_MARK:
            failed.append(subjects[k])
    if att < MIN_ATT:
        pending.append("attendance " + str(att) + "% (needs " + str(MIN_ATT) + "%)")
    missing = []
    for course in required:
        if course not in done:
            missing.append(course)
    if len(missing) > 0:
        pending.append("prerequisites missing: " + ", ".join(missing))
    if len(failed) > 0:
        pending.append("backlog in: " + ", ".join(failed))

    if len(pending) == 0:
        status = "ELIGIBLE"
        count_e += 1
    elif att >= MIN_ATT and len(missing) == 0 and len(failed) <= MAX_BACKLOG:
        status = "CONDITIONAL"
        count_c += 1
    else:
        status = "NOT ELIGIBLE"
        count_n += 1

    print(sid, "->", status)
    for p in pending:
        print("      -", p)

print("\n=== SUMMARY ===")
print("Eligible:", count_e, " Conditional:", count_c, " Not eligible:", count_n)
```

## 8. Test Cases
| ID | Input / Scenario | Expected Output |
|----|------------------|-----------------|
| T1 | R01: all marks >= 40, attendance 90, all prerequisites | ELIGIBLE |
| T2 | R02: Physics 35, attendance 82, prerequisites done | CONDITIONAL (backlog in Physics) |
| T3 | R03: attendance 70 | NOT ELIGIBLE (attendance 70% needs 75%) |
| T4 | R04: PH101 not completed | NOT ELIGIBLE (prerequisites missing: PH101) |
| T5 | R05: fails Maths, Physics, Python | NOT ELIGIBLE (3 backlogs) |
| T6 | R06: attendance 60, two prerequisites missing, one failed subject | NOT ELIGIBLE with all 3 reasons listed |
| T7 | R07: marks exactly 40 and attendance exactly 75 | ELIGIBLE (boundary values pass) |
| T8 | R08: English mark 101 | DATA ERROR: marks must be 0-100 |
| T9 | Summary | Eligible: 2, Conditional: 1, Not eligible: 4 |

*Run the program and type the input shown. For the data-driven programs, the test data is already stored in the program as lists/tuples; edit those lists to try your own cases.*

## 9. Sample Output
Full output saved in `outputs/case98_progression_audit_output.txt`.

```text
R01 -> ELIGIBLE
R02 -> CONDITIONAL
      - backlog in: Physics
R03 -> NOT ELIGIBLE
      - attendance 70% (needs 75%)
R04 -> NOT ELIGIBLE
      - prerequisites missing: PH101
R05 -> NOT ELIGIBLE
      - backlog in: Maths, Physics, Python
R06 -> NOT ELIGIBLE
      - attendance 60% (needs 75%)
      - prerequisites missing: PH101, CS101
      - backlog in: Python
R07 -> ELIGIBLE
R08 -> DATA ERROR: marks must be 0-100

=== SUMMARY ===
Eligible: 2  Conditional: 1  Not eligible: 4
```

## 10. Output Screenshot
> Add your own terminal screenshot as `docs/screenshots/case98_progression_audit_output.png` and the image below will appear:
>
> `![Output screenshot](screenshots/case98_progression_audit_output.png)`

## 11. Conclusion
The audit program reports every unmet requirement rather than only the first, which is what a student or advisor needs. The boundary cases (exactly 40 marks and exactly 75% attendance) confirm that the comparison operators are correct.
