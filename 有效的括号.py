class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) % 2 != 0:
            return False
        stack = []
        # a = ""
        for a in s:
            if a == '(':
                stack.append(')')
                # print(1)
            elif a == '{':
                stack.append('}')
                # print(2)
            elif a == '[':
                stack.append(']')
                # print(3)
            else:
                if not stack:
                    return False
                elif stack.pop() != a:
                # if not stack or stack.pop() != a:
                #     print(4)
                    return False
            # print(5)
        return len(stack) == 0



if __name__ == '__main__':
    '''给定一个只包括 '('，')'，'{'，'}'，'['，']' 的字符串 s ，判断字符串是否有效。

有效字符串需满足：
左括号必须用相同类型的右括号闭合。
左括号必须以正确的顺序闭合。
每个右括号都有一个对应的相同类型的左括号。

示例 1：
输入：s = "()"
输出：true

示例 2：
输入：s = "()[]{}"
输出：true

示例 3：
输入：s = "(]"
输出：false'''
    solution = Solution()
    s = "(((())))))))"
    result = solution.isValid(s)
    print(result)
    # 期望的输出结果是 true
    # assert result is True
