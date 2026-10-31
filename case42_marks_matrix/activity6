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
