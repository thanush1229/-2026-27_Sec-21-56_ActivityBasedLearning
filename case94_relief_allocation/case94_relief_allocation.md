# Case Study 94: Disaster Relief Supply Allocation

## 1. Problem Statement
After a disaster, limited stocks of food packets, water cans and medical kits must be shared among several areas. Areas have an urgency level and a demand for each item. The program prioritises areas by a fixed policy, allocates supplies and reports the unmet demand.

## 2. Objectives
- Use nested lists/tuples to hold stock, items and area demands.
- Validate urgency levels and demand values.
- Sort areas by priority using tuple keys and nested loops.
- Allocate each item as min(demand, remaining stock).
- Compute remaining stock and total unmet demand per item.

## 3. Assumptions
- Urgency 3 = critical, 2 = high, 1 = normal; any other value is invalid.
- Priority order: higher urgency first; for equal urgency the area with the larger total demand first; then area name.
- An area is served completely for an item (as far as stock allows) before the next area is considered; no partial sharing between areas of the same priority.
- Demands cannot be negative.

## 4. Algorithm
1. Store item names, opening stock and the area list.
2. For each area, validate urgency (1-3) and demands (>= 0) and report invalid areas.
3. For valid areas create a key (-urgency, -total demand, name, demand list).
4. Bubble-sort the queue by the first three key parts.
5. For each area in order and for each item, give = demand if demand <= stock else stock.
6. Reduce stock, record the shortage (demand - give) and add it to the item's total unmet demand.
7. Print the allocation for each area and the final summary.

## 5. Pseudocode
```text
START
READ items, stock, areas
FOR each area (name, urgency, demand list)
    IF urgency not in 1..3 OR any demand < 0 THEN report invalid ; skip
    total <- sum of demands
    add (-urgency, -total, name, demands) to queue
END FOR
BUBBLE SORT queue by (-urgency, -total, name)
FOR each area in queue
    FOR each item k
        give <- MIN(demand[k], stock[k])
        stock[k] <- stock[k] - give
        shortage <- demand[k] - give
        unmet[k] <- unmet[k] + shortage
        PRINT demand, give, shortage
    END FOR
END FOR
PRINT remaining stock and total unmet demand for every item
END
```

## 6. Flowchart
![Flowchart for Case Study 94](images/case94_flowchart.png)

## 7. Python Source Code
File: `programs/case94_relief_allocation.py`

```python
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
```

## 8. Test Cases
| ID | Input / Scenario | Expected Output |
|----|------------------|-----------------|
| T1 | Northgate with demand -5 | Invalid: negative demand -5 |
| T2 | Lakeview with urgency 4 | Invalid: urgency 4 |
| T3 | Riverside and Old Town (both urgency 3) | Riverside first (total demand 460 > 370) |
| T4 | Riverside demand 250/150/60 | Fully served |
| T5 | Old Town medical kits demand 50, only 40 left | Given 40, unmet 10 |
| T6 | Hilltop (urgency 2) | Food 50 of 200, water 30 of 100, medical 0 of 30 |
| T7 | Seaport (urgency 1) | Receives nothing: 100/80/20 unmet |
| T8 | Final totals | Stock remaining 0/0/0; unmet 250 food, 150 water, 60 medical kits |

*Run the program and type the input shown. For the data-driven programs, the test data is already stored in the program as lists/tuples; edit those lists to try your own cases.*

## 9. Sample Output
Full output saved in `outputs/case94_relief_allocation_output.txt`.

```text
=== VALIDATION ===
Northgate -> negative demand -5
Lakeview -> invalid urgency 4

=== ALLOCATION (priority order) ===
Riverside (urgency 3 )
    Food packets  demand  250 given  250 unmet    0
    Water cans    demand  150 given  150 unmet    0
    Medical kits  demand   60 given   60 unmet    0
Old Town (urgency 3 )
    Food packets  demand  200 given  200 unmet    0
    Water cans    demand  120 given  120 unmet    0
    Medical kits  demand   50 given   40 unmet   10
Hilltop (urgency 2 )
    Food packets  demand  200 given   50 unmet  150
    Water cans    demand  100 given   30 unmet   70
    Medical kits  demand   30 given    0 unmet   30
Seaport (urgency 1 )
    Food packets  demand  100 given    0 unmet  100
    Water cans    demand   80 given    0 unmet   80
    Medical kits  demand   20 given    0 unmet   20

=== SUMMARY ===
Food packets  remaining stock:    0  total unmet demand: 250
Water cans    remaining stock:    0  total unmet demand: 150
Medical kits  remaining stock:    0  total unmet demand: 60
```

## 10. Output Screenshot
> Add your own terminal screenshot as `docs/screenshots/case94_relief_allocation_output.png` and the image below will appear:
>
> `![Output screenshot](screenshots/case94_relief_allocation_output.png)`

## 11. Conclusion
The program implements a clear priority policy and shows exactly who gets what and what remains unmet. The sample shows the policy working when stock runs out and when invalid data has to be excluded.
