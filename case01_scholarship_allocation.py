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
