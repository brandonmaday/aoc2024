import sys
import re

with open(f"aoc{sys.argv[1]}_in{'_smpl' if '-t' in sys.argv else ''}.txt") as f:
    txt = f.read().strip()

# part 1
mult = lambda x: int(x[0]) * int(x[1])
muls = [mult(m[4:-1].split(",")) for m in re.findall(r"mul\(\d+,\d+\)", txt)]
print(sum(muls))

# part 2
# tokens = re.findall(r"mul\(\d+,\d+\)|do\(\)|don't\(\)", txt)
def countEm(tokens, enabled = True, tot = 0):
    if len(tokens) == 0:
        return tot
    match enabled, tokens[0]:
        case _, "do()":
            return countEm(tokens[1:], True, tot)
        case _, "don't()":
            return countEm(tokens[1:], False, tot)
        case True, _:
            tot += mult(tokens[0][4:-1].split(","))
            return countEm(tokens[1:], True, tot)
        case False, _:
            return countEm(tokens[1:], False, tot)
print(countEm(re.findall(r"mul\(\d+,\d+\)|do\(\)|don't\(\)", txt)))
