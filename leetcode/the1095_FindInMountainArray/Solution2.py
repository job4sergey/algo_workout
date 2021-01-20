class Solution:
    def findInMountainArray(self, t, arr):
        def bs(i, j, fn):
            while i < j - 1:
                m = i + (j - i) // 2
                if fn(m):
                    i = m
                else:
                    j = m

            return i

        def doit():
            i = bs(0, arr.length() - 1, lambda m: arr.get(m - 1) < arr.get(m))
            j = bs(-1, i + 1, lambda m: arr.get(m) <= t)
            if 0 <= j <= i and arr.get(j) == t:
                return j

            j = bs(i, arr.length(), lambda m: arr.get(m) >= t)
            return j if i < j < arr.length() and arr.get(j) == t else -1

        return doit()