class Solution(object):
    def myPow(self, x, n):
        is_less_zero = n < 0
        n = abs(n)

        res = 1
        p = 1
        y = x
        while p <= n:
            if p & n:
                res *= y

            p <<= 1
            y *= y

        return 1 / res if is_less_zero else res
