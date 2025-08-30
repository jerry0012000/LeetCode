# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummyHead = ListNode(0) # 创建哑节点，哑节点是一个虚拟的节点，常用来简化链表的处理，特别是当我们需要在链表的头部插入节点时。这样，dummyHead 作为链表的开始，不会影响链表本身的结构。
        tail = dummyHead # tail 是当前链表的最后一个节点。我们从 dummyHead 开始构建新的链表，每次插入一个新节点后，tail 会向后移动。
        # 这样做的好处是，我们不需要处理链表头部的特殊情况，只需要直接操作 tail.next 来插入新节点。
        carry = 0 # 进位
        while l1 is not None or l2 is not None or carry != 0:
            # l1 is not None：l1 链表还有未处理的节点。
            # l2 is not None：l2 链表还有未处理的节点。
            # carry != 0：上一次加法可能产生进位，进位也要继续参与下一次加法。
            digit1 = l1.val if l1 is not None else 0
            digit2 = l2.val if l2 is not None else 0

            sum = digit1 + digit2 + carry
            digit = sum % 10 # 余数
            carry = sum // 10 # 是否进位

            newNode = ListNode(digit) # 加上去一个节点
            tail.next = newNode # 写入新链表
            tail = tail.next

            l1 = l1.next if l1 is not None else None
            l2 = l2.next if l2 is not None else None

        result = dummyHead.next
        dummyHead.next = None
        return result
