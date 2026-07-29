class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        window_sum = sum(nums[:k])
        max_sum = window_sum
        for right in range (k, len(nums)):
            window_sum -= nums[right - k]
            window_sum += nums[right]
            max_sum = max(max_sum,window_sum)
        return max_sum / k