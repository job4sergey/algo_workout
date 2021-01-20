class Solution:
    def findInMountainArray(self, t, arr):
        def idx():
            i, j = 0, arr.length() - 1

            while i < j - 1:
                m = i + (j - i) // 2
                if arr.get(m - 1) < arr.get(m):
                    i = m
                else:
                    j = m

            return i

        def bs(i, j, fn=lambda x: x):
            while i <= j:
                m = i + (j - i) // 2
                x = arr.get(m)
                if x == t:
                    return m
                elif fn(x < t):
                    i = m + 1
                else:
                    j = m - 1

            return -1

        def doit():
            k = idx()
            res = bs(0, k)
            if res > -1:
                return res

            return bs(k + 1, arr.length() - 1, lambda x: not x)

        return doit()

# """
# This is MountainArray's API interface.
# You should not implement it, or speculate about its implementation
# """
# class MountainArray(object):
#    def get(self, index):
#        """
#        :type index: int
#        :rtype int
#        """
#
#    def length(self):
#        """
#        :rtype int
#        """
