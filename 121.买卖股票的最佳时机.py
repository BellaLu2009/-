s = '''给定一个数组 prices ，它的第 i 个元素 prices[i] 表示一支给定股票第 i 天的价格。

你只能选择 某一天 买入这只股票，并选择在 未来的某一个不同的日子 卖出该股票。设计一个算法来计算你所能获取的最大利润。

返回你可以从这笔交易中获取的最大利润。如果你不能获取任何利润，返回 0 。


示例 1：

输入：[7,1,5,3,6,4]
输出：5
解释：在第 2 天（股票价格 = 1）的时候买入，在第 5 天（股票价格 = 6）的时候卖出，最大利润 = 6-1 = 5 。
     注意利润不能是 7-1 = 6, 因为卖出价格需要大于买入价格。

示例 2：

输入：prices = [7,6,4,3,1]
输出：0
解释：在这种情况下, 没有交易完成, 所以最大利润为 0。


提示：

1 <= prices.length <= 10^5
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
    assert profit1 == 5

    # Test Case 2
    prices2 = [7, 6, 4, 3, 1]
    profit2 = solution.maxProfit(prices2)
    assert profit2 == 0

    # Test Case 3 (Empty array - though constraints say 1 <= length)
    # prices3 = []
    # profit3 = solution.maxProfit(prices3)
    # assert profit3 == 0

    # Test Case 4 (Single element)
    prices4 = [5]
    profit4 = solution.maxProfit(prices4)
    assert profit4 == 0

    # Test Case 5 (Increasing prices)
    prices5 = [1, 2, 3, 4, 5]
    profit5 = solution.maxProfit(prices5)
    assert profit5 == 4

    # Test Case 6 (Decreasing prices)
    prices6 = [5, 4, 3, 2, 1]
    profit6 = solution.maxProfit(prices6)
    assert profit6 == 0

    # Test Case 7 (Complex case)
    prices7 = [2, 4, 1]
    profit7 = solution.maxProfit(prices7)
    assert profit7 == 2

    print("所有测试用例通过！")
