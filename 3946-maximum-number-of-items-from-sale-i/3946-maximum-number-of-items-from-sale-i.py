class Solution:
    def maximumSaleItems(self, items: List[List[int]], budget: int) -> int:
        n = len(items)
        cheapest = min(price for factor, price in items)

        profit = []

        for i in range(n):
            f = items[i][0]
            free = 0

            for j in range(n):
                if i != j and items[j][0] % f == 0:
                    free += 1

            profit.append(free + 1)

        dp = [-10**9] * (budget + 1)
        dp[0] = 0

        for i in range(n):
            factor, price = items[i]

            for b in range(budget, price - 1, -1):
                dp[b] = max(dp[b], dp[b - price] + profit[i])

        ans = 0

        for b in range(budget + 1):
            if dp[b] != -10**9:
                ans = max(ans, dp[b] + (budget - b) // cheapest)

        return ans