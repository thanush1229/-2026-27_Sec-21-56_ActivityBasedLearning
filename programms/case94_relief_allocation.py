# Case Study 94: Disaster Relief Supply Allocation
# Uses: lists, nested lists, tuples, unpacking, loops, conditionals
# Policy: serve areas by urgency (3 = critical first); ties -> larger total demand;
#         then area name. Each item is given min(demand, remaining stock).

items = ["Food packets", "Water cans", "Medical kits"]
stock = [500, 300, 100]

# (area, urgency 1-3, [demand for each item])
areas = [
    ("Riverside", 3, [250, 150, 60]),
    ("Hilltop", 2, [200, 100, 30]),
    ("Old Town", 3, [200, 120, 50]),
    ("Seaport", 1, [100, 80, 20]),
    ("Northgate", 2, [150, 90, -5]),      # invalid demand
    ("Lakeview", 4, [50, 50, 10]),        # invalid urgency
]

queue = []
print("=== VALIDATION ===")
for a in areas:
    name, urgency, demand = a
    bad = False
    if urgency < 1 or urgency > 3:
        print(name, "-> invalid urgency", urgency)
        bad = True
    for d in demand:
        if d < 0:
            print(name, "-> negative demand", d)
            bad = True
    if not bad:
        total = 0
        for d in demand:
            total += d
        queue.append((-urgency, -total, name, demand))   # sort key + data

# Bubble sort the queue
n = len(queue)
for i in range(n - 1):
    for j in range(n - 1 - i):
        if queue[j][0:3] > queue[j + 1][0:3]:
            queue[j], queue[j + 1] = queue[j + 1], queue[j]

print("\n=== ALLOCATION (priority order) ===")
unmet_total = [0, 0, 0]
for q in queue:
    neg_u, neg_t, name, demand = q
    print(name, "(urgency", -neg_u, ")")
    for k in range(len(items)):
        if demand[k] <= stock[k]:
            give = demand[k]
        else:
            give = stock[k]
        stock[k] -= give
        shortage = demand[k] - give
        unmet_total[k] += shortage
        print("   ", items[k].ljust(13), "demand", str(demand[k]).rjust(4),
              "given", str(give).rjust(4), "unmet", str(shortage).rjust(4))

print("\n=== SUMMARY ===")
for k in range(len(items)):
    print(items[k].ljust(13), "remaining stock:", str(stock[k]).rjust(4),
          " total unmet demand:", unmet_total[k])
