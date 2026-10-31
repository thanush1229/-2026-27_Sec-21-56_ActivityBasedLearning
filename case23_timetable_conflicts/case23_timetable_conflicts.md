# Case Study 23: Student Timetable Conflict Detection

## 1. Problem Statement
A proposed timetable lists course sessions with day, start time, end time, room and student group, written as strings inside tuples. The program must validate the times, detect overlapping sessions that share a room or a student group, and report sessions placed in rooms that are unavailable.

## 2. Objectives
- Validate time strings in HH:MM format using string indexing and string methods.
- Convert times to minutes so they can be compared.
- Detect overlaps between every pair of sessions using nested loops.
- Check sessions against a list of unavailable rooms.
- Produce a clear VALID / INVALID verdict with all reasons.

## 3. Assumptions
- Times use the 24-hour format HH:MM (for example 09:30).
- Two sessions overlap if they are on the same day and start1 < end2 and start2 < end1; sessions that only touch (one ends when the next starts) do not overlap.
- A clash exists when overlapping sessions use the same room or the same student group.
- Blocked rooms are given as (room, day, start, end) tuples.

## 4. Algorithm
1. Store sessions and blocked rooms as lists of tuples.
2. For each session, unpack it and validate both time strings (length 5, colon at position 2, digits elsewhere).
3. Reject sessions where start time is not before end time.
4. Convert valid times to minutes and store the session in the valid list.
5. Compare every pair (i, j) of valid sessions; if they overlap on the same day, report room clash and/or group clash.
6. Compare each valid session with the blocked-room list and report unavailable rooms.
7. Print all errors and clashes and the final verdict.

## 5. Pseudocode
```text
START
FOR each session (course, day, start, end, room, group)
    IF start or end is not in HH:MM format THEN log error ; CONTINUE
    convert start, end to minutes
    IF start >= end THEN log error ; CONTINUE
    add session to valid list
END FOR
FOR i <- 0 TO n-1
    FOR j <- i+1 TO n-1
        IF same day AND start_i < end_j AND start_j < end_i THEN
            IF room_i = room_j THEN log ROOM clash
            IF group_i = group_j THEN log GROUP clash
        END IF
    END FOR
END FOR
FOR each valid session
    FOR each blocked (room, day, start, end)
        IF same room AND same day AND times overlap THEN log unavailable-room clash
    END FOR
END FOR
PRINT errors and clashes
IF none THEN PRINT VALID ELSE PRINT INVALID
END
```

## 6. Flowchart
![Flowchart for Case Study 23](images/case23_flowchart.png)

## 7. Python Source Code
File: `programs/case23_timetable_conflicts.py`

