s = '''给定两个数组 nums1 和 nums2 ，返回它们的交集。输出结果中的每个元素一定是唯一的。我们可以不考虑输出结果的顺序。

示例 1：
输入：nums1 = [1,2,2,1], nums2 = [2,2]
输出：[2]

示例 2：
输入：nums1 = [4,9,5], nums2 = [9,4,9,8,4]
输出：[9,4]

提示：
1 <= nums1.length, nums2.length <= 1000
0 <= nums1[i], nums2[i] <= 1000
'''


class Solution:
    def intersection(self, nums1: list[int], nums2: list[int]) -> list[int]:
        pass


if __name__ == '__main__':
    solution = Solution()

    # Test Case 1
    nums1_1 = [1, 2, 2, 1]
    nums2_1 = [2, 2]
    result1 = solution.intersection(nums1_1, nums2_1)
    assert sorted(result1) == [2]

    # Test Case 2
    nums1_2 = [4, 9, 5]
    nums2_2 = [9, 4, 9, 8, 4]
    result2 = solution.intersection(nums1_2, nums2_2)
    assert sorted(result2) == [4, 9]

    # Test Case 3 (no intersection)
    nums1_3 = [1, 3, 5]
    nums2_3 = [2, 4, 6]
    result3 = solution.intersection(nums1_3, nums2_3)
    assert result3 == []

    print("所有测试用例通过！")
