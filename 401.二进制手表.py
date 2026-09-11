s = '''二进制手表顶部有 4 个 LED 代表 小时（0-11），底部有 6 个 LED 代表 分钟（0-59）。

每个 LED 代表一个 0 或 1，最低位在右侧。给定一个非负整数 turnedOn，表示当前亮着的 LED 数量，返回所有可能的时间。

答案可以按任意顺序返回。

示例 1：
输入：turnedOn = 1
输出：["0:01","0:02","0:04","0:08","0:16","0:32","1:00","2:00","4:00","8:00"]

示例 2：
输入：turnedOn = 9
输出：[]

提示：
0 <= turnedOn <= 10
'''


class Solution:
    def readBinaryWatch(self, turnedOn: int) -> list[str]:
        pass


if __name__ == '__main__':
    solution = Solution()

    # Test Case 1
    turned_on_1 = 1
    result1 = solution.readBinaryWatch(turned_on_1)
    assert "0:01" in result1
    assert "8:00" in result1

    # Test Case 2
    turned_on_2 = 9
    result2 = solution.readBinaryWatch(turned_on_2)
    assert result2 == []

    # Test Case 3
    turned_on_3 = 0
    result3 = solution.readBinaryWatch(turned_on_3)
    assert result3 == ["0:00"]

    print("所有测试用例通过！")
