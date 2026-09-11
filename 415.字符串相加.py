s = '''给定两个字符串形式的非负整数 num1 和 num2，计算它们的和并同样以字符串形式返回。

你不能使用任何内建的用于处理大整数的库（如 BigInteger），也不能直接将输入转换为整数。

示例 1：
输入：num1 = "11", num2 = "123"
输出："134"

示例 2：
输入：num1 = "456", num2 = "77"
输出："533"

示例 3：
输入：num1 = "0", num2 = "0"
输出："0"

提示：
1 <= num1.length, num2.length <= 10^4
num1 和 num2 都只包含数字 0-9
num1 和 num2 都不包含任何前导零（除了数字 0 本身）
'''


class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        pass


if __name__ == '__main__':
    solution = Solution()

    # Test Case 1
    num1_1 = "11"
    num2_1 = "123"
    result1 = solution.addStrings(num1_1, num2_1)
    assert result1 == "134"

    # Test Case 2
    num1_2 = "456"
    num2_2 = "77"
    result2 = solution.addStrings(num1_2, num2_2)
    assert result2 == "533"

    # Test Case 3
    num1_3 = "0"
    num2_3 = "0"
    result3 = solution.addStrings(num1_3, num2_3)
    assert result3 == "0"

    print("所有测试用例通过！")
