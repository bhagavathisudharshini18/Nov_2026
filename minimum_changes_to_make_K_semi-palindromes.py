class Solution:
    def minimumChanges(self, s: str, k: int) -> int:
        n = len(s)

        # Calculate minimum changes to make every substring semi-palindrome
        cost = [[0] * n for _ in range(n)]

        for length in range(2, n + 1):
            for i in range(n - length + 1):
                j = i + length - 1
                best = float('inf')

                # Try every valid divisor
                for d in range(1, length):
                    if length % d != 0:
                        continue

                    changes = 0

                    # Compare characters in each group
                    for r in range(d):
                        left = i + r
                        right = i + r + ((length - 1 - r) // d) * d

                        while left < right:
                            if s[left] != s[right]:
                                changes += 1

                            left += d
                            right -= d

                    best = min(best, changes)

                cost[i][j] = best

        # DP: dp[p][i] = minimum changes to partition
        # first i characters into p semi-palindromes
        INF = float('inf')
        dp = [[INF] * (n + 1) for _ in range(k + 1)]

        dp[0][0] = 0

        for parts in range(1, k + 1):
            for i in range(2 * parts, n + 1):
                for j in range(2 * (parts - 1), i - 1):
                    dp[parts][i] = min(
                        dp[parts][i],
                        dp[parts - 1][j] + cost[j][i - 1]
                    )

        return dp[k][n]
