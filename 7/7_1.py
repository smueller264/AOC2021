from collections import defaultdict

with open('input.txt') as f:
    crabs = [int(x) for x in f.read().split(',')]

result = defaultdict(int)
maxValue = max(crabs)

for i in crabs:
    result[i] += 1

distance = 99999999999999
index = 0
for pos in range(1, maxValue):
    newdistance = 0
    cost = 0
    for nex in crabs:
        print(f"{nex} - {pos}")
        newdistance += sum(range(1, abs(nex - pos) + 1))
        print(newdistance)
    if (newdistance < distance):
        distance = newdistance
    print(distance)
print(distance)
