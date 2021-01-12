class Solution(object):
    def nthUglyNumber(self, n, a, b, c):
        def gcd(x, y):
            while y != 0:
                x, y = y, x % y

            return x

        def lcm(x, y):
            return (x * y) // gcd(x, y)

        # Finds the count of ugly numbers <= x
        def cn(x):
            res = x // a + x // b + x // c
            res -= x // lcm(a, b) + x // lcm(a, c) + x // lcm(b, c)
            res += x // lcm(lcm(a, b), c)
            return res

        i, j = 1, 2 * 10 ** 9 + 1

        # Find smallest number j s.t, cn(j) >= n

        while i < j - 1:
            m = i + (j - i) // 2
            if cn(m) < n:
                i = m
            else:
                j = m

        return j
