# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # 创建哑节点，指向头节点
        dummy = ListNode(0, head)
        fast = dummy
        slow = dummy
        
        # 先让fast走n+1步，保持fast和slow之间相隔n个节点
        for _ in range(n + 1):
            fast = fast.next
        
        # fast和slow一起走，直到fast到达末尾
        while fast:
        # (while fast: 和 while fast is not None: 是等价的写法。这样循环会一直走，直到 fast 变成 None（即走到链表末尾）。)
            fast = fast.next
            slow = slow.next
        
        # slow.next就是要删除的节点
        slow.next = slow.next.next
        
        # 返回新头节点
        return dummy.next
