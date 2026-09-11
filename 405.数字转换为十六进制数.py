s = '''给定一个整数 num，返回它对应的十六进制字符串。对于负整数，通常使用补码方式表示。

所有字母 (a-f) 都必须是小写，且不能包含多余的前导 0；如果 num 为 0，返回 "0"。

示例 1：
输入：num = 26
输出："1a"

示例 2：
输入：num = -1
输出："ffffffff"

提示：
-2^31 <= num <= 2^31 - 1
'''


class Solution:
    def toHex(self, num: int) -> str:
        pass


if __name__ == '__main__':
    solution = Solution()

    # Test Case 1
    num1 = 26
    result1 = solution.toHex(num1)
    assert result1 == "1a"

    # Test Case 2
    num2 = -1
    result2 = solution.toHex(num2)
    assert result2 == "ffffffff"

    # Test Case 3
    num3 = 0
    result3 = solution.toHex(num3)
    assert result3 == "0"

    print("所有测试用例通过！")
