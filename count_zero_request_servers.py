class Solution:
    def countServers(self, n: int, logs: List[List[int]], x: int, queries: List[int]) -> List[int]:
        logs.sort(key=lambda a: a[1])

        sorted_queries = sorted((q, i) for i, q in enumerate(queries))

        count = [0] * (n + 1)
        active = 0
        left = right = 0

        ans = [0] * len(queries)

        for q, idx in sorted_queries:
            start = q - x

            # Add logs within the current time window
            while right < len(logs) and logs[right][1] <= q:
                server = logs[right][0]
                if count[server] == 0:
                    active += 1
                count[server] += 1
                right += 1

            # Remove logs outside the current time window
            while left < right and logs[left][1] < start:
                server = logs[left][0]
                count[server] -= 1
                if count[server] == 0:
                    active -= 1
                left += 1

            ans[idx] = n - active

        return ans
