class Solution:
    def maxProduct(self, nums: List[int]) -> int:

        largest1 = 0
        largest2 = 0

        for num in nums:

            if num > largest1:
                largest2 = largest1
                largest1 = num

            elif num > largest2:
                largest2 = num

        return (largest1 - 1) * (largest2 - 1)