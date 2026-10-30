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
