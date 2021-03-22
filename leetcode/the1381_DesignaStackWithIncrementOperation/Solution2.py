from collections import defaultdict


class CustomStack:
    def __init__(self, maxSize: int):
        self.st = []
        self.maxSize = maxSize
        self.incs = defaultdict(int)

    def push(self, x: int) -> None:
        st = self.st

        if len(st) < self.maxSize:
            st.append(x)

    def pop(self) -> int:
        st = self.st
        if not st:
            return -1

        dx = 0
        if len(st) - 1 in self.incs:
            tmp = self.incs.pop(len(st) - 1)
            dx += tmp
            if len(st) > 1:
                self.incs[len(st) - 2] += tmp

        return st.pop() + dx

    def increment(self, k: int, dx: int) -> None:
        self.incs[min(k - 1, len(self.st) - 1)] += dx
