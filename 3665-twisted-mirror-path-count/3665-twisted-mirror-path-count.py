
class Solution:
    def uniquePaths(self, grid: List[List[int]]) -> int:
        MOD = 10**9 + 7

        m, n = len(grid), len(grid[0])

        down = [0] * n
        down[0] = 1

        for i in range(m):
            right = 0

            for j in range(n):
                if grid[i][j] == 1:
                    right, down[j] = down[j], right
                else:
                    right = (right + down[j]) % MOD
                    down[j] = right

        return right
