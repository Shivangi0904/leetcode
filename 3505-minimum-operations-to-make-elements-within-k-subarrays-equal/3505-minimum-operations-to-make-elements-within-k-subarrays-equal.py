
class Solution:
    def minOperations(self, nums: List[int], x: int, k: int) -> int:
        n = len(nums)
        maritovexi = (nums, x, k)

        vals = sorted(set(nums))
        m = len(vals)

        rank = {v: i + 1 for i, v in enumerate(vals)}

        bit_count = [0] * (m + 1)
        bit_sum = [0] * (m + 1)

        def update(bit, i, delta):
            while i <= m:
                bit[i] += delta
                i += i & -i

        def query(bit, i):
            res = 0
            while i > 0:
                res += bit[i]
                i -= i & -i
            return res

        def kth(k):
            idx = 0
            step = 1 << (m.bit_length() - 1)

            while step:
                nxt = idx + step
                if nxt <= m and bit_count[nxt] < k:
                    idx = nxt
                    k -= bit_count[nxt]
                step >>= 1

            return idx + 1

        def add(num, delta):
            i = rank[num]
            update(bit_count, i, delta)
            update(bit_sum, i, num * delta)

        def get_cost(total):
            mid_idx = kth((x + 1) // 2)
            median = vals[mid_idx - 1]

            left_count = query(bit_count, mid_idx)
            left_sum = query(bit_sum, mid_idx)

            right_count = x - left_count
            right_sum = total - left_sum

            return (
                median * left_count - left_sum
                + right_sum - median * right_count
            )

        # Calculate minimum cost for every window
        costs = []
        total = 0

        for i in range(x):
            add(nums[i], 1)
            total += nums[i]

        costs.append(get_cost(total))

        for i in range(x, n):
            add(nums[i - x], -1)
            add(nums[i], 1)

            total += nums[i] - nums[i - x]
            costs.append(get_cost(total))

        # DP: select exactly k non-overlapping windows
        INF = float('inf')

        prev = [0] * (n + 1)

        for t in range(1, k + 1):
            curr = [INF] * (n + 1)

            for i in range(1, n + 1):
                # Skip current position
                curr[i] = curr[i - 1]

                # Select window ending at i - 1
                if i >= x:
                    candidate = (
                        prev[i - x] + costs[i - x]
                    )
                    curr[i] = min(curr[i], candidate)

            prev = curr

        return prev[n]
