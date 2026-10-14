class Solution:
    def maxSumOfSquares(self, num: int, sum: int) -> str:
        if sum > 9 * num:
            return ""

        nines, rem = divmod(sum, 9)

        ans = "9" * nines

        if rem > 0:
            ans += str(rem)

        ans += "0" * (num - len(ans))

        return ans