from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        return None

if __name__ == '__main__':
    '''将两个升序链表合并为一个新的 升序 链表并返回。新链表是通过拼接给定的两个链表的所有节点组成的。 

示例 1：
输入：l1 = [1,2,4], l2 = [1,3,4]
输出：[1,1,2,3,4,4]

示例 2：
输入：l1 = [], l2 = []
输出：[]

示例 3：
输入：l1 = [], l2 = [0]
输出：[0]'''
    solution = Solution()
    # 构造测试用例
    l1 = ListNode(1, ListNode(2, ListNode(4)))
    l2 = ListNode(1, ListNode(3, ListNode(4)))
    
    result = solution.mergeTwoLists(l1, l2)
    
    # 简单的打印验证
    current = result
    output = []
    while current:
        output.append(current.val)
        current = current.next
    print(output)
    # 期望的输出结果是 [1, 1, 2, 3, 4, 4]
    assert output == [1, 1, 2, 3, 4, 4]
