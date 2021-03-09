import os
import sys
from collections import deque


# stack
def solution(ns, k):
    q = deque()
    res = []

    for i, n in enumerate(ns):
        while q and q[len(q) - 1] > n:
            q.pop()

        q.append(n)

        if i >= k - 1:
            res.append(q[0])

            if ns[i - k + 1] == q[0]:  # prepare for the next iteration
                q.popleft()

    if q and len(ns) < k:
        res.append(q[0])

    return res


if 'NOMAIN' not in os.environ:
    def parse_and_run():
        iff, off = sys.stdin, sys.stdout

        _, k = map(int, next(iff).strip().split())
        ns = list(map(int, next(iff).strip().split()))
        res = solution(ns, k)
        for r in res:
            off.write("%s\n" % r)


    parse_and_run()
