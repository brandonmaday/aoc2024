import sys
from itertools import permutations as per

with open(f"in{'_s' if '-t' in sys.argv else ''}.txt") as f:
    lines = f.read().strip().split("\n")
puz = []
for line in lines:
    testVal, nums = line.split(":")
    puz.append((int(testVal), [int(n) for n in nums.strip().split(" ")]))

def things(nums):
    spaces = len(nums) - 1
    opers = set()
    opers.add("+"*spaces)
    opers.add("*"*spaces)
    for i in range(spaces):
        opers.add((i)*"+" + (spaces-i)*"*")
    opers = list(opers)
    perms = set()
    for o in opers:
        for p in per(o):
            perms.add(p)
    return list(perms)

proc = lambda a: lambda b, o: a + b if o == "+" else a * b

def valid(testVal, nums):
    ops = things(nums)
    for op in ops:
        comp = proc(nums[0])
        for i, n in enumerate(nums[1:]):
            comp = proc(comp(n, op[i]))
        if comp(0, "+") == testVal:
            return testVal
    return 0

tot = 0
for i, p in enumerate(puz):
    print(f"Processing line {i + 1}")
    tot += valid(p[0], p[1])

print("tot", tot)
