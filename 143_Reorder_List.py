# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        fast = head
        slow = head

        # Step 1: Find the middle of the list
        while fast and fast.next: # 还没到末尾的时候，快指针走两步，慢指针走一步，分割链表。
            fast = fast.next.next
            slow = slow.next

        # Step 2: Reverse the second half of the list
        second = slow.next # 取出中点后面的部分
        slow.next = None # 断开前半部分和后半部分
        # 此时
        # first half:  1 -> 2 -> 3 -> None
        # second half: 4 -> 5
        node = None

        while second:
            temp = second.next # 保存后续节点
            second.next = node # 反转指针方向
            node = second # node 前移，相当于“新的头”
            second = temp # second 前移，继续下一个
        
        # 第一次循环：
        # second = 4
        # temp = 5
        # second.next = node → 4.next = None
        # node = 4
        # second = 5

        # 第二次循环：
        # second = 5
        # temp = None
        # second.next = node → 5.next = 4
        # node = 5
        # second = None（循环结束）

        # Step 3: Merge the two halves
        first = head # 前半部分
        second = node # 后半部分

        while second:
            temp1, temp2 = first.next, second.next
            first.next, second.next = second, temp1
            first, second = temp1, temp2
