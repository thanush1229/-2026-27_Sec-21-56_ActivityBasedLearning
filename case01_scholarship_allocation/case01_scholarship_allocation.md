# Case Study 1: University Scholarship Allocation

## 1. Problem Statement
A university offers a limited number of scholarships. Each applicant has marks in five subjects, an attendance percentage and a family income. The system must decide who is eligible, rank the eligible students, and resolve ties using fixed rules so that the same data always produces the same ranking.

## 2. Objectives
- Apply four eligibility rules (aggregate, subject-wise minimum, attendance, income) using conditional statements.
- Store applicants as tuples in a list and unpack them with tuple unpacking.
- Rank eligible students by sorting tuple keys with nested loops (bubble sort).
- Resolve ties with a predefined, deterministic order.
- Report the exact reason(s) for every rejection.

## 3. Assumptions
- Aggregate = average of the five subject marks (out of 100).
- Policy values: aggregate >= 60, every subject >= 40, attendance >= 75, income <= Rs 3,00,000, quota = 3.
- Tie-break order: higher aggregate, then lower income, then higher attendance, then smaller student ID.
- All data is hypothetical and typed into the program as a list of tuples.

## 4. Algorithm
1. Define policy constants and the applicant list.
2. For each applicant, unpack the tuple and compute the total, aggregate and lowest subject mark.
3. Check the four rules; add a reason string for every rule that fails.
4. If there are no reasons, add the sort key (-aggregate, income, -attendance, id, name) to the eligible list; otherwise print the reasons.
5. Bubble-sort the eligible list (tuples compare element by element, which applies the tie-break order automatically).
6. Walk through the sorted list: ranks 1..QUOTA are AWARDED, the rest are WAITING LIST.
7. Print the rank table.

## 5. Pseudocode
```text
START
SET MIN_AGG=60, MIN_SUB=40, MIN_ATT=75, MAX_INCOME=300000, QUOTA=3
FOR each applicant (id, name, marks, att, income)
    total <- sum of marks ; lowest <- smallest mark
    aggregate <- total / number of subjects
    reasons <- empty list
    IF aggregate < MIN_AGG THEN add reason
    IF lowest < MIN_SUB THEN add reason
    IF att < MIN_ATT THEN add reason
    IF income > MAX_INCOME THEN add reason
    IF reasons is empty THEN
        append (-aggregate, income, -att, id, name) to eligible
    ELSE
        print REJECTED with reasons
    END IF
END FOR
BUBBLE SORT eligible in ascending order
rank <- 1
FOR each entry in eligible
    IF rank <= QUOTA THEN result <- AWARDED ELSE result <- WAITING LIST
    print rank, id, name, aggregate, income, attendance, result
    rank <- rank + 1
END FOR
END
```

## 6. Flowchart
![Flowchart for Case Study 1](images/case01_flowchart.png)

## 7. Python Source Code
File: `programs/case01_scholarship_allocation.py`

