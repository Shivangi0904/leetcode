
class Solution:
    def canAliceWin(self, n: int) -> bool:
        turn = 10

        while n >= turn:
            n -= turn
            turn -= 1

        return turn % 2 == 9 % 2
