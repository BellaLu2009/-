class Solution:
    def isPalindrome(self, x: int) -> bool:
        c = str(x)
        length = len(c)
        a = 0
        b = -1
        count=1

        while True:

            if c[a] == c[b]:
                print(c[a],c[b])

                if abs(b) + a > length:
                    print(length,count)

                    return True
                count += 1

                a += 1
                b -= 1
                # return True
            else:
                return False



if __name__ == '__main__':
    '''给你一个整数 x ，如果 x 是一个回文整数，返回 true ；否则，返回 false 。
    回文数是指正序（从左向右）和倒序（从右向左）读都是一样的整数。
    例如，121 是回文，而 123 不是。'''
    solution = Solution()
    x1 = 1765376819186735671

    result = solution.isPalindrome(x1)
    print(result)
    # 期望的输出结果是 True
    assert result is True

    # 123454321 13531 456  7 6 5 4 1234554321
    #                a0123-4-3-2-1b
    # 输入：一个整数 输出：true/false

    a=0
    b=-1
    #结束条件 abs(b)+a
#     if a对应的数字==b对应的数字:
#         a+=1
#         b-=1
#     else:
#         return False
#
#     # 123454321   4  -5   9   9
# #     13531       2  -3   5   5
# #     1234554321  4  -5   9   10
# #     5278725     3  -4   7   7
#       1753817183571   6  -7   13   13
#     17653768199186735671   9  -10   19   20
#
#     # str(数字)------字符串
#     # len（字符串）------字符串长度
#
#     作业：补成代码
#
#
#
#
#     c=str(input("输入"))
#     length = len(s)
#     a = 0
#     b = -1
#     while abs(b) + a < length:
#         if s[a] == s[b]:
#             a += 1
#             b -= 1
#         else:
#            return False
