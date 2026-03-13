from typing import List

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        # 存放去重之后的数据
        only_nums = []
        # 用来去重
        dic_1={}
        # 将原列表数据存入字典
        for a in nums:
            dic_1[a]=0
        print(dic_1)
        # 把字典里的键存入新列表
        for a in dic_1:
            only_nums.append(a)
        print(len(only_nums), only_nums)
        return len(only_nums),only_nums


if __name__ == '__main__':
    '''给你一个 升序排列 的数组 nums ，请你 原地 删除重复出现的元素，使每个元素 只出现一次 ，返回删除后数组的新长度。元素的相对顺序应该保持 一致 。然后返回 nums 中唯一元素的个数。

考虑 nums 的唯一元素的数量为 k ，你需要做以下事情确保你的题解可以被通过：

更改数组 nums ，使 nums 的前 k 个元素包含唯一元素，并按照它们最初在 nums 中出现的顺序排列。nums 的其余元素与 nums 的大小不重要。
返回 k 。

示例 1：
输入：nums = [1,1,2]
输出：2, nums = [1,2,_]
解释：函数应该返回新的长度 2 ，并且原数组 nums 的前两个元素被修改为 1, 2 。不需要考虑数组中超出新长度后面的元素。

示例 2：
输入：nums = [0,0,1,1,1,2,2,3,3,4]
输出：5, nums = [0,1,2,3,4,_,_,_,_,_]
解释：函数应该返回新的长度 5 ， 并且原数组 nums 的前五个元素被修改为 0, 1, 2, 3, 4 。不需要考虑数组中超出新长度后面的元素。'''
    solution = Solution()
    nums = [1,1,2]
    k,nums = solution.removeDuplicates(nums)
    print(k, nums)
    # 期望的输出结果是 2, [1, 2]
    assert k == 2
    assert nums[:k] == [1, 2]



#     有序字典
