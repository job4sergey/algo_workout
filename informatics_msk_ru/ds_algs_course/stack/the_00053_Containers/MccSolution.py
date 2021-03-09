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
        while sts[1] and sts[1][-1]:
            mv(sts, 1, 0, fqs, acts)

        while fqs[0][2] and sts[0][-1] == 2:
            mv(sts, 0, 1, fqs, acts)

        if fqs[0][2]:
            return None
        else:
            return acts

    # INV: for all ii < i containers are ordered
    for i in range(sz):
        j, tt = (i + 1) % sz, (i + 2) % sz
        tsz = 0

        for k in range(i + 1, sz):
            while fqs[i][i + 1] < gfq[i + 1] and sts[k] and fqs[k][i + 1]:
                mv(sts, k, i, fqs, acts)

        # all 'i+1's are in i position

        while sts[i]:
            if sts[i][-1] == i + 1:
                mv(sts, i, j, fqs, acts)
            else:
                mv(sts, i, tt, fqs, acts)
                tsz += 1

        # sts[i] empty

        while fqs[j][i + 1]:
            mv(sts, j, i, fqs, acts)

        # restore temporary storage
        for _ in range(tsz):
            mv(sts, tt, j, fqs, acts)

        # i position contains only 'i+1's

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
