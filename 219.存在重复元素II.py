s = '''给你一个整数数组 nums 和一个整数 k ，判断数组中是否存在两个 不同的索引 i 和 j ，满足 nums[i] == nums[j] 且 abs(i - j) <= k 。如果存在，返回 true ；否则，返回 false 。


示例 1：

输入：nums = [1,2,3,1], k = 3
输出：true

示例 2：

输入：nums = [1,0,1,1], k = 1
输出：true

示例 3：

输入：nums = [1,2,3,1,2,3], k = 2
输出：false


提示：

1 <= nums.length <= 10^5
-10^9 <= nums[i] <= 10^9
0 <= k <= 10^5
'''

class Solution:
    def containsNearbyDuplicate(self, nums: list[int], k: int) -> bool:
        pass

if __name__ == '__main__':
    solution = Solution()

    # Test Case 1
    nums1 = [1, 2, 3, 1]
    k1 = 3
    result1 = solution.containsNearbyDuplicate(nums1, k1)
    assert result1 is True

    # Test Case 2
    nums2 = [1, 0, 1, 1]
    k2 = 1
    result2 = solution.containsNearbyDuplicate(nums2, k2)
    assert result2 is True

    # Test Case 3
    nums3 = [1, 2, 3, 1, 2, 3]
    k3 = 2
    result3 = solution.containsNearbyDuplicate(nums3, k3)
    assert result3 is False

    # Test Case 4 (No duplicates)
    nums4 = [1, 2, 3, 4, 5]
    k4 = 5
    result4 = solution.containsNearbyDuplicate(nums4, k4)
    assert result4 is False

    # Test Case 5 (k is 0)
    nums5 = [1, 1]
    k5 = 0
    result5 = solution.containsNearbyDuplicate(nums5, k5)
    assert result5 is False

    # Test Case 6 (Large k)
    nums6 = [1, 2, 3, 4, 1]
    k6 = 10
    result6 = solution.containsNearbyDuplicate(nums6, k6)
    assert result6 is True

    # Test Case 7 (Edge case)
    nums7 = [99, 99]
    k7 = 2
    result7 = solution.containsNearbyDuplicate(nums7, k7)
    assert result7 is True

    print("所有测试用例通过！")
