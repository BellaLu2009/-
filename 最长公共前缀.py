from typing import List

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:

        string = strs[0]
        # len(strs)=n
        for i in range(1, len(strs)):
            print(1, 0 + i, string in strs[0 + i])
            # 循环长度
            while string not in strs[0+i]:
                # while not strs[i].startswith(string):
                string = string[0:-1]
                print(string)
                # string出现在了strs列表里的当前字符串的下一个字符串
                # if string in strs[0 + i]:
                #     break
            # print(string in strs[0 + 2])
            # while True:
            #     string = string[0:-1]
            #     print(string)
            #     if string in strs[0+2]:
            #         break
        print(string)
        return string

if __name__ == '__main__':
    '''编写一个函数来查找字符串数组中的最长公共前缀。

如果不存在公共前缀，返回空字符串 ""。
    

示例 1：
输入：strs = ["flower","flow","flight"]
输出："fl"

示例 2：
输入：strs = ["dog","racecar","car"]
输出：""
解释：输入不存在公共前缀。'''
    solution = Solution()

    a = list(dict.keys())



    strs = ["a","b","c"]
    result = solution.longestCommonPrefix(strs)
    print(result)
    # 期望的输出结果是 "fl"
    assert result == ""


    # string = "dogggggggggggggggggggggggggggggggggggg"
    # print(string)
    # length = len(string)
    # print(length)
    # print(string[0])
    # print(string[-1])
    # print(string[2:5])
    # string="do"+"g"*3
    # print(string)
    # print(string.find("g"))
    # stri="ggg"
    # print(stri in string)



