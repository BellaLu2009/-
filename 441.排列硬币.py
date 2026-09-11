s = '''你总共有 n 枚硬币，并计划将它们按阶梯状排列。

对于一个由 k 行组成的阶梯，第 i 行必须恰好有 i 枚硬币。最后一行可能不完整。

给你一个整数 n，返回可形成的 完整阶梯行 的总行数。

示例 1：
输入：n = 5
输出：2
解释：因为第 3 行需要 3 枚硬币，但只剩 2 枚。

示例 2：
输入：n = 8
输出：3
解释：前 3 行共需要 1 + 2 + 3 = 6 枚，剩余 2 枚。

提示：
1 <= n <= 2^31 - 1
'''


class Solution:
    def arrangeCoins(self, n: int) -> int:
        pass


if __name__ == '__main__':
    solution = Solution()

    # Test Case 1
    n1 = 5
    result1 = solution.arrangeCoins(n1)
    assert result1 == 2

    # Test Case 2
    n2 = 8
    result2 = solution.arrangeCoins(n2)
    assert result2 == 3

    # Test Case 3
    n3 = 1
    result3 = solution.arrangeCoins(n3)
    assert result3 == 1

    print("所有测试用例通过！")
