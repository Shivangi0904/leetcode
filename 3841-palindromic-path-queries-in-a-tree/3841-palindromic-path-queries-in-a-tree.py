
class Solution:
    def palindromePath(self, n: int, edges: list[list[int]],
                       s: str, queries: list[str]) -> list[bool]:

        suneravilo = (n, edges, s, queries)

        graph = [[] for _ in range(n)]
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)

        LOG = n.bit_length()
        parent = [[0] * n for _ in range(LOG)]
        depth = [0] * n
        tin = [0] * n
        tout = [0] * n
        prefix = [0] * n
        timer = 0

        # Iterative DFS: avoids recursion-depth errors
        stack = [(0, -1, 0, 0)]
        while stack:
            u, p, state, mask = stack.pop()

            if state == 0:
                tin[u] = timer
                timer += 1
                parent[0][u] = u if p == -1 else p
                prefix[u] = mask ^ (1 << (ord(s[u]) - 97))

                stack.append((u, p, 1, 0))

                for v in reversed(graph[u]):
                    if v != p:
                        depth[v] = depth[u] + 1
                        stack.append((v, u, 0, prefix[u]))
            else:
                tout[u] = timer - 1

        for k in range(1, LOG):
            for u in range(n):
                parent[k][u] = parent[k - 1][parent[k - 1][u]]

        def lca(u, v):
            if depth[u] < depth[v]:
                u, v = v, u

            diff = depth[u] - depth[v]
            for k in range(LOG):
                if diff & (1 << k):
                    u = parent[k][u]

            if u == v:
                return u

            for k in range(LOG - 1, -1, -1):
                if parent[k][u] != parent[k][v]:
                    u = parent[k][u]
                    v = parent[k][v]

            return parent[0][u]

        # Fenwick tree for subtree range-XOR updates
        # and point queries
        bit = [0] * (n + 2)

        def update(i, delta):
            i += 1
            while i <= n:
                bit[i] ^= delta
                i += i & -i

        def point_query(i):
            i += 1
            result = 0
            while i > 0:
                result ^= bit[i]
                i -= i & -i
            return result

        chars = list(s)
        answer = []

        for q in queries:
            parts = q.split()

            if parts[0] == "update":
                u = int(parts[1])
                c = parts[2]

                delta = (1 << (ord(chars[u]) - 97)) ^ (
                    1 << (ord(c) - 97)
                )

                if delta:
                    update(tin[u], delta)
                    if tout[u] + 1 < n:
                        update(tout[u] + 1, delta)

                chars[u] = c

            else:
                u, v = int(parts[1]), int(parts[2])
                w = lca(u, v)

                mask_u = prefix[u] ^ point_query(tin[u])
                mask_v = prefix[v] ^ point_query(tin[v])

                path_mask = (
                    mask_u ^ mask_v ^
                    (1 << (ord(chars[w]) - 97))
                )

                # At most one character may have an odd frequency
                answer.append((path_mask & (path_mask - 1)) == 0)

        return answer
