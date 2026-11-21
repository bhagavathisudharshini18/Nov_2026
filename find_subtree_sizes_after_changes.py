class Solution:
    def findSubtreeSizes(self, parent: List[int], s: str) -> List[int]:
        n = len(parent)
        children = [[] for _ in range(n)]
        for i in range(1, n):
            children[parent[i]].append(i)
        last = {}
        new_parent = [-1] * n
        def dfs(node):
            ch = s[node]
            old = last.get(ch, -1)
            new_parent[node] = old if old != -1 else parent[node]
            last[ch] = node
            for child in children[node]:
                dfs(child)
            if old == -1:
                last.pop(ch)
            else:
                last[ch] = old
        dfs(0)
        new_children = [[] for _ in range(n)]
        for i in range(1, n):
            new_children[new_parent[i]].append(i)
        ans = [1] * n
        def calculate(node):
            for child in new_children[node]:
                ans[node] += calculate(child)
            return ans[node]
        calculate(0)
        return ans
