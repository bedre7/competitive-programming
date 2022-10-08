from typing import OrderedDict


class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        self.mapify(prices)
        prices.sort()

        for i in range(len(prices)):
            buy = prices[i]
            for j in range(len(prices) - 1, -1, -1):
                
                # if prices[j] in self.stockMap[buy] and buy < prices[j]:
                    # return prices[j] - buy
            print('------')
        return 0

    def getIndex(self, value):
        return list(self.stockMap.keys())[list(self.stockMap.values()).index(value)]

    def mapify(self, prices: list[int]) -> map:
        idxToStockMap = {}
        for i, val in enumerate(prices):
            if val in idxToStockMap:
                idxToStockMap[val].append(i + 1)
            else:
                idxToStockMap[val] = [i + 1]

        self.stockMap = idxToStockMap


if __name__ == "__main__":
    sol = Solution()
    print(sol.mapify([2,1,2,0,1]))