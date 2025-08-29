"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if head is None: 
            return None

        ## Step 1 : Add New Nodes in Between
        h1 = head
        while h1 :
            newNode = Node(h1.val)
            newNode.next = h1.next 
            h1.next = newNode
            h1 = h1.next.next # 添加后，还是把h1的指针指回以前的next，绕过了刚刚添加的节点。

        ## Step 2 : Add Links to New Nodes 
        h1 = head 
        while h1:
            if h1.random is not None :
                h1.next.random = h1.random.next # h1.next是对应的新节点, h1.random 是旧节点的 random 指针，指向某个旧节点, 那么 h1.random.next 一定是 h1.random 对应的新节点
                # 把新节点的 random 指向老节点 random 的下一个节点（即 random 对应的新节点）。
                # 这样我们就把新节点的 random 指向了正确的复制节点。
            h1 = h1.next.next 

        ## Step 3 : Break links and Separate the LLs
        h1 = head 
        resHead = h1.next # 新链表的头
        while h1.next: # 继续拆分链表，直到旧节点后面没有新节点了
            h2 = h1.next # 当前旧节点对应的新节点，把它记录在 h2
            h1.next = h1.next.next # 把原链表和新链表拆开。让旧节点 h1 的 next 指针跳过新节点 h2，直接指向下一个旧节点，这样旧链表恢复了一部分。
            if h1.next: # 用在单个节点检查时（不是循环），作用是“下一步有没有节点？如果有就做一些操作”，检查当前旧节点后面还有没有下一个旧节点（防止空指针）。
                h2.next = h1.next.next # h1.next 是下一个旧节点，下一个旧节点后面是它的新节点。所以让 h2.next 指向下一个新节点，把新链表也连起来。
                h1 = h1.next # h1 前进到下一个旧节点，继续循环
        return resHead
