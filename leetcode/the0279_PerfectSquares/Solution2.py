import math


def sqrt(x):
    i, j = 1, x
    while i <= j:
        m = i + (j - i) // 2
        mm = m * m
        if mm == x:
            return m
        elif mm < x:
            i = m + 1
        else:
            j = m - 1

    return 0


# correct but slow
class Solution(object):
    def numSquares(self, N):
        mn = N
        for a in range(int(math.sqrt(N)), 0, -1):
            if a * a == N:
                mn = min(mn, 1)
                if mn == 1:
                    break

            for b in range(int(math.sqrt(N - a * a)), 0, -1):
                if a * a + b * b == N:
                    mn = min(mn, 2)
                    continue

                for c in range(int(math.sqrt(N - a * a - b * b)), 0, -1):
                    if a * a + b * b + c * c == N:
                        mn = min(mn, 3)
                        continue

                    dd = N - a * a - b * b - c * c

                    y = sqrt(dd)
                    if y > 0:
                        mn = min(mn, 4)
                        continue

        return mn
