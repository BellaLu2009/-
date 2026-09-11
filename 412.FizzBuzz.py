s = '''给你一个整数 n，找出从 1 到 n 各个整数的 FizzBuzz 表示，并用字符串数组 answer 返回结果。

规则如下：
1. 如果 i 能被 3 整除，answer[i] == "Fizz"
2. 如果 i 能被 5 整除，answer[i] == "Buzz"
3. 如果 i 同时能被 3 和 5 整除，answer[i] == "FizzBuzz"
4. 如果都不满足，answer[i] == i 的字符串形式

示例 1：
输入：n = 3
输出：["1","2","Fizz"]

示例 2：
输入：n = 5
输出：["1","2","Fizz","4","Buzz"]

示例 3：
输入：n = 15
输出：["1","2","Fizz","4","Buzz","Fizz","7","8","Fizz","Buzz","11","Fizz","13","14","FizzBuzz"]

提示：
1 <= n <= 10^4
'''


class Solution:
    def fizzBuzz(self, n: int) -> list[str]:
        pass


if __name__ == '__main__':
    solution = Solution()

    # Test Case 1
    n1 = 3
    result1 = solution.fizzBuzz(n1)
    assert result1 == ["1", "2", "Fizz"]

    # Test Case 2
    n2 = 5
    result2 = solution.fizzBuzz(n2)
    assert result2 == ["1", "2", "Fizz", "4", "Buzz"]

    # Test Case 3
    n3 = 15
    result3 = solution.fizzBuzz(n3)
    assert result3[-1] == "FizzBuzz"

    print("所有测试用例通过！")
