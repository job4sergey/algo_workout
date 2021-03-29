class Solution(object):
    def trap(self, hs):
        if not hs:
            return 0

        sz = len(hs)
        gts = [0] * sz
        st = [hs[-1]]
        for i in range(sz - 2, -1, -1):
            gts[i] = st[-1]
            if hs[i] > st[-1]:
                st.append(hs[i])

        st.clear()
        st.append(hs[0])
        area = 0
        for i in range(1, sz):
            left = st[-1]  # highest on the left
            right = gts[i]  # highest on the right
            height = min(left, right)  # max possible current water level
            area += max(height - hs[i], 0)
            if st[-1] < hs[i]:
                st.append(hs[i])

        return area
