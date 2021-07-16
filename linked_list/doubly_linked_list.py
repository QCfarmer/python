class DNode():
    def __init__(self,data,prev=None,next=None):
        self.data = data
        self._prev = prev
        self._next = next
    def __str__(self):
        if self._next == None:
            return '{}'.format(self.data)
        else:
            return '{}⇄{}'.format(self.data,self._next)

class DLinkedList:
    '''
    双向链表
    '''
    def __init__(self):
        self._head = None

    def find_by_value(self,value):
        p = self._head
        while p != None and p.data != value:
            p = p._next
        return p

    def find_by_node(self,node:DNode):
        return self.find_by_value(node.data)

    def find_by_index(self, index: int) -> DNode:
        p = self._head
        position = 0
        while p and position != index:
            p = p._next
            position += 1
        return p

    def insert_value_to_head(self, value: int):
        new_node = DNode(value)
        self.insert_node_to_head(new_node)

    def insert_node_to_head(self, new_node: DNode):
        if new_node: #判断是否为空节点  
            if self._head == None:
                self._head = new_node
            else:
                new_node._next = self._head
                new_node._prev = self._head._prev
                self._head._prev = new_node
                self._head = new_node
        else:
            print('empty node')

    def insert_value_to_tail(self,value:int):
        new_node = DNode(value)
        self.insert_node_to_tail(new_node)

    def insert_node_to_tail(self,new_node:DNode):
        if not new_node:
            return
        else:
            p = self._head
            while p._next != None:
                p = p._next
            new_node._next = p._next
            new_node._prev = p
            p._next = new_node

    def insert_value_after_node(self, node: DNode, value: int):
        new_node = DNode(value)
        self.insert_node_after_node(node, new_node)

    def insert_node_after_node(self, node: DNode, new_node: DNode):
        if not node or not new_node:
            print('empty node or new_node')
            return
        else:
            new_node._prev = node
            new_node._next = node._next
            node._next._prev = new_node
            node._next = new_node

    def insert_value_before_node(self, node: DNode, value: int):
        new_node = DNode(value)
        self.insert_node_before_node(node, new_node)

    def insert_node_before_node(self, node: DNode, new_node: DNode):
        if not self._head or not node or not new_node: #空链表
            print('empty linked list or node or new_node')
            return
        if self._head == node: #该节点为头节点
            self.insert_node_to_head(new_node)
            return
        else:
            current = self._head
            while current._next and current._next != node: #在尾节点之前寻找该节点
                current = current._next
            if not current._next: #没有找到该节点
                print('no such node')
                return
            else:
                new_node._prev = node._prev
                new_node._next = node
                node._prev._next = new_node
                node._prev = new_node

    def delete_by_node(self, node: DNode):
        if not self._head or not node:#空链表
            print('empty linked list or empty node')
            return
        elif node._next: #要删除的节点不是尾节点
            #将要删除的节点直接修改为下一节点，即改变了当前位置的数据
            node.data = node._next.data
            node._next = node._next._next
            return
        else:
            current = self._head
            while current and current._next != node:
                current = current._next
            if not current: #遍历完整个链表没有找到该节点current=None
                print('no such node')
                return
            else: #尾节点
                current._next = node._next

    def delete_by_value(self, value: int): #删除所有为该值的节点，不会显示链表中是否存在该值
        if not self._head or value == None: #空链表或删除的值为空
            # 大坑，不能写成 not value，如果value=0,那么not value就会进入下面的选择，实际数字0是有意义的
            print('empty linked list or value')
            return
        else:
            fake_head = DNode('fake')
            fake_head._next = self._head
            fake_head._prev = self._head._prev
            prev, current = fake_head, self._head
            while current: #当前值不为空，即尾节点的next
                current._prev = prev
                if current.data != value:
                    prev._next = current
                    prev = prev._next
                current = current._next
            if prev._next:
                prev._next = current
            self._head = fake_head._next #该值正好是头节点
            self._head._prev = fake_head._prev
    
    def __repr__(self):
        if self._head == None:
            return 'empty linked list'
        else:
            return '{}'.format(self._head)

    # 重写__iter__方法，方便for关键字调用打印值
    def __iter__(self):
        node = self._head
        while node:
            yield node.data
            node = node._next

if __name__ == "__main__":

    # 测试单链表
    l = DLinkedList()
    print(l)
    for i in range(15):
        l.insert_value_to_head(i)
    print(l)
    node9 = l.find_by_value(9)
    print(node9)
    l.insert_value_to_tail(77)
    node88 = DNode(88)
    l.insert_node_to_tail(node88)
    print(l)
    l.insert_value_before_node(node9, 20)
    l.insert_value_before_node(node9, 16)
    l.insert_value_before_node(node9, 16)
    print(l)
    l.delete_by_value(16)
    print(l)
    l.delete_by_node(node88)
    print(l)
    node0 = l.find_by_index(0)
    l.delete_by_node(node0)
    print(l)
    l.insert_node_to_head(node88)
    print(l)
    l.delete_by_value(88)
    print(l)
    l.delete_by_value(0)
    print(l)
    for value in l:
        print(value)