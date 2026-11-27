class Solution:
    def maximumSaleItems(self, items: List[List[int]], budget: int) -> int:
        n = len(items)
        values = []
        for i in range(n):
            free = 0
            for j in range(n):
                if i != j and items[j][0] % items[i][0] == 0:
                    free += 1
            values.append(free + 1)
        groups = defaultdict(list)
        for i in range(n):
            factor, price = items[i]
            groups[price].append(values[i])
        dp = [0] * (budget + 1)
        ans = 0
        for p in sorted(groups.keys(), reverse=True):
            curr = [-1] * (budget + 1)
            for v in groups[p]:
                for b in range(budget, p - 1, -1):
                    if dp[b - p] >= 0:
                        curr[b] = max(curr[b], dp[b - p] + v)
                    if curr[b - p] >= 0:
                        curr[b] = max(curr[b], curr[b - p] + v)
            for b in range(budget + 1):
                if curr[b] >= 0:
                    ans = max(ans, curr[b] + (budget - b) // p)
            for b in range(budget + 1):
                dp[b] = max(dp[b], curr[b])
        return ans
