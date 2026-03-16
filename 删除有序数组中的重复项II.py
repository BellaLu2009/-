s = '''给你一个有序数组 nums ，请你 原地 删除重复出现的元素，使得出现次数超过两次的元素只保留两次，并返回删除后数组的新长度。

不要使用额外的数组空间，你必须在 原地 修改输入数组 并在使用 O(1) 额外空间的条件下完成。

评测机将使用以下代码测试您的解决方案：

int[] nums = [...]; // 输入数组
int[] expectedNums = [...]; // 长度正确的预期答案。
                            // 它以不等于 val 的值排序。

int k = removeDuplicates(nums); // 调用你的实现

assert k == expectedNums.length;
for (int i = 0; i < actualLength; i++) {
    assert nums[i] == expectedNums[i];
}
如果所有的断言都通过，你的解决方案将会 通过。


示例 1：

输入：nums = [1,1,1,2,2,3]
输出：5, nums = [1,1,2,2,3,_]
解释：你的函数应该返回 k = 5，并且 nums 中的前五个元素是 1, 1, 2, 2, 3 。
在返回的 k 个元素之外的任何东西都不重要。

示例 2：

输入：nums = [0,0,1,1,1,1,2,3,3]
输出：7, nums = [0,0,1,1,2,3,3,_,_]
解释：你的函数应该返回 k = 7，并且 nums 中的前七个元素是 0, 0, 1, 1, 2, 3, 3 。
在返回的 k 个元素之外的任何东西都不重要。


提示：

1 <= nums.length <= 3 * 10^4
-10^4 <= nums[i] <= 10^4
nums 已按 非递减顺序 排列
'''

class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:
        pass

if __name__ == '__main__':
    solution = Solution()

    # Test Case 1
    nums1 = [1, 1, 1, 2, 2, 3]
    k1 = solution.removeDuplicates(nums1)
    assert k1 == 5
    assert nums1[:k1] == [1, 1, 2, 2, 3]

    # Test Case 2
    nums2 = [0, 0, 1, 1, 1, 1, 2, 3, 3]
    k2 = solution.removeDuplicates(nums2)
    assert k2 == 7
    assert nums2[:k2] == [0, 0, 1, 1, 2, 3, 3]

    # Test Case 3 (No duplicates)
    nums3 = [1, 2, 3, 4, 5]
    k3 = solution.removeDuplicates(nums3)
    assert k3 == 5
    assert nums3[:k3] == [1, 2, 3, 4, 5]

    # Test Case 4 (All same elements, more than two)
    nums4 = [1, 1, 1, 1, 1]
    k4 = solution.removeDuplicates(nums4)
    assert k4 == 2
    assert nums4[:k4] == [1, 1]

    # Test Case 5 (Empty array)
    nums5 = []
    k5 = solution.removeDuplicates(nums5)
    assert k5 == 0
    assert nums5[:k5] == []

    # Test Case 6 (Single element)
    nums6 = [7]
    k6 = solution.removeDuplicates(nums6)
    assert k6 == 1
    assert nums6[:k6] == [7]

    # Test Case 7 (Elements with exactly two duplicates)
    nums7 = [1, 1, 2, 2, 3, 3]
    k7 = solution.removeDuplicates(nums7)
    assert k7 == 6
    assert nums7[:k7] == [1, 1, 2, 2, 3, 3]

    print("所有测试用例通过！")
