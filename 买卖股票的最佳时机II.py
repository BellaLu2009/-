s = '''给你一个整数数组 prices ，其中 prices[i] 表示某支股票第 i 天的价格。

在每一天，你可以决定是否购买和/或出售股票。你在任何时候 最多 只允许持有 一股 股票。你也可以先卖出，然后在 同一天 买入。

返回 你能获得的 最大 利润 。


示例 1：

输入：prices = [7,1,5,3,6,4]
输出：7
解释：在第 2 天（股票价格 = 1）的时候买入，在第 3 天（股票价格 = 5）的时候卖出, 这笔交易所能获得利润 = 5-1 = 4 。
     随后，在第 4 天（股票价格 = 3）的时候买入，在第 5 天（股票价格 = 6）的时候卖出, 这笔交易所能获得利润 = 6-3 = 3 。
     总利润为 4 + 3 = 7 。

示例 2：

输入：prices = [1,2,3,4,5]
输出：4
解释：在第 1 天（股票价格 = 1）的时候买入，在第 5 天 （股票价格 = 5）的时候卖出, 这笔交易所能获得利润 = 5-1 = 4 。
     总利润为 4 。

示例 3：

输入：prices = [7,6,4,3,1]
输出：0
解释：在这种情况下, 交易无法获得正利润，所以最大利润为 0 。


提示：

1 <= prices.length <= 3 * 10^4
0 <= prices[i] <= 10^4
'''

class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        pass

if __name__ == '__main__':
    solution = Solution()

    # Test Case 1
    prices1 = [7, 1, 5, 3, 6, 4]
    profit1 = solution.maxProfit(prices1)
    assert profit1 == 7

    # Test Case 2
    prices2 = [1, 2, 3, 4, 5]
    profit2 = solution.maxProfit(prices2)
    assert profit2 == 4

    # Test Case 3
    prices3 = [7, 6, 4, 3, 1]
    profit3 = solution.maxProfit(prices3)
    assert profit3 == 0

    # Test Case 4 (Single element)
    prices4 = [10]
    profit4 = solution.maxProfit(prices4)
    assert profit4 == 0

    # Test Case 5 (Alternating prices)
    prices5 = [1, 5, 2, 8, 3, 9]
    profit5 = solution.maxProfit(prices5)
    assert profit5 == (5-1) + (8-2) + (9-3) # 4 + 6 + 6 = 16

    # Test Case 6 (Two transactions)
    prices6 = [3, 3, 5, 0, 0, 3, 1, 4]
    profit6 = solution.maxProfit(prices6)
    assert profit6 == (5-3) + (3-0) + (4-1) # 2 + 3 + 3 = 8

    print("所有测试用例通过！")
