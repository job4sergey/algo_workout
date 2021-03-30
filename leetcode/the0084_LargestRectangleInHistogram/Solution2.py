from typing import List


# IDEA: for each i, find the area of max rectangle, which contains hs[i]
# its area is (lessR[i] - lessL[i] - 1) * hs[i]
# where
# lessL ===  for position i, lessL[i] is the first pos to left < h
# lessR === for position i, lessR[i] is the first pos to right < h
class Solution:
    def largestRectangleArea(self, hs: List[int]) -> int:
        sz = len(hs)
        lessL = [-1] * sz
        lessR = [sz] * sz

        st = []

        for i, h in enumerate(hs):
            while st and hs[st[-1]] >= h:
                st.pop()

            lessL[i] = st[-1] if st else -1
            st.append(i)

        st.clear()

        for i, h in enumerate(reversed(hs)):
            i = sz - i - 1
            while st and hs[st[-1]] >= h:
                st.pop()

            lessR[i] = st[-1] if st else sz
            st.append(i)

        mx = 0

        for i, h in enumerate(hs):
            area = (lessR[i] - lessL[i] - 1) * hs[i]
            mx = max(mx, area)

        return mx
