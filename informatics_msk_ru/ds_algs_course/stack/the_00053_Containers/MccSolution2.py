import os
import sys
from collections import Counter


def mv(sts, fro, to, fqs, acts):
    x = sts[fro].pop()
    fqs[fro][x] -= 1

    sts[to].append(x)
    fqs[to][x] += 1

    acts.append((fro, to))


# stack
def solution(sts):
    sz = len(sts)
    if sz <= 1:
        return []

    acts = []
    gfq = Counter()
    fqs = [Counter()] * len(sts)

    for i, st in enumerate(sts):
        for x in st:
            if x < 1 or x > sz:
                return None
        fqs[i] = Counter(st)
        gfq.update(fqs[i])

    is_ok = True
    for i in range(len(sts)):
        if len(fqs[i]) != 1 or fqs[i][i + 1] != gfq[i + 1]:
            is_ok = False
            break

    if is_ok:
        return []

    if sz == 2:
        while sts[1]:
            mv(sts, 1, 0, fqs, acts)

        while fqs[0][2] and sts[0][-1] == 2:
            mv(sts, 0, 1, fqs, acts)

        return acts if fqs[0][2] == 0 else None

    for i in range(1, sz):
        while sts[i]:
            mv(sts, i, 0, fqs, acts)

    # everything is in pos 0

    while sts[0] and (fqs[0][1] != len(sts[0])):
        if sts[0][-1] == 1:
            mv(sts, 0, 1, fqs, acts)
        else:
            mv(sts, 0, sts[0][-1] - 1, fqs, acts)

    cn = 0
    while fqs[1][1] > 0:
        if sts[1][-1] == 1:
            mv(sts, 1, 0, fqs, acts)
        else:
            mv(sts, 1, 2, fqs, acts)
            cn += 1

    for _ in range(cn):
        mv(sts, 2, 1, fqs, acts)

    return acts


if 'NOMAIN' not in os.environ:
    def parse_and_run():
        iff, off = sys.stdin, sys.stdout

        sz = int(next(iff).strip())
        sts = []
        for _ in range(sz):
            sts.append(list(map(int, next(iff).strip().split()))[1:])
        res = solution(sts)
        if res is None:
            off.write("0")
        else:
            for k, r in enumerate(res):
                i, j = r
                off.write("%s %s%s" % (i + 1, j + 1, "\n"))
            else:
                off.write("")


    parse_and_run()
