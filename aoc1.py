with open("aoc1_in.txt") as f:
    lines = f.read().split("\n")[:-1]

# day 1 puzzle 1
left = []
right = []
for line in lines:
    a, *b, c = line.split(" ")
    left.append(int(a))
    right.append(int(c))
left.sort()
right.sort()
distance = 0
for i in range(len(left)):
    distance += abs(left[i] - right[i])
print(distance)

# day 1 puzzle 2
right_map = {}
sim = 0
for loc in right:
    try:
        right_map[loc] = right_map[loc] + 1
    except KeyError:
        right_map[loc] = 1
for loc in left:
    try:
        sim = sim + (loc * right_map[loc])
    except KeyError:
        pass
print(sim)
