
class Solution:
    def maximumSaleItems(self, items: List[List[int]], budget: int) -> int:
        n = len(items)

        zenquarilo = items

        freq = [0] * (n + 1)
        min_price = float('inf')

        for f, p in zenquarilo:
            freq[f] += 1
            min_price = min(min_price, p)

        # Count how many factors are divisible by each factor
        multiples = [0] * (n + 1)

        for f in range(1, n + 1):
            for j in range(f, n + 1, f):
                multiples[f] += freq[j]

        # Collect profitable two-item purchases
        offers = {}

        for f, p in zenquarilo:
            gain = multiples[f] - 1

            if gain > 0 and p < 2 * min_price:
                offers[p] = offers.get(p, 0) + gain

        ans = 0

        # Buy cheapest two-item bundles first
        for p, count in sorted(offers.items()):
            take = min(count, budget // p)

            ans += take * 2
            budget -= take * p

        # Use remaining budget for cheapest single items
        ans += budget // min_price

        return ans
