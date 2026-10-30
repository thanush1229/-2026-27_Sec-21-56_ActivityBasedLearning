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
