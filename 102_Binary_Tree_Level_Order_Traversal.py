# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        # BFS（层序遍历），用队列一层一层扫
        if not root:
            return []
        # Q 保存当前层节点，temp 保存下一层节点
        # 每处理完一层，把 temp 赋值给 Q，继续下一层
        Q = deque([root])  # 当前层队列
        levels = [[root.val]]  # 最终答案
        temp = deque()  # 下一层队列
        # Q = [3]          # 当前层队列
        # levels = [[3]]   # 已收集的结果
        # temp = []        # 下一层队列
        while Q:
            node = Q.popleft()  # 取出队头节点
            if node.left: temp.append(node.left) # 把 3.left (9) 放入 temp
            if node.right: temp.append(node.right) # 3.right (20) 放入 temp

            # 如果当前层处理完了
            if not Q:# Q 空了 -> 说明当前层处理完，加入结果：levels = [[3], [9, 20]]
                if temp:  # 如果下一层有节点，说明确实有下一层，先把下一层的值存下来
                    levels.append([n.val for n in temp])
                Q = temp  # 下一层变成当前层，用下一层替换当前层
                temp = deque() # 把 temp 赋值给 Q，重置 temp：Q = [9, 20], temp = []，新建一个空的 deque，准备收集下一层

        return levels
