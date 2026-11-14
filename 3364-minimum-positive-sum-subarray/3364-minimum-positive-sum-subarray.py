
from typing import List

class Solution:
    def minimumSumSubarray(self, nums: List[int], l: int, r: int) -> int:
        n = len(nums)
        prefix = [0] * (n + 1)

        for i in range(n):
            prefix[i + 1] = prefix[i] + nums[i]

        ans = float('inf')

        for start in range(n):
            for length in range(l, r + 1):
                end = start + length

                if end > n:
                    break

                total = prefix[end] - prefix[start]

                if total > 0:
                    ans = min(ans, total)

        return ans if ans != float('inf') else -1
