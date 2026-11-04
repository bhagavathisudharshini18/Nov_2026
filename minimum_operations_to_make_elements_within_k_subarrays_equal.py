class Solution:
    def minOperations(self, nums: List[int], x: int, k: int) -> int:
        n = len(nums)

        vals = sorted(set(nums))
        m = len(vals)

        rank = {v: i + 1 for i, v in enumerate(vals)}

        class Fenwick:
            def __init__(self):
                self.bit = [0] * (m + 1)

            def update(self, i, val):
                while i <= m:
                    self.bit[i] += val
                    i += i & -i

            def query(self, i):
                res = 0
                while i > 0:
                    res += self.bit[i]
                    i -= i & -i
                return res

            def kth(self, k):
                idx = 0
                step = 1 << (m.bit_length() - 1)
                while step:
                    nxt = idx + step
                    if nxt <= m and self.bit[nxt] < k:
                        idx = nxt
                        k -= self.bit[nxt]
                    step >>= 1
                return idx + 1

        cnt = Fenwick()
        sm = Fenwick()

        def update(v, d):
            p = rank[v]
            cnt.update(p, d)
            sm.update(p, v * d)

        def get_cost():
            mid = (x + 1) // 2
            p = cnt.kth(mid)
            med = vals[p - 1]

            c = cnt.query(p)
            s = sm.query(p)
            total = sm.query(m)

            return med * c - s + total - s - med * (x - c)

        costs = []

        for i in range(x):
            update(nums[i], 1)

        costs.append(get_cost())

        for i in range(x, n):
            update(nums[i - x], -1)
            update(nums[i], 1)
            costs.append(get_cost())

        INF = float('inf')
        prev = [0] * (n + 1)

        for j in range(1, k + 1):
            curr = [INF] * (n + 1)

            for i in range(1, n + 1):
                curr[i] = curr[i - 1]

                if i >= x:
                    curr[i] = min(
                        curr[i],
                        prev[i - x] + costs[i - x]
                    )

            prev = curr

        return prev[n]
