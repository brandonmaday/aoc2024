import sys

with open(f"aoc{sys.argv[1]}_in{'_smpl' if '-t' in sys.argv else ''}.txt") as f:
    txt = f.read().strip()

next_letter = "m"

def ping(txt, code=[]):
    idx = txt.find("mul(")
    if idx == -1:
        return code
    code.append(txt[idx+4:])
    return ping(txt[idx+1:], code)

def ping2(txt, code=[]):
    off = txt.find("don't()")
    if off == -1:
        return ping(txt, code)
    idx = txt.find("mul(",0, off)
    if idx == -1:
        on = txt.find("do()", off)
        if on == -1:
            return code
        else:
            return ping2(txt[on:], code)
    code.append(txt[idx+4:])
    return ping2(txt[idx+1:], code)


def pong(op):
    i = op.find(",")
    if i == -1:
        return None, True
    a = op[:i]
    j = op.find(")", i)
    if j == -1:
        return None, True
    b = op[i+1:j]
    try:
        return (int(a), int(b)), False
    except ValueError:
        return None, True

res = 0
for op in ping2(txt):
    s, err = pong(op)
    if not err:
        res = res + (s[0] * s[1])
print(res)
