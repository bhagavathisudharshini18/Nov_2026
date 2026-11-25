class Solution:
    def smallestUniqueSubarray(self, nums: List[int]) -> int:
        n = len(nums)
        length = [0]
        link = [-1]
        nxt = [{}]
        occ = [0]
        last = 0
        for x in nums:
            cur = len(length)
            length.append(length[last] + 1)
            link.append(0)
            nxt.append({})
            occ.append(1)
            p = last
            while p != -1 and x not in nxt[p]:
                nxt[p][x] = cur
                p = link[p]
            if p == -1:
                link[cur] = 0
            else:
                q = nxt[p][x]
                if length[p] + 1 == length[q]:
                    link[cur] = q
                else:
                    clone = len(length)
                    length.append(length[p] + 1)
                    link.append(link[q])
                    nxt.append(nxt[q].copy())
                    occ.append(0)
                    while p != -1 and nxt[p].get(x) == q:
                        nxt[p][x] = clone
                        p = link[p]
                    link[q] = clone
                    link[cur] = clone
            last = cur
        order = sorted(range(1, len(length)), key = lambda i: length[i], reverse = True)
        for v in order:
            if link[v] != -1:
                occ[link[v]] += occ[v]
        ans = n
        for v in range(1, len(length)):
            if occ[v] == 1:
                ans = min(ans, length[link[v]] + 1)
        return ans
