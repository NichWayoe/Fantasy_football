# Whose ready for some football?

# pen players.txt to get a list of players and positions.

# We want to build the best team of:
# 1 QB
# 2 RB
# 2 WR
# 1 TE
# 1 RB or WR or TE

# Your code here!
positions = []  # an array for keeping positions
total = []  # an array for keeping the excepted scores of all players
names = []  # an array for keeping names
wr = []  # an array for keeping the scores of WR'S
rb = []  # an array for keeping the scores of RB's
qb = []  # an array for keeping the scores of QB's
te = []  # an array for keeping the scores of TE's
f = open("players.txt")
for i in f:
    line = i.split()
    positions.append(line[0])
    names.append(line[1])
    a = int(line[2]) // 25 + int(line[3]) * 4 + int(line[4]) // 10 + int(line[5]) * 6 + int(line[6]) // 10 + int(
        line[7]) * 6
    total.append(a)
for k in range(len(positions)):
    if positions[k] == "WR":
        wr.append(total[k])

    elif positions[k] == "RB":
        rb.append(total[k])

    elif positions[k] == "QB":
        qb.append(total[k])

    elif positions[k] == "TE":
        te.append(total[k])

print("QB ", names[total.index(max(qb))], max(qb))

print("RB1", names[total.index(max(rb))], max(rb))

rb.remove(max(rb))  # removes max value from rb

print("RB2", names[total.index(max(rb))], max(rb))
rb.remove(max(rb))
print("WR1", names[total.index(max(wr))], max(wr))

wr.remove(max(wr))

print("WR2", names[total.index(max(wr))], max(wr))
wr.remove(max(wr))

print("TE", names[total.index(max(te))], max(te))
te.remove(max(te))

a = max(wr + rb + te)

print("FLEX", names[total.index(a)], a)



