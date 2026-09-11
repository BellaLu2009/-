s = '''统计字符串中的单词个数。这里的单词是指由连续的非空格字符组成的序列。

请注意，字符串中可以包含前导或尾随空格，也可能有多个连续空格。

示例 1：
输入：s = "Hello, my name is John"
输出：5

示例 2：
输入：s = "Hello"
输出：1

提示：
0 <= s.length <= 300
s 由英文字母、数字、空格和常见标点符号组成
'''


class Solution:
    def countSegments(self, s: str) -> int:
        pass


if __name__ == '__main__':
    solution = Solution()

    # Test Case 1
    s1 = "Hello, my name is John"
    result1 = solution.countSegments(s1)
    assert result1 == 5

    # Test Case 2
    s2 = "Hello"
    result2 = solution.countSegments(s2)
    assert result2 == 1

    # Test Case 3
    s3 = "   fly me   to   the moon  "
    result3 = solution.countSegments(s3)
    assert result3 == 5

    print("所有测试用例通过！")
