from bisect import bisect_left


# Follow ups:
# 1) prove that my pivot() function always quits?

class Solution(object):
    def search(self, ns, t):
        sz = len(ns)

        # searches for ii s.t.,
        # ns[ii - 1] > ns[i], i.e. 'downward ladder', aka 'ladder'
        def pivot():
            i, j = 0, sz - 1

            # INVARIANT - our search space has at least 2 elements
            while j - i > 0:
                if j - i == 1:
                    # our search space has exactly 2 elements
                    return j if ns[j] < ns[i] else -1

                m = i + (j - i) // 2
                if ns[m] < ns[i]:
                    j = m  # ladder in [1, m]
                else:
                    i = m  # ladder in [m, sz - 1]

            return -1  # ladder not found

        ip = pivot()
        if ip == -1:  # ladder not found
            if sz > 1:  # input array is monotone
                ip = 1
            elif sz == 1:  # single element
                return 0 if ns[0] == t else -1
            else:  # empty array
                return -1

        ie = bisect_left(ns, t, 0, ip - 1)
        if ie < sz and ns[ie] == t:
            return ie

        ie = bisect_left(ns, t, ip, sz)
        if ie < sz and ns[ie] == t:
            return ie

        return -1
