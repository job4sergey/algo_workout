from collections import Counter


class Solution(object):
    def smallestSubsequence(self, s):
        fq = Counter(s)

        st = []
        uni = set()

        for c in s:
            fq[c] -= 1
            if c in uni:
                continue

            while st and fq[st[-1]] > 0 and st[-1] > c:
                uni.remove(st.pop())

            st.append(c)
            uni.add(c)

        return ''.join(st)
