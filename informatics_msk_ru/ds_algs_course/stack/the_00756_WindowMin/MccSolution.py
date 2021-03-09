import os
import sys
from collections import deque


def enq(q, n):
    while q and q[-1] > n:
        q.pop()

    q.append(n)


# stack
def solution(ns, k):
    q = deque()
    res = []

    for n in ns[:k]:
        enq(q, n)

    res.append(q[0])

    for i, n in enumerate(ns[k:], k):
        enq(q, n)

        if ns[i - k] == q[0]:
            q.popleft()

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
