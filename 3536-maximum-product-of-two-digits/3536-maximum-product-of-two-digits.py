class Solution:
    def maxProduct(self, n: int) -> int:
        lar1 = 0
        lar2 = 0
        while n > 0:
            digit = n % 10
            if digit > lar1:
                lar2 = lar1
                lar1 = digit
            elif digit > lar2:
                lar2 = digit
            n //= 10
        return lar1*lar2
