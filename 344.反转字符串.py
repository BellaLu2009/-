s = '''编写一个函数，其作用是将输入的字符串反转过来。输入字符串以字符数组 s 的形式给出。

不要给另外的数组分配额外的空间，你必须原地修改输入数组、使用 O(1) 的额外空间解决这一问题。

示例 1：
输入：s = ["h","e","l","l","o"]
输出：["o","l","l","e","h"]
s = s[::-1]
s=input str("enter a word:")
b=[]
# 从前往后循环s，把每一项加入到b的最前面
for i in s:
    b.insert(0,i)
for i in a:
    # n=b.append
    b是一个列表，往b里增加一个元素：b.append(元素)
    加到最前用：b.insert(0,元素)
    把a列表的最后一个换到b列表的第一个，以此类推
    


示例 2：
输入：s = ["H","a","n","n","a","h"]
输出：["h","a","n","n","a","H"]

提示：
1 <= s.length <= 10^5
s[i] 都是 ASCII 码表中的可打印字符
'''


class Solution:
    def reverseString(self, s: list[str]) -> None:

        """
        Do not return anything, modify s in-place instead.
        """
        b = []
        # 从前往后循环s，把每一项加入到b的最前面
        for i in s:
            b.insert(0, i)
        s = b
        pass


if __name__ == '__main__':
    solution = Solution()

    # Test Case 1
    s1 = ["h", "e", "l", "l", "o"]
    s1 = solution.reverseString(s1)
    assert s1 == ["o", "l", "l", "e", "h"]

    # Test Case 2
    s2 = ["H", "a", "n", "n", "a", "h"]
    s2 = solution.reverseString(s2)
    assert s2 == ["h", "a", "n", "n", "a", "H"]

    # Test Case 3 (single char)
    s3 = ["a"]
    s3 = solution.reverseString(s3)
    assert s3 == ["a"]

    print("所有测试用例通过！")
