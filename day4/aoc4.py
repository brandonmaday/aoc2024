import sys

with open(f"in{'_s' if '-t' in sys.argv else ''}.txt") as f:
    txt = f.read().strip().split("\n")

seek = (
    (-1, -1), (-1, 0), (-1, 1),
    (0, -1), (0, 1),
    (1, -1), (1, 0), (1, 1),
)

def safeLetter(y, x):
    if y < 0 or x < 0:
        return 'Z'
    try:
        return txt[y][x]
    except IndexError:
        return 'Z'

count = 0
for i in range(len(txt)):
    for j in range(len(txt[i])):
        if txt[i][j] == 'X':
            for m_x, m_y in seek:
                if safeLetter(i + m_y, j + m_x) == 'M':
                    if safeLetter(i + m_y*2, j + m_x*2) == 'A':
                        if safeLetter(i + m_y*3, j + m_x*3) == 'S':
                            count += 1
print("count", count)

def letterMatch(y1, x1, y2, x2):
    a = safeLetter(y1, x1)
    b = safeLetter(y2, x2)
    return (a == "M" and b == "S") or (a == "S" and b == "M")

count = 0
for i in range(len(txt)):
    for j in range(len(txt[i])):
        if txt[i][j] == 'A':
            if letterMatch(i-1, j-1, i+1, j+1) and letterMatch(i-1, j+1, i+1, j-1):
                count += 1
print("count", count)
