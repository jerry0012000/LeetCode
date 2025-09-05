class LRUCache:
    # LRU Cache（最近最少使用缓存）
    class Node:
        def __init__(self, key: int, value: int):
            self.key = key
            self.value = value
            self.prev = None
            self.next = None

    def __init__(self, capacity: int):
        self.cap = capacity
        self.head = self.Node(-1, -1)
        self.tail = self.Node(-1, -1)
        self.head.next = self.tail
        self.tail.prev = self.head
        self.dic = dict()
        # head 和 tail 永远存在，不存储实际数据。
        # 新节点总是插入在 head 后面（表示“最新使用”）。
        # 删除节点时，只需要修改它的前后指针，不需要遍历。

    def addNode(self, newnode):
        temp = self.head.next # 取出原来head后面的第一个节点
        newnode.next = temp # 新节点的next指向temp
        newnode.prev = self.head # 新节点的prev指向head
        self.head.next = newnode # head的next指向新节点
        temp.prev = newnode # 原来的第一个节点的prev指向新节点

    def deleteNode(self, delnode):
        prevv = delnode.prev # 待删除节点的前一个
        nextt = delnode.next # 待删除节点的后一个
        prevv.next = nextt # 前一个的next改成后一个
        nextt.prev = prevv # 后一个的prev改成前一个

    def get(self, key: int) -> int:
        if key in self.dic:
            resNode = self.dic[key] # 从哈希表里删掉旧引用
            ans = resNode.value 
            del self.dic[key] # 删除字典里的内容，这个节点马上要移动到表头，如果不删掉旧的self.m[key]，它可能指向错误的节点。删掉后，等节点加到表头，再用 self.m[key] = self.head.next 更新成新位置。这样保证 dict 里始终存的是 key 对应的最新节点位置。
            self.deleteNode(resNode) # 从链表里删掉旧位置
            self.addNode(resNode) # 把节点重新加到表头（表示最新使用）
            self.dic[key] = self.head.next # 在哈希表里更新 key -> 新位置
            return ans
        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.dic: # 如果 key 已经存在
            current = self.dic[key]
            del self.dic[key] # 删除旧引用
            self.deleteNode(current) # 从链表里删掉旧节点
        
        if len(self.dic) == self.cap: # 缓存满了
            del self.dic[self.tail.prev.key] # 从哈希表删除最久未使用的节点
            self.deleteNode(self.tail.prev) # 从链表删除最久未使用的节点

        self.addNode(self.Node(key, value)) # 把这个节点移到链表头
        self.dic[key] = self.head.next # 更新哈希表的值


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
