s = '''给定字符串 s 和 t ，判断 s 是否为 t 的子序列。

字符串的子序列是原始字符串删除一些（也可以不删除）字符而不改变剩余字符相对位置形成的新字符串。

示例 1：
输入：s = "abc", t = "ahbgdc"
输出：true

示例 2：
输入：s = "axc", t = "ahbgdc"
输出：false

提示：
0 <= s.length <= 100
0 <= t.length <= 10^4
s 和 t 仅由小写英文字母组成
'''


class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        pass


if __name__ == '__main__':
    solution = Solution()

    # Test Case 1
    s1 = "abc"
    t1 = "ahbgdc"
    result1 = solution.isSubsequence(s1, t1)
    assert result1 is True

    # Test Case 2
    s2 = "axc"
    t2 = "ahbgdc"
    result2 = solution.isSubsequence(s2, t2)
    assert result2 is False

    # Test Case 3 (empty s)
    s3 = ""
    t3 = "ahbgdc"
    result3 = solution.isSubsequence(s3, t3)
    assert result3 is True

    print("所有测试用例通过！")
