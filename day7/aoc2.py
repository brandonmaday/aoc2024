import sys
from itertools import product

with open(f"in{'_s' if '-t' in sys.argv else ''}.txt") as f:
    lines = f.read().strip().split("\n")
puz = []
for line in lines:
    testVal, nums = line.split(":")
    puz.append((int(testVal), [int(n) for n in nums.strip().split(" ")]))

def things(nums):
    return product("*+|", repeat=len(nums)-1)

def proc(a):
    def wrap(b, o):
        match o:
            case "+":
                return a + b
            case "*":
                return a * b
            case "|":
                return int(str(a) + str(b))
            case _:
                print("something has gone horribly wrong")
                sys.exit(1)
    return wrap


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
