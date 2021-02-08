class Solution(object):
    def stoneGame(self, piles):
        return True
        
#   Proof:
#
#   Th 1: Let dp1[i] - is the loot of player 1 at turn i
#   and dp2[i] same thing for player 2. Then dp1[i] >= dp2[i].
#
#   Proof by induction:
#
#   Let e1, e2 is the positions of current ends in pile.
#   (base) dp1[0] >= dp2[0] (Player one selects better of two loots)
#   (induction)
#   dp1[i] = dp1[i-1] + piles[ee1], where ee1 = argmax(piles[e1], piles[e2])
#   dp2[i] = dp2[i-1] + piles[ee2], where ee2 = argmin(piles[e1], piles[e2])
#   dp1[i-1] >= dp2[i-1] by I.H. and piles[ee1] >= piles[ee2]
#   END of Th.1 proof.
#
#   After N=len(piles) turns, game ends.
#   dp1[N] >= dp2[N], already proved.
#   There cannot be tie, since sum(piles) is odd (Task constraint).
#
#                         Q.E.D