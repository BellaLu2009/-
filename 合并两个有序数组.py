s = '''给你两个按 非递减顺序 排列的整数数组 nums1 和 nums2，另有两个整数 m 和 n ，分别表示 nums1 和 nums2 中的元素数目。

请你 合并 nums2 到 nums1 中，使合并后的数组同样按 非递减顺序 排列。

注意：最终，合并后数组不应由函数返回，而是存储在数组 nums1 中。为了应对这种情况，nums1 的初始长度为 m + n，其中前 m 个元素表示应合并的元素，后 n 个元素为 0 ，应忽略。nums2 的长度为 n 。


示例 1：

输入：nums1 = [1,2,3,0,0,0], m = 3, nums2 = [2,5,6], n = 3
输出：[1,2,2,3,5,6]
解释：需要合并 [1,2,3] 和 [2,5,6] 。
合并结果是 [1,2,2,3,5,6] ，其中第一个粗体ented部分是 nums1 的内容，第二个粗体ented部分是 nums2 的内容。

示例 2：

输入：nums1 = [1], m = 1, nums2 = [], n = 0
输出：[1]
解释：需要合并 [1] 和 [] 。
合并结果是 [1] 。

示例 3：

输入：nums1 = [0], m = 0, nums2 = [1], n = 1
输出：[1]
解释：需要合并 [] 和 [1] 。
合并结果是 [1] 。
注意，因为 m = 0 ，所以 nums1 中没有元素。nums1 中仅存的 0 仅仅是为了确保合并结果可以存储在 nums1 中。


提示：

nums1.length == m + n
nums2.length == n
0 <= m, n <= 200
1 <= m + n <= 200
-10^9 <= nums1[i], nums2[j] <= 10^9
'''

class Solution:
    def merge(self, nums1: list[int], m: int, nums2: list[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        pass

if __name__ == '__main__':
    solution = Solution()

    # Test Case 1
    nums1_1 = [1, 2, 3, 0, 0, 0]
    m1 = 3
    nums2_1 = [2, 5, 6]
    n1 = 3
    solution.merge(nums1_1, m1, nums2_1, n1)
    assert nums1_1 == [1, 2, 2, 3, 5, 6]

    # Test Case 2
    nums1_2 = [1]
    m2 = 1
    nums2_2 = []
    n2 = 0
    solution.merge(nums1_2, m2, nums2_2, n2)
    assert nums1_2 == [1]

    # Test Case 3
    nums1_3 = [0]
    m3 = 0
    nums2_3 = [1]
    n3 = 1
    solution.merge(nums1_3, m3, nums2_3, n3)
    assert nums1_3 == [1]

    # Test Case 4: nums1 has elements, nums2 is empty
    nums1_4 = [4, 5, 6, 0, 0, 0]
    m4 = 3
    nums2_4 = []
    n4 = 0
    solution.merge(nums1_4, m4, nums2_4, n4)
    assert nums1_4 == [4, 5, 6, 0, 0, 0] # Should remain unchanged

    # Test Case 5: nums1 is empty (all zeros), nums2 has elements
    nums1_5 = [0, 0, 0]
    m5 = 0
    nums2_5 = [1, 2, 3]
    n5 = 3
    solution.merge(nums1_5, m5, nums2_5, n5)
    assert nums1_5 == [1, 2, 3]

    # Test Case 6: Negative numbers
    nums1_6 = [-1, 0, 0, 0, 0]
    m6 = 1
    nums2_6 = [-2, 1, 2]
    n6 = 3
    solution.merge(nums1_6, m6, nums2_6, n6)
    assert nums1_6 == [-2, -1, 0, 1, 2]

    print("所有测试用例通过！")