```python
# Case Study 1: University Scholarship Allocation
# Uses: variables, loops, conditionals, lists, tuples, tuple unpacking

# ---------- Policy (change these to test other rules) ----------
MIN_AGGREGATE = 60      # minimum average marks (%)
MIN_SUBJECT = 40        # minimum marks in EVERY subject
MIN_ATTENDANCE = 75     # minimum attendance (%)
MAX_INCOME = 300000     # maximum annual family income (Rs)
QUOTA = 3               # number of scholarships available

# ---------- Applicants: (id, name, (5 subject marks), attendance, income) ----------
applicants = [
    ("S101", "Asha",   (78, 82, 75, 80, 85), 92, 200000),
    ("S102", "Bala",   (70, 72, 68, 75, 70), 88, 150000),
    ("S103", "Chitra", (80, 82, 75, 80, 83), 92, 180000),
    ("S104", "Dev",    (85, 90, 35, 88, 92), 95, 100000),
    ("S105", "Esha",   (75, 78, 80, 72, 70), 70, 120000),
    ("S106", "Farid",  (90, 88, 92, 85, 87), 96, 450000),
    ("S107", "Gita",   (55, 58, 60, 52, 50), 85, 90000),
    ("S108", "Hari",   (70, 72, 68, 75, 70), 88, 150000),
    ("S109", "Indu",   (40, 45, 50, 55, 40), 60, 350000),
]

eligible = []   # sort keys of eligible students

print("=== STEP 1: ELIGIBILITY CHECK ===")
for a in applicants:
    sid, name, marks, att, income = a        # tuple unpacking
    total = 0
    lowest = marks[0]
    for m in marks:
        total = total + m
        if m < lowest:
            lowest = m
    aggregate = round(total / len(marks), 2)

    reasons = []                              # list of failed conditions
    if aggregate < MIN_AGGREGATE:
        reasons.append("aggregate " + str(aggregate) + " < " + str(MIN_AGGREGATE))
    if lowest < MIN_SUBJECT:
        reasons.append("subject mark " + str(lowest) + " < " + str(MIN_SUBJECT))
    if att < MIN_ATTENDANCE:
        reasons.append("attendance " + str(att) + " < " + str(MIN_ATTENDANCE))
    if income > MAX_INCOME:
        reasons.append("income " + str(income) + " > " + str(MAX_INCOME))

    if len(reasons) == 0:
        print(sid, name.ljust(7), "ELIGIBLE   aggregate =", aggregate)
        # Tie-break key: higher aggregate, lower income, higher attendance, smaller ID
        eligible.append((-aggregate, income, -att, sid, name))
    else:
        print(sid, name.ljust(7), "REJECTED   ->", "; ".join(reasons))

# ---------- Bubble sort on the tuple keys (tuples compare element by element) ----------
n = len(eligible)
for i in range(n - 1):
    for j in range(n - 1 - i):
        if eligible[j] > eligible[j + 1]:
            temp = eligible[j]
            eligible[j] = eligible[j + 1]
            eligible[j + 1] = temp

print("\n=== STEP 2: RANK LIST (quota =", QUOTA, ") ===")
print("Rank  ID    Name     Aggr   Income  Att  Result")
rank = 1
for e in eligible:
    neg_agg, income, neg_att, sid, name = e
    if rank <= QUOTA:
        result = "AWARDED"
    else:
        result = "WAITING LIST"
    print(str(rank).ljust(5), sid, name.ljust(8), str(-neg_agg).ljust(6),
          str(income).ljust(7), str(-neg_att).ljust(4), result)
    rank = rank + 1

if len(eligible) == 0:
    print("No eligible applicants.")
```

## 8. Test Cases
| ID | Input / Scenario | Expected Output |
|----|------------------|-----------------|
| T1 | S101 Asha: avg 80, attendance 92, income 2,00,000 | ELIGIBLE, aggregate = 80.0 |
| T2 | S104 Dev: one subject mark 35 | REJECTED -> subject mark 35 < 40 |
| T3 | S105 Esha: attendance 70 | REJECTED -> attendance 70 < 75 |
| T4 | S106 Farid: income 4,50,000 | REJECTED -> income 450000 > 300000 |
| T5 | S107 Gita: average 55 | REJECTED -> aggregate 55.0 < 60 |
| T6 | S109 Indu: fails three rules | REJECTED with 3 reasons (aggregate, attendance, income) |
| T7 | S101 and S103 both have aggregate 80 | S103 ranked above S101 (lower income) |
| T8 | S102 and S108 identical in every field | S102 gets rank 3 (AWARDED), S108 rank 4 (WAITING LIST) by smaller ID |
| T9 | Final list | Ranks 1-3: S103, S101, S102 awarded; S108 on waiting list |

*Run the program and type the input shown. For the data-driven programs, the test data is already stored in the program as lists/tuples; edit those lists to try your own cases.*

## 9. Sample Output
Full output saved in `outputs/case01_scholarship_allocation_output.txt`.

```text
=== STEP 1: ELIGIBILITY CHECK ===
S101 Asha    ELIGIBLE   aggregate = 80.0
S102 Bala    ELIGIBLE   aggregate = 71.0
S103 Chitra  ELIGIBLE   aggregate = 80.0
S104 Dev     REJECTED   -> subject mark 35 < 40
S105 Esha    REJECTED   -> attendance 70 < 75
S106 Farid   REJECTED   -> income 450000 > 300000
S107 Gita    REJECTED   -> aggregate 55.0 < 60
S108 Hari    ELIGIBLE   aggregate = 71.0
S109 Indu    REJECTED   -> aggregate 46.0 < 60; attendance 60 < 75; income 350000 > 300000

=== STEP 2: RANK LIST (quota = 3 ) ===
Rank  ID    Name     Aggr   Income  Att  Result
1     S103 Chitra   80.0   180000  92   AWARDED
2     S101 Asha     80.0   200000  92   AWARDED
3     S102 Bala     71.0   150000  88   AWARDED
4     S108 Hari     71.0   150000  88   WAITING LIST
```

## 10. Output Screenshot
> Add your own terminal screenshot as `docs/screenshots/case01_scholarship_allocation_output.png` and the image below will appear:
>
> `![Output screenshot](screenshots/case01_scholarship_allocation_output.png)`

## 11. Conclusion
The program evaluates all applicants with the same rules, explains every rejection and produces a repeatable ranking. Sorting tuple keys made the multi-level tie-break simple, and the sample data shows each rule and tie case working correctly.
