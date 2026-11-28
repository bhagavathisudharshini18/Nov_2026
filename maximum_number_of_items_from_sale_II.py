class Solution:
    def maximumSaleItems(self, items: List[List[int]], budget: int) -> int:
        n = len(items)
        freq = [0] * (n + 1)
        for f, p in items:
            freq[f] += 1
        cnt = [0] * (n + 1)
        for f in range(1, n + 1):
            for j in range(f, n + 1, f):
                cnt[f] += freq[j]
        min_price = min(p for f, p in items)
        arr = []
        for f, p in items:
            free_count = cnt[f] - 1
            if free_count > 0 and p <= 2 * min_price:
                arr.append((p, free_count))
        arr.sort()
        ans = 0
        spent = 0
        for price, count in arr:
            if spent + price > budget:
                break
            take = min(count, (budget - spent) // price)
            ans += 2 * take
            spent += take * price
        ans += (budget - spent) // min_price
        return ans
