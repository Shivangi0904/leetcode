
from math import gcd, lcm

class Solution:
    def maxLength(self, nums: List[int]) -> int:
        n = len(nums)
        ans = 0

        for i in range(n):
            prod = 1
            g = 0
            L = 1

            for j in range(i, n):
                prod *= nums[j]
                g = gcd(g, nums[j])
                L = lcm(L, nums[j])

                if prod == g * L:
                    ans = max(ans, j - i + 1)

        return ans
