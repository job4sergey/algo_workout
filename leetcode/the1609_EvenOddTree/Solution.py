from collections import deque


class Solution(object):
    def isEvenOddTree(self, r0):
        lev = 0
        cn = 1
        q = deque([r0])

        while cn:
            next_cn = 0

            pre = float('inf') if lev % 2 else float('-inf')
            while cn:
                r = q.popleft()

                if r.left:
                    q.append(r.left)
                    next_cn += 1

                if r.right:
                    q.append(r.right)
                    next_cn += 1

                if r.val % 2 == lev % 2:
                    return False

                if lev % 2:
                    if pre <= r.val:
                        return False
                else:
                    if pre >= r.val:
                        return False

                pre = r.val
                cn -= 1

            lev += 1
            cn = next_cn

        return True
