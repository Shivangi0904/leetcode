
class Solution:
    def findSubtreeSizes(self, parent: List[int], s: str) -> List[int]:
        n = len(parent)
        children = [[] for _ in range(n)]

        for i in range(1, n):
            children[parent[i]].append(i)

        new_parent = [-1] * n
        last = {}

        def dfs(u):
            ch = s[u]
            old = last.get(ch, -1)

            last[ch] = u

            for v in children[u]:
                dfs(v)

            new_parent[u] = old if old != -1 else parent[u]

            if old == -1:
                last.pop(ch)
            else:
                last[ch] = old

        dfs(0)

        new_children = [[] for _ in range(n)]

        for i in range(1, n):
            new_children[new_parent[i]].append(i)

        ans = [0] * n

        def calc(u):
            ans[u] = 1
            for v in new_children[u]:
                ans[u] += calc(v)
            return ans[u]

        calc(0)
        return ans
