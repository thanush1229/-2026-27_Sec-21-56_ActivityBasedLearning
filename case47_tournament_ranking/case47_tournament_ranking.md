# Case Study 47: Sports Tournament Ranking System

## 1. Problem Statement
A round-robin tournament has results stored as tuples (team1, goals1, team2, goals2). The program validates each result, computes played, won, drawn, lost, goals for/against, goal difference and points for each team, and produces a ranked table using a fixed tie-break policy.

## 2. Objectives
- Store match results as tuples and team statistics in parallel lists.
- Use tuple unpacking and list methods (index) to update the right team.
- Reject invalid matches (unknown team, same team, negative score).
- Rank teams by sorting tuple keys under a multi-level tie-break policy.
- Print a formatted standings table.

## 3. Assumptions
- Win = 3 points, draw = 1 point, loss = 0 points.
- Tie-break order: points, then goal difference, then goals scored, then team name (A-Z).
- Each team name appears exactly once in the team list.
- Head-to-head results are not used for ranking.

## 4. Algorithm
1. Create the team list and parallel lists for P, W, D, L, GF, GA and points.
2. For each match, unpack the tuple and validate it; print REJECTED and skip invalid ones.
3. Find the list positions of both teams with index().
4. Update played, goals for and goals against for both teams.
5. Compare goals and award points and win/draw/loss counts.
6. Build a key (-points, -goal difference, -goals for, name, position) for every team.
7. Bubble-sort the keys, then print the standings and the champion.

## 5. Pseudocode
```text
START
teams <- list of names ; initialise P,W,D,L,GF,GA,PTS lists to 0
FOR each match (t1, g1, t2, g2)
    IF t1 or t2 unknown OR t1 = t2 OR g1 < 0 OR g2 < 0 THEN
        PRINT REJECTED ; CONTINUE
    a <- position of t1 ; b <- position of t2
    P[a]++, P[b]++ ; GF[a]+=g1, GA[a]+=g2 ; GF[b]+=g2, GA[b]+=g1
    IF g1 > g2 THEN W[a]++, L[b]++, PTS[a]+=3
    ELSE IF g1 < g2 THEN W[b]++, L[a]++, PTS[b]+=3
    ELSE D[a]++, D[b]++, PTS[a]++, PTS[b]++
END FOR
FOR each team i: key <- (-PTS, -(GF-GA), -GF, name, i)
BUBBLE SORT keys ascending
PRINT table in sorted order
PRINT champion = first team
END
```

## 6. Flowchart
![Flowchart for Case Study 47](images/case47_flowchart.png)

## 7. Python Source Code
File: `programs/case47_tournament_ranking.py`

