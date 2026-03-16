s = '''给你一个数组 nums 和一个值 threshold，你需要 原地 移除所有数值小于 threshold 的元素。元素的顺序可能发生改变。然后返回 nums 中大于等于 threshold 的元素的数量。

假设 nums 中大于等于 threshold 的元素数量为 k，要通过此题，您需要执行以下操作：

更改 nums 数组，使 nums 的前 k 个元素包含大于等于 threshold 的元素。nums 的其余元素和 nums 的大小并不重要。
返回 k。
用户评测：

评测机将使用以下代码测试您的解决方案：

int[] nums = [...]; // 输入数组
int threshold = ...; // 要移除的值
int[] expectedNums = [...]; // 长度正确的预期答案。
                            // 它以大于等于 threshold 的值排序。

int k = removeElementsLessThanThreshold(nums, threshold); // 调用你的实现

assert k == expectedNums.length;
sort(nums, 0, k); // 排序 nums 的前 k 个元素
for (int i = 0; i < actualLength; i++) {
    assert nums[i] == expectedNums[i];
}
如果所有的断言都通过，你的解决方案将会 通过。

示例 1：

输入：nums = [3,2,2,3], threshold = 3
输出：2, nums = [3,3,_,_]
解释：你的函数应该返回 k = 2, 并且 nums 中的前两个元素均为 3。
你在返回的 k 个元素之外留下了什么并不重要（因此它们并不计入评测）。

示例 2：

输入：nums = [0,1,2,2,3,0,4,2], threshold = 2
输出：5, nums = [2,2,3,4,2,_,_,_]
解释：你的函数应该返回 k = 5，并且 nums 中的前五个元素为 2,2,3,4,2。
注意这五个元素可以任意顺序返回。
你在返回的 k 个元素之外留下了什么并不重要（因此它们并不计入评测）。

提示：

0 <= nums.length <= 100
0 <= nums[i] <= 50
0 <= threshold <= 100
'''


class Solution:
    def removeElementsLessThanThreshold(self, nums: list[int], threshold: int) -> int:
        pass


if __name__ == '__main__':
    solution = Solution()

    # Test Case 1
    nums1 = [3, 2, 2, 3]
    threshold1 = 3
    k1 = solution.removeElementsLessThanThreshold(nums1, threshold1)
    assert k1 == 2
    # 由于顺序不重要，我们只检查元素是否正确，不检查顺序
    assert sorted(nums1[:k1]) == sorted([3, 3])

    # Test Case 2
    nums2 = [0, 1, 2, 2, 3, 0, 4, 2]
    threshold2 = 2
    k2 = solution.removeElementsLessThanThreshold(nums2, threshold2)
    assert k2 == 5
    assert sorted(nums2[:k2]) == sorted([2, 2, 3, 4, 2])

    # Test Case 3 (All elements less than threshold)
    nums3 = [1, 2, 3]
    threshold3 = 4
    k3 = solution.removeElementsLessThanThreshold(nums3, threshold3)
    assert k3 == 0
    assert nums3[:k3] == []

    # Test Case 4 (All elements greater than or equal to threshold)
    nums4 = [5, 6, 7]
    threshold4 = 5
    k4 = solution.removeElementsLessThanThreshold(nums4, threshold4)
    assert k4 == 3
    assert sorted(nums4[:k4]) == sorted([5, 6, 7])

    # Test Case 5 (Empty array)
    nums5 = []
    threshold5 = 10
    k5 = solution.removeElementsLessThanThreshold(nums5, threshold5)
    assert k5 == 0
    assert nums5[:k5] == []

    print("所有测试用例通过！")