```python
# Case Study 23: Student Timetable Conflict Detection
# Uses: strings, tuples, lists, nested loops, conditionals

# Session: (course, day, start, end, room, student_group)
sessions = [
    ("CS101", "Mon", "09:00", "10:00", "R101", "A"),
    ("MA101", "Mon", "09:30", "10:30", "R102", "A"),
    ("PH101", "Mon", "09:30", "10:30", "R101", "B"),
    ("EN101", "Tue", "10:00", "11:00", "R103", "A"),
    ("CH101", "Tue", "11:00", "12:00", "R103", "B"),
    ("BE101", "Wed", "14:00", "13:00", "R104", "A"),
    ("PY101", "Wed", "9am",   "10:00", "R104", "B"),
    ("LAB1",  "Thu", "10:00", "12:00", "R105", "A"),
]

# Rooms unavailable: (room, day, start, end)
blocked = [("R105", "Thu", "11:00", "13:00")]

valid = []        # (course, day, start_min, end_min, room, group)
errors = []

print("=== STEP 1: VALIDATE TIMES ===")
for s in sessions:
    course, day, start, end, room, group = s       # unpacking
    ok = True
    for t in (start, end):
        # format must be HH:MM -> length 5, colon at index 2, digits elsewhere
        if len(t) != 5 or t[2] != ":" or not t[0:2].isdigit() or not t[3:5].isdigit():
            ok = False
    if not ok:
        errors.append(course + ": invalid time format (" + start + " - " + end + ")")
        continue
    sm = int(start[0:2]) * 60 + int(start[3:5])   # minutes since midnight
    em = int(end[0:2]) * 60 + int(end[3:5])
    if sm >= em:
        errors.append(course + ": start time must be before end time")
        continue
    valid.append((course, day, sm, em, room, group))
    print(course, "OK")

clashes = []
for i in range(len(valid)):
    for j in range(i + 1, len(valid)):
        c1, d1, s1, e1, r1, g1 = valid[i]
        c2, d2, s2, e2, r2, g2 = valid[j]
        if d1 == d2 and s1 < e2 and s2 < e1:       # overlap rule
            if r1 == r2:
                clashes.append(c1 + " & " + c2 + ": ROOM clash in " + r1 + " on " + d1)
            if g1 == g2:
                clashes.append(c1 + " & " + c2 + ": GROUP clash for group " + g1 + " on " + d1)

for v in valid:
    course, day, sm, em, room, group = v
    for b in blocked:
        broom, bday, bs, be = b
        bsm = int(bs[0:2]) * 60 + int(bs[3:5])
        bem = int(be[0:2]) * 60 + int(be[3:5])
        if room == broom and day == bday and sm < bem and bsm < em:
            clashes.append(course + ": room " + room + " unavailable on " + day)

print("\n=== STEP 2: REPORT ===")
print("Errors:")
if len(errors) == 0:
    print("  none")
for e in errors:
    print("  -", e)
print("Clashes:")
if len(clashes) == 0:
    print("  none")
for c in clashes:
    print("  -", c)

if len(errors) == 0 and len(clashes) == 0:
    print("\nRESULT: Timetable is VALID")
else:
    print("\nRESULT: Timetable is INVALID (", len(errors), "errors,", len(clashes), "clashes )")
```

## 8. Test Cases
| ID | Input / Scenario | Expected Output |
|----|------------------|-----------------|
| T1 | CS101 (Mon 09:00-10:00, group A) and MA101 (Mon 09:30-10:30, group A) | GROUP clash for group A on Mon |
| T2 | CS101 (R101) and PH101 (Mon 09:30-10:30, R101, group B) | ROOM clash in R101 on Mon |
| T3 | MA101 (R102, A) and PH101 (R101, B), overlapping time | No clash (different room and group) |
| T4 | EN101 Tue 10:00-11:00 and CH101 Tue 11:00-12:00, same room | No clash (sessions only touch) |
| T5 | BE101 Wed 14:00-13:00 | Error: start time must be before end time |
| T6 | PY101 start time '9am' | Error: invalid time format (9am - 10:00) |
| T7 | LAB1 Thu 10:00-12:00 in R105 (blocked 11:00-13:00) | R105 unavailable on Thu |
| T8 | Overall result | INVALID (2 errors, 3 clashes) |

*Run the program and type the input shown. For the data-driven programs, the test data is already stored in the program as lists/tuples; edit those lists to try your own cases.*

## 9. Sample Output
Full output saved in `outputs/case23_timetable_conflicts_output.txt`.

```text
=== STEP 1: VALIDATE TIMES ===
CS101 OK
MA101 OK
PH101 OK
EN101 OK
CH101 OK
LAB1 OK

=== STEP 2: REPORT ===
Errors:
  - BE101: start time must be before end time
  - PY101: invalid time format (9am - 10:00)
Clashes:
  - CS101 & MA101: GROUP clash for group A on Mon
  - CS101 & PH101: ROOM clash in R101 on Mon
  - LAB1: room R105 unavailable on Thu

RESULT: Timetable is INVALID ( 2 errors, 3 clashes )
```

## 10. Output Screenshot
> Add your own terminal screenshot as `docs/screenshots/case23_timetable_conflicts_output.png` and the image below will appear:
>
> `![Output screenshot](screenshots/case23_timetable_conflicts_output.png)`

## 11. Conclusion
The program converts text times into minutes, so overlaps can be found with a simple comparison. It reports each type of problem separately, which makes it easy to correct a timetable. It also shows that sessions that merely touch are handled correctly.
