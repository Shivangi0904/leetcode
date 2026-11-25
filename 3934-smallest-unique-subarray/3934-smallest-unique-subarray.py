
class Solution:
    def smallestUniqueSubarray(self, nums: List[int]) -> int:
        n = len(nums)

        # Coordinate compression
        vals = {v: i for i, v in enumerate(sorted(set(nums)))}
        rank = [vals[x] for x in nums]

        # Build suffix array using doubling
        sa = list(range(n))
        k = 1

        while k < n:
            sa.sort(key=lambda i: (
                rank[i],
                rank[i + k] if i + k < n else -1
            ))

            new_rank = [0] * n

            for j in range(1, n):
                a, b = sa[j - 1], sa[j]

                prev = (
                    rank[a],
                    rank[a + k] if a + k < n else -1
                )
                curr = (
                    rank[b],
                    rank[b + k] if b + k < n else -1
                )

                new_rank[b] = new_rank[a] + (prev != curr)

            rank = new_rank

            if rank[sa[-1]] == n - 1:
                break

            k *= 2

        # Build LCP array using Kasai's algorithm
        pos = [0] * n

        for i, s in enumerate(sa):
            pos[s] = i

        lcp = [0] * n
        h = 0

        for i in range(n):
            p = pos[i]

            if p == 0:
                continue

            j = sa[p - 1]

            while (i + h < n and j + h < n
                   and nums[i + h] == nums[j + h]):
                h += 1

            lcp[p] = h

            if h:
                h -= 1

        # Find minimum unique prefix length
        ans = n

        for p in range(n):
            i = sa[p]

            common = max(
                lcp[p],
                lcp[p + 1] if p + 1 < n else 0
            )

            length = common + 1

            if length <= n - i:
                ans = min(ans, length)

        return ans
