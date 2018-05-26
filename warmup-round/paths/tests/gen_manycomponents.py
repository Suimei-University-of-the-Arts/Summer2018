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

# Graph with many components of size c.
# Will contain <= m edges

n = int(cmdlinearg('n'))
m = int(cmdlinearg('m'))
k = int(cmdlinearg('k'))
c = int(cmdlinearg("compsize"))


colors = list(range(k)) + [random.randrange(k) for _ in range(n - k)]
random.shuffle(colors)
colors = colors[:n]
eds = []

edset = set()
failures = 0
failurelim = 100
while len(edset) < m:
    if failures >= failurelim:
        break
    a = random.randrange(n)
    b = 1+random.randrange(c-1)
    b += a//c * c
    if a > b:
        a,b = b,a
    if a == b or max(a,b) >= n or ((a,b) in edset):
        failures += 1
        continue
    else:
        failures = 0
    edset.add((a,b))
eds = list(edset)

output(k, colors, eds)
