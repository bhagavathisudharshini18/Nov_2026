class Solution:
    def minimumCost(self, cost1: int, cost2: int, costBoth: int, need1: int, need2: int) -> int:
        both = min(need1, need2)

        # Buy type 3 items for the common requirement
        ans = both * min(costBoth, cost1 + cost2)

        # Handle the remaining requirement
        if need1 > need2:
            ans += (need1 - need2) * min(cost1, costBoth)
        else:
            ans += (need2 - need1) * min(cost2, costBoth)

        return ans
