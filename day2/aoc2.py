import sys

with open(f"aoc{sys.argv[1]}_in{'_smpl' if '-t' in sys.argv else ''}.txt") as f:
    lines = f.read().split("\n")[:-1]

reports = [[int(level) for level in report.split(" ")] for report in lines]

evalDirection = lambda a, b: "Same" if a == b else "Up" if a < b else "Down"
isGradual = lambda a, b: 1 <= abs(a-b) <= 3

def isSafe(levels, lastLevel=None, direction=None):
    if lastLevel is None:
        if len(levels) < 2:
            return 0
        return isSafe(levels[1:], levels[0], evalDirection(levels[0], levels[1]))
    else:
        if len(levels) == 0:
            return 1
        else:
            if direction != evalDirection(lastLevel, levels[0]) or not isGradual(lastLevel, levels[0]):
                return 0
            return isSafe(levels[1:], levels[0], direction)

print("part1", sum([isSafe(levels) for levels in reports]))

def isKindaSafe(levels, i = 0):
    if i > len(levels):
        return 0
    if isSafe(levels[:i] + levels[i+1:]) == 1:
        return 1
    else:
        return isKindaSafe(levels, i+1)

print("part1", sum([isKindaSafe(levels) for levels in reports]))
