s = '''给定一个包含大小写字母的字符串 s，返回通过这些字母可以构造的 最长回文串 的长度。

字母区分大小写，例如 "Aa" 不能当成相同字符。

示例 1：
输入：s = "abccccdd"
输出：7
解释：可以构造成 "dccaccd"，长度为 7。

示例 2：
输入：s = "a"
输出：1

提示：
1 <= s.length <= 2000
s 仅由大小写英文字母组成
'''


class Solution:
    def longestPalindrome(self, s: str) -> int:
        pass


if __name__ == '__main__':
    solution = Solution()

    # Test Case 1
    s1 = "abccccdd"
    result1 = solution.longestPalindrome(s1)
    assert result1 == 7

    # Test Case 2
    s2 = "a"
    result2 = solution.longestPalindrome(s2)
    assert result2 == 1

    # Test Case 3
    s3 = "bb"
    result3 = solution.longestPalindrome(s3)
    assert result3 == 2

    print("所有测试用例通过！")
