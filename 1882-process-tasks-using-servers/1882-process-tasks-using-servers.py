
import heapq
from typing import List

class Solution:
    def assignTasks(self, servers: List[int], tasks: List[int]) -> List[int]:

        available = [(w, i) for i, w in enumerate(servers)]
        heapq.heapify(available)

        busy = []
        result = []

        time = 0

        for i, duration in enumerate(tasks):

            time = max(time, i)

            # Release all servers that have finished
            while busy and busy[0][0] <= time:
                end, weight, server = heapq.heappop(busy)
                heapq.heappush(available, (weight, server))

            # If no server is available, advance time
            if not available:
                time = busy[0][0]

                while busy and busy[0][0] <= time:
                    end, weight, server = heapq.heappop(busy)
                    heapq.heappush(available, (weight, server))

            # Select the server with minimum weight and index
            weight, server = heapq.heappop(available)

            result.append(server)

            # Mark server as busy
            heapq.heappush(
                busy,
                (time + duration, weight, server)
            )

        return result