```python
# Case Study 47: Sports Tournament Ranking System
# Uses: lists, tuples, unpacking, nested loops, conditionals
# Policy: Win = 3 pts, Draw = 1 pt, Loss = 0.
# Tie-breaks: 1) points 2) goal difference 3) goals scored 4) team name (A-Z)

teams = ["Lions", "Tigers", "Eagles", "Sharks"]

# Match: (team1, goals1, team2, goals2)
matches = [
    ("Lions", 2, "Tigers", 1),
    ("Eagles", 0, "Sharks", 0),
    ("Lions", 1, "Eagles", 1),
    ("Tigers", 3, "Sharks", 0),
    ("Lions", 0, "Sharks", 1),
    ("Tigers", 2, "Eagles", 2),
    ("Eagles", 1, "Lions", -1),      # invalid: negative score
    ("Lions", 2, "Lions", 2),        # invalid: team plays itself
    ("Tigers", 1, "Pumas", 0),       # invalid: unknown team
]

# Parallel lists: index i belongs to teams[i]
played = [0, 0, 0, 0]
won = [0, 0, 0, 0]
drawn = [0, 0, 0, 0]
lost = [0, 0, 0, 0]
gf = [0, 0, 0, 0]
ga = [0, 0, 0, 0]
pts = [0, 0, 0, 0]

print("=== PROCESSING MATCHES ===")
for m in matches:
    t1, g1, t2, g2 = m
    if t1 not in teams or t2 not in teams:
        print("REJECTED", m, "-> unknown team")
        continue
    if t1 == t2:
        print("REJECTED", m, "-> a team cannot play itself")
        continue
    if g1 < 0 or g2 < 0:
        print("REJECTED", m, "-> negative score")
        continue

    a = teams.index(t1)
    b = teams.index(t2)
    played[a] += 1
    played[b] += 1
    gf[a] += g1
    ga[a] += g2
    gf[b] += g2
    ga[b] += g1
    if g1 > g2:
        won[a] += 1
        lost[b] += 1
        pts[a] += 3
    elif g1 < g2:
        won[b] += 1
        lost[a] += 1
        pts[b] += 3
    else:
        drawn[a] += 1
        drawn[b] += 1
        pts[a] += 1
        pts[b] += 1
    print("OK      ", m)

# Build sort keys (negatives make "bigger is better" sort ascending)
table = []
for i in range(len(teams)):
    gd = gf[i] - ga[i]
    table.append((-pts[i], -gd, -gf[i], teams[i], i))

n = len(table)
for i in range(n - 1):                    # bubble sort
    for j in range(n - 1 - i):
        if table[j] > table[j + 1]:
            table[j], table[j + 1] = table[j + 1], table[j]

print("\n=== FINAL STANDINGS ===")
print("Pos Team     P  W  D  L  GF GA  GD  Pts")
pos = 1
for row in table:
    np_, ngd, ngf, name, i = row
    print(str(pos).ljust(3), name.ljust(8), str(played[i]).ljust(2), str(won[i]).ljust(2),
          str(drawn[i]).ljust(2), str(lost[i]).ljust(2), str(gf[i]).ljust(2),
          str(ga[i]).ljust(2), str(-ngd).rjust(3), str(pts[i]).rjust(4))
    pos += 1
print("\nChampion:", table[0][3])
```

## 8. Test Cases
| ID | Input / Scenario | Expected Output |
|----|------------------|-----------------|
| T1 | Lions 2 - 1 Tigers | Accepted: Lions +3 points |
| T2 | Eagles 0 - 0 Sharks | Accepted: draw, 1 point each |
| T3 | Eagles 1 - Lions -1 | REJECTED -> negative score |
| T4 | Lions 2 - Lions 2 | REJECTED -> a team cannot play itself |
| T5 | Tigers 1 - Pumas 0 | REJECTED -> unknown team |
| T6 | Tigers, Lions and Sharks all finish on 4 points | Order decided by goal difference: Tigers (+2), Lions (0), Sharks (-2) |
| T7 | Final standings | 1 Tigers 4 pts, 2 Lions 4 pts, 3 Sharks 4 pts, 4 Eagles 3 pts |
| T8 | Champion | Tigers |

*Run the program and type the input shown. For the data-driven programs, the test data is already stored in the program as lists/tuples; edit those lists to try your own cases.*

## 9. Sample Output
Full output saved in `outputs/case47_tournament_ranking_output.txt`.

```text
=== PROCESSING MATCHES ===
OK       ('Lions', 2, 'Tigers', 1)
OK       ('Eagles', 0, 'Sharks', 0)
OK       ('Lions', 1, 'Eagles', 1)
OK       ('Tigers', 3, 'Sharks', 0)
OK       ('Lions', 0, 'Sharks', 1)
OK       ('Tigers', 2, 'Eagles', 2)
REJECTED ('Eagles', 1, 'Lions', -1) -> negative score
REJECTED ('Lions', 2, 'Lions', 2) -> a team cannot play itself
REJECTED ('Tigers', 1, 'Pumas', 0) -> unknown team

=== FINAL STANDINGS ===
Pos Team     P  W  D  L  GF GA  GD  Pts
1   Tigers   3  1  1  1  6  4    2    4
2   Lions    3  1  1  1  3  3    0    4
3   Sharks   3  1  1  1  1  3   -2    4
4   Eagles   3  0  3  0  3  3    0    3

Champion: Tigers
```

## 10. Output Screenshot
> Add your own terminal screenshot as `docs/screenshots/case47_tournament_ranking_output.png` and the image below will appear:
>
> `![Output screenshot](screenshots/case47_tournament_ranking_output.png)`

## 11. Conclusion
The program turns raw match tuples into a reliable league table. Using sort keys with negative values lets one comparison handle points, goal difference, goals scored and name, and the invalid matches show that the validation layer protects the table from bad data.
