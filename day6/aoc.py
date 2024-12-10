import sys

with open(f"in{'_s' if '-t' in sys.argv else ''}.txt") as f:
    txt = [list(l) for l in f.read().strip().split("\n")]

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
nextPosition = lambda x, y, xOffset, yOffset: (x+xOffset, y+yOffset)
def hitBlocker(xOffset, yOffset):
    newXOffset, newYOffset = {
        (0, -1): (1, 0),
        (1, 0): (0, 1),
        (0, 1): (-1, 0),
        (-1, 0): (0, -1),
    }[(xOffset, yOffset)]
    return newXOffset, newYOffset 

def trampoline(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        while callable(result):
            result = result()
        return result
    return wrapper

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
            return(x, y, 0, -1)
        case "v": 
            return(x, y, 0, 1)
        case ">":
            return(x, y, 1, 0)
        case "<":
            return(x, y, -1, 0)
        case _:
            print(f"Unknown Guard Symbol: {t[0][0]}")
            return None

# Update dots with X's
def paths(txt, x, y, xOffset, yOffset, outOfBounds):
    newX, newY = nextPosition(x, y, xOffset, yOffset)
    if outOfBounds(newX, newY):
        return txt
    match txt[newY][newX]:
        case "#":
            newXOffset, newYOffset = hitBlocker(xOffset, yOffset)
            return lambda: paths(txt, x, y, newXOffset, newYOffset, outOfBounds)
        case _:
            txt[newY][newX] = "X"
            return lambda: paths(txt, newX, newY, xOffset, yOffset, outOfBounds)

# Set initial guard position w/ X after getting direction
x, y, xOffset, yOffset = trampoline(guardPosition)(txt)
txt[y][x] = "X"
txt = trampoline(paths)(txt, x, y, xOffset, yOffset, xyIsOut(txt))

# Count up the "X"'s
print(len([x for y in txt for x in y if x == "X"]))
