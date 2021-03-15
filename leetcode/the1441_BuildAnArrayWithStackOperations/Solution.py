class Solution(object):
    def buildArray(self, tg, n):
        i = 0
        res = []
        for j in range(1, n + 1):
            res.append('Push')
            if j != tg[i]:
                res.append('Pop')
            else:
                i += 1
                if i == len(tg):
                    break

        return res
