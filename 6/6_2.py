from collections import defaultdict

with open("input.txt") as f:
    fish = [int(x) for x in f.read().split(",")]

result = defaultdict(int)


for i in fish:
    result[i] += 1

for day in range(257):
    if day == 256:
        print(sum(result.values()))

    new_result = defaultdict(int)
    for fish, num in result.items():
        if fish == 0:
            new_result[6] += num
            new_result[8] += num
        else:
            new_result[fish - 1] += num
    result = new_result
