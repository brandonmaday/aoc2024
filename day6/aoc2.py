import sys

# 418 is TO LOW
# 1732 is TO HIGH

def trampoline(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        while callable(result):
            result = result()
        return result
    return wrapper


with open(f"in{'_s' if '-t' in sys.argv else ''}.txt") as f:
    txt = [list(l) for l in f.read().strip().split("\n")]
# print("\n".join(["".join(r) for r in txt]))

# Model out of bounds conditions for x
xIsOutOnLeft = lambda x: x < 0
xIsOutOnRight = lambda lineLength, x: x > lineLength-1
xIsOut = lambda lineLength, x: xIsOutOnLeft(x) or xIsOutOnRight(lineLength, x)
# Model out of bounds conditions for y
yIsOutUp = lambda y: y < 0
yIsOutDown = lambda blockLength, y: y > blockLength -1
yIsOut = lambda blockLength, y: yIsOutUp(y) or yIsOutDown(blockLength, y)
xyIsOut = lambda t: lambda x, y: yIsOut(len(t), y) or xIsOut(len(t[y]), x)
# Model movement blockers and logic
isBlocker = lambda c: c == "#"
dOffset = {"U": (0, -1), "R": (1, 0), "D": (0, 1), "L": (-1, 0)}
nextD = {"U": "R", "R": "D", "D": "L", "L": "U"}
def move(x, y, d):
    xOffset, yOffset = dOffset[d]
    return x + xOffset, y + yOffset

# Find starting x, y
def guardPosition(t, y=0, x=0, c=0):
    if len(t) == 0:
        print(f"Couldn't find a guard symbol")
        return None
    if len(t[0]) == 0:
        return lambda: guardPosition(t[1:], y+1, 0, c+1)
    match t[0][0]:
        case "." | "#":
            return lambda: guardPosition([t[0][1:]] + t[1:], y, x+1, c+1)
        case "^":
            return(x, y, "U")
        case "v": 
            return(x, y, "D")
        case ">":
            return(x, y, "R")
        case "<":
            return(x, y, "L")
        case _:
            print(f"Unknown Guard Symbol: {t[0][0]}")
            return None


def initWalk(g, x, y, d, outOfBounds, sqrs):
    if (x, y, d) in sqrs:
        return 1
    sqrs.add((x, y, d))
    newX, newY = move(x, y, d)
    if outOfBounds(newX, newY):
        return set([(x, y) for x, y, _ in sqrs])
    if g[newY][newX] == "#":
        d = nextD[d]
        newX, newY = move(x, y, d)
    return lambda: initWalk(g, newX, newY, d, outOfBounds, sqrs)

x, y, d = trampoline(guardPosition)(txt)
path = trampoline(initWalk)(txt, x, y, d, xyIsOut(txt), set())

cp = lambda arr: [[c for c in r] for r in arr]
res = 0
for blockX, blockY in path:
    g = cp(txt)
    g[blockY][blockX] = "#"
    if trampoline(initWalk)(g, x, y, d, xyIsOut(g), set()) == 1:
        res += 1
print("res", res)

