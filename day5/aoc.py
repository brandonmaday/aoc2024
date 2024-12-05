import sys

with open(f"in{'_s' if '-t' in sys.argv else ''}.txt") as f:
    txt = f.read().strip().split("\n")

rules = {}
pages = []
onRules = True
for line in txt:
    if onRules:
        if line == "":
            onRules = False
            continue
        else:
            a,b = line.split("|")
            try:
                rules[a].append(b)
            except KeyError:
                rules[a] = [b]
    else:
        pages.append(line.split(","))

def mid(line):
    for i in range(len(line)):
        try:
            ruleset = rules[line[i]]
        except KeyError:
            continue
        else:
            for j in rules[line[i]]:
                if j in line[:i]:
                    return 0
    return line[len(line)//2]

print(sum([int(mid(m)) for m in pages]))

def mid2(line):
    hadError = False
    for i in range(len(line)):
        try:
            ruleset = rules[line[i]]
        except KeyError:
            continue
        else:
            for j in rules[line[i]]:
                try:
                    k = line[:i].index(j)
                except ValueError:
                    pass
                else:
                    hadError = True
                    line.insert(i+1, j)
                    del[line[k]]
    if hadError:
        if mid2(line[:]) == 0:
            return line[len(line)//2]
        else:
            return mid2(line[:])
    else:
        return 0


print(sum([int(mid2(m)) for m in pages]))
