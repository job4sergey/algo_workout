#
#
#   #
#  ##
# ###
# ###     #
# ###    ##
# ###   ###
# ###  ####
# ### #####
# #########
#
#
# When splitting the search space into two arbitrary parts,
# one part is sorted while other is not.
# Check whether sorted part interval contains the target.
# If it is - then recurse into it, otherwise - recurse to other part

class Solution(object):
    def search(self, a, t):
        i, j = 0, len(a) - 1

        while i <= j:
            m = i + (j - i) // 2
            if a[m] == t:
                return m
            elif a[m] < a[j]:
                if a[m] < t <= a[j]:
                    i = m + 1
                else:
                    j = m - 1
            else:
                if a[i] <= t < a[m]:
                    j = m - 1
                else:
                    i = m + 1

        return -1
