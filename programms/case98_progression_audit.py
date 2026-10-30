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
