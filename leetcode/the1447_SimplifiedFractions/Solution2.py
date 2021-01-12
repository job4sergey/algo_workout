class Solution(object):
    def simplifiedFractions(self, n):
        def gcd(x, y):
            while y:
                x, y = y, x % y

            return x

        res = []

        for no in range(1, n):
            for de in range(no + 1, n + 1):
                if gcd(no, de) == 1:
                    res.append('%s/%s' % (no, de))

        return res
