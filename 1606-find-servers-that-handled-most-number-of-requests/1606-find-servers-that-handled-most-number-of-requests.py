
import heapq
from typing import List

class Solution:
    def busiestServers(self, k: int, arrival: List[int], load: List[int]) -> List[int]:

        # Segment tree: 1 means available, 0 means busy
        size = 1
        while size < k:
            size *= 2

        tree = [0] * (2 * size)

        for i in range(k):
            tree[size + i] = 1

        for i in range(size - 1, 0, -1):
            tree[i] = tree[2 * i] + tree[2 * i + 1]

        def update(pos, val):
            pos += size
            tree[pos] = val

            pos //= 2
            while pos:
                tree[pos] = tree[2 * pos] + tree[2 * pos + 1]
                pos //= 2

        def find_first(node, l, r, ql, qr):
            if r < ql or l > qr or tree[node] == 0:
                return -1

            if l == r:
                return l

            mid = (l + r) // 2

            res = find_first(
                node * 2, l, mid, ql, qr
            )

            if res != -1:
                return res

            return find_first(
                node * 2 + 1, mid + 1, r, ql, qr
            )

        busy = []
        count = [0] * k

        for i in range(len(arrival)):

            # Release completed servers
            while busy and busy[0][0] <= arrival[i]:
                end, server = heapq.heappop(busy)
                update(server, 1)

            start = i % k

            # Find available server >= start
            server = find_first(1, 0, size - 1, start, k - 1)

            # Wrap around if necessary
            if server == -1:
                server = find_first(1, 0, size - 1, 0, start - 1)

            # Drop request if no server is available
            if server == -1:
                continue

            count[server] += 1

            # Mark server as busy
            update(server, 0)

            heapq.heappush(
                busy,
                (arrival[i] + load[i], server)
            )

        maximum = max(count)

        return [
            i for i in range(k)
            if count[i] == maximum
        ]
