class Solution(object):
    def countSubstrings(self, s):
        sz = len(s)
        cn = 0

        for k in range(sz):
            for i, j in ((k, k), (k - 1, k)):
                is_poly = 1
                while i > -1 and j < sz and is_poly:
                    is_poly = s[i] == s[j]
                    cn += is_poly
                    i -= 1
                    j += 1

        return cn