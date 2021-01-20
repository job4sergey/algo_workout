class Solution(object):
    def nthMagicalNumber(self, n, a, b):
        if a > b:
            a, b = b, a

        def gcd(x, y):
            while y != 0:
                x, y = y, x % y

            return x

        def lcm(x, y):
            return (x * y) // gcd(x, y)

        def cn(x):
            return x // a + x // b - x // lcm(a, b)

        def do_it():
            i, j = a - 1, n * b

            while i < j - 1:
                m = i + (j - i) // 2
                if cn(m) < n:
                    i = m
                else:
                    j = m

            return j % (10 ** 9 + 7)

        return do_it()
