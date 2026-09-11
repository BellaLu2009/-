s = '''给你一个非空数组，返回此数组中 第三大的数。如果不存在，则返回数组中最大的数。

示例 1：
输入：nums = [3,2,1]
输出：1

示例 2：
输入：nums = [1,2]
输出：2

示例 3：
输入：nums = [2,2,3,1]
输出：1

提示：
1 <= nums.length <= 10^4
-2^31 <= nums[i] <= 2^31 - 1
'''


class Solution:
    def thirdMax(self, nums: list[int]) -> int:
        pass


if __name__ == '__main__':
    solution = Solution()

    # Test Case 1
    nums1 = [3, 2, 1]
    result1 = solution.thirdMax(nums1)
    assert result1 == 1

    # Test Case 2
    nums2 = [1, 2]
    result2 = solution.thirdMax(nums2)
    assert result2 == 2

    # Test Case 3
    nums3 = [2, 2, 3, 1]
    result3 = solution.thirdMax(nums3)
    assert result3 == 1

    print("所有测试用例通过！")
