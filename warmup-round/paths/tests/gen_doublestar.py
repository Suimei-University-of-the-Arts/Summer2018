#!/usr/bin/python3

import random
import sys

def cmdlinearg(name, default=None):
    for arg in sys.argv:
        if arg.startswith(name + "="):
            return arg.split("=")[1]
    assert default is not None, name
    return default

random.seed(int(cmdlinearg('seed', sys.argv[-1])))

# add 'extra' additional random edges
def add_extra(eds, extra, n):
    edset = set(eds)
    assert len(eds) == len(edset)
    m = len(eds)
    while len(edset) < m + extra:
        a = random.randrange(n)
        b = random.randrange(n)
        if a == b:
            continue
        if a > b:
            a,b = b,a
        edset.add((a,b))
    return list(edset)

def output(k, colors, eds):
    n = len(colors)

    eds = add_extra(eds, int(cmdlinearg('extra', 0)), n)

    m = len(eds)

    colnames = list(range(k))
    nodenames = list(range(n))
    random.shuffle(colnames)
    random.shuffle(nodenames)
    random.shuffle(eds)
    nodenamesinv = [None] * n
    for i in range(n):
        nodenamesinv[nodenames[i]] = i

    print(n, m, k)
    print(*[colnames[colors[nodenamesinv[i]]]+1 for i in range(n)])
    for (a, b) in eds:
        assert a != b
        if random.choice([True, False]):
            a,b = b,a
        print(nodenames[a]+1, nodenames[b]+1)


#Only works for k=5
#m <= 1e5 for n <= 75000

n = int(cmdlinearg('n'))
k = 5
endsize = n//3
midsize = n - 2*endsize - 2
star_a = n-2
star_b = n-1

colors = []
eds = []

left = list(range(0, endsize))
mid = list(range(endsize, endsize + midsize))
right = list(range(endsize + midsize, endsize*2 + midsize))

for i in left:
    colors.append(0)
    eds.append((i, star_a))

for i in mid:
    colors.append(1)
    eds.append((i, star_a))
    eds.append((i, star_b))

for i in right:
    colors.append(2)
    eds.append((i, star_b))

colors.append(3)
colors.append(4)

output(k, colors, eds)
