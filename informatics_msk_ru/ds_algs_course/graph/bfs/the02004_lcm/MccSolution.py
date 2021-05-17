import os
import sys
from collections import deque


def solution(x, k, ds):
    if x % k == 0:
        return [x]

    x0 = x
    vis = {x % k: None}
    q = deque([x % k])

    y = None
    while q:
        x = q.popleft()
        for d in ds:
            x2 = (x * 10 + d) % k
            if x2 in vis:
                continue

            if x2 == 0:
                y = (x, d)
                q.clear()
                break

            vis[x2] = (x, d)
            q.append(x2)

    if y is None:
        return None

    ns = []
    while y:
        x, d = y
        ns.append(d)
        y = vis[x]

    ns.append(x0)
    ns.reverse()

    return ns


def parse_and_run(iff, off):
    x, k = map(int, next(iff).strip().split())
    cn = int(next(iff).strip())
    ds = set(list(map(int, next(iff).strip().split()))[:cn])

    res = solution(x, k, ds)
    if res is None:
        off.write('%d' % -1)
    else:
        off.write('%s' % ''.join(map(str, res)))


if 'NOMAIN' not in os.environ:
    parse_and_run(sys.stdin, sys.stdout)
