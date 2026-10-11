class Solution:
    def sumOfSquares(self, nums: List[int]) -> int:
        n = len(nums)
        ans = 0

        for i, num in enumerate(nums, 1):
            if n % i == 0:
                ans += num * num

        return ans