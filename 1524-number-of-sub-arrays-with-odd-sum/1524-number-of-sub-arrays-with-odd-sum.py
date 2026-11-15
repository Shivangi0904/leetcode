
class Solution:
    def numOfSubarrays(self, arr: List[int]) -> int:
        MOD = 10**9 + 7

        count = [1, 0]  # [even prefix sums, odd prefix sums]
        prefix = 0
        ans = 0

        for num in arr:
            prefix = (prefix + num) % 2

            ans = (ans + count[1 - prefix]) % MOD

            count[prefix] += 1

        return ans
