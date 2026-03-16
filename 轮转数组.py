s = '''给定一个整数数组 nums，将数组中的元素向右轮转 k 个位置，其中 k 是非负数。


示例 1:

输入: nums = [1,2,3,4,5,6,7], k = 3
输出: [5,6,7,1,2,3,4]
解释:
向右轮转 1 步: [7,1,2,3,4,5,6]
向右轮转 2 步: [6,7,1,2,3,4,5]
向右轮转 3 步: [5,6,7,1,2,3,4]

示例 2:

输入: nums = [-1,-100,3,99], k = 2
输出: [3,99,-1,-100]
解释:
向右轮转 1 步: [99,-1,-100,3]
向右轮转 2 步: [3,99,-1,-100]


提示：

1 <= nums.length <= 10^5
-2^31 <= nums[i] <= 2^31 - 1
0 <= k <= 10^5

进阶：

尽可能想出更多的解决方案，至少有 三种 不同的方法可以解决这个问题。
你可以使用空间复杂度为 O(1) 的 原地 算法解决这个问题吗？
'''

class Solution:
    def rotate(self, nums: list[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        pass

if __name__ == '__main__':
    solution = Solution()

    # Test Case 1
    nums1 = [1, 2, 3, 4, 5, 6, 7]
    k1 = 3
    solution.rotate(nums1, k1)
    assert nums1 == [5, 6, 7, 1, 2, 3, 4]

    # Test Case 2
    nums2 = [-1, -100, 3, 99]
    k2 = 2
    solution.rotate(nums2, k2)
    assert nums2 == [3, 99, -1, -100]

    # Test Case 3 (k is 0)
    nums3 = [1, 2, 3]
    k3 = 0
    solution.rotate(nums3, k3)
    assert nums3 == [1, 2, 3]

    # Test Case 4 (k is equal to length)
    nums4 = [1, 2, 3, 4]
    k4 = 4
    solution.rotate(nums4, k4)
    assert nums4 == [1, 2, 3, 4]

    # Test Case 5 (k is greater than length)
    nums5 = [1, 2, 3]
    k5 = 5 # equivalent to k = 2
    solution.rotate(nums5, k5)
    assert nums5 == [2, 3, 1]

    # Test Case 6 (Single element)
    nums6 = [10]
    k6 = 100
    solution.rotate(nums6, k6)
    assert nums6 == [10]

    print("所有测试用例通过！")
