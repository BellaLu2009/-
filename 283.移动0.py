s = '''给定一个数组 nums，编写一个函数将所有 0 移动到数组的末尾，同时保持非零元素的相对顺序。

请注意 ，你必须在不复制数组的情况下原地对数组进行操作。

示例 1:

输入: nums = [0,1,0,3,12]
输出: [1,3,12,0,0]

示例 2:

输入: nums = [0]
输出: [0]

提示:

1 <= nums.length <= 10^4
-2^31 <= nums[i] <= 2^31 - 1
'''


class Solution:
    def moveZeroes(self, nums: list[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        pass


if __name__ == '__main__':
    solution = Solution()

    # Test Case 1
    nums1 = [0, 1, 0, 3, 12]
    solution.moveZeroes(nums1)
    assert nums1 == [1, 3, 12, 0, 0]

    # Test Case 2
    nums2 = [0]
    solution.moveZeroes(nums2)
    assert nums2 == [0]

    # Test Case 3
    nums3 = [1, 0, 0, 2, 3]
    solution.moveZeroes(nums3)
    assert nums3 == [1, 2, 3, 0, 0]

    # Test Case 4
    nums4 = [1, 2, 3]
    solution.moveZeroes(nums4)
    assert nums4 == [1, 2, 3]

    # Test Case 5
    nums5 = [0, 0, 0]
    solution.moveZeroes(nums5)
    assert nums5 == [0, 0, 0]

    print("所有测试用例通过！")

