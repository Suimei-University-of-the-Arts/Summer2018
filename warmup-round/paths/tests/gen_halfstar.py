#!/usr/bin/python3

# Star graph where half of the "rays" have length 2.
# Short rays get color 1, center gets color 2,
# mid points of long rays get color 3,
# leaves of long rays get color 4.
# Only works for k = 4.

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


n = int(cmdlinearg('n'))
m = n-1
k = 4
longsize = n//3
shortsize = n-2*longsize-1
colors = []

for i in range(0,shortsize):
    colors.append(0)
colors.append(1)
for i in range(0,longsize):
    colors.append(2)
for i in range(0,longsize):
    colors.append(3)

eds = []
for i in range(0,shortsize):
    eds.append((i,shortsize))

for i in range(0,longsize):
    eds.append((shortsize,shortsize+i+1))

for i in range(0,longsize):
    eds.append((shortsize+i+1,shortsize+longsize+i+1))

output(k, colors, eds)
