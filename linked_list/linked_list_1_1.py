'''
改自原书代码 python/06_linkedlist/singly_linked_list.py
https://github.com/wangzheng0822/algo/blob/b2c1228ff915287ad7ebeae4355fa26854ea1557/python/06_linkedlist/singly_linked_list.py
为理解给原书代码添加了注释和部分打印消息
哨兵实现
'''

class Node:
    def __init__(self, data, next_node=None):
        self.data = data
        self._next = next_node
    def __repr__(self): #为实现打印链表，重写了节点的打印方法
        if self._next == None:
            return '{}'.format(self.data)
        else:
            return '{}->{}'.format(self.data,self._next)

class SinglyLinkedList:
    '''
    单链表
    添加哨兵
    '''
    def __init__(self):
        self._guard = Node(None)
        self._head = self._guard
        # self._tail = self._guard

    def find_by_value(self, value: int) -> Node:
        p = self._head._next
        while p != None and p.data != value:
            p = p._next
        return p
    
    # 有按值查找，也应有按节点查找
    # 用找节点的值的方法
    def find_by_node(self,node:Node):
        return self.find_by_value(node.data)

    def find_by_index(self, index: int) -> Node:
        p = self._head._next
        position = 0
        while p and position != index:
            p = p._next
            position += 1
        return p

    def insert_value_to_head(self, value: int):
        new_node = Node(value)
        self.insert_node_to_head(new_node)

    def insert_node_to_head(self, new_node: Node):
        if new_node: #判断是否为空节点   
            new_node._next = self._head._next
            self._head._next = new_node
        else:
            print('empty node')
            
    # 既然有从头插入，理应也有尾插
    def insert_value_to_tail(self,value:int):
        new_node = Node(value)
        self.insert_node_to_tail(new_node)

    def insert_node_to_tail(self,new_node:Node):
        if not new_node:
            return
        else:
            p = self._head._next
            while p._next != None:
                p = p._next
            p._next = new_node

    def insert_value_after_node(self, node: Node, value: int):
        new_node = Node(value)
        self.insert_node_after_node(node, new_node)

    def insert_node_after_node(self, node: Node, new_node: Node):
        if not node or not new_node:
            print('empty node or new_node')
            return
        else:
            new_node._next = node._next
            node._next = new_node

    def insert_value_before_node(self, node: Node, value: int):
        new_node = Node(value)
        self.insert_node_before_node(node, new_node)

    def insert_node_before_node(self, node: Node, new_node: Node):
        if not self._head._next or not node or not new_node: #空链表
            print('empty linked list or node or new_node')
            return
        else:
            current = self._head._next
            while current._next and current._next != node: #在尾节点之前寻找该节点
                current = current._next
            if not current._next: #没有找到该节点
                print('no such node')
                return
            else:
                new_node._next = node
                current._next = new_node

    # 重写一个删除节点的方法，参照插入值的方法，用删除值实现
    def delete_by_node(self, node: Node):
        value = node.data
        self.delete_by_value(value)

    def delete_by_value(self, value: int): #删除所有为该值的节点，不会显示链表中是否存在该值
        if not self._head._next or not value: #空链表或删除的值为空
            print('empty linked list or value')
            return
        else:
            prev, current = self._head, self._head._next
            while current: #当前值不为尾节点
                if current.data != value:
                    prev._next = current
                    prev = prev._next
                current = current._next
            if prev._next:
                prev._next = None
    # 改写的方法，通过打印节点的信息打印整个链表
    def __repr__(self):
        if self._head == None:
            return 'empty linked list'
        else:
            return '{}'.format(self._head._next)

    # 重写__iter__方法，方便for关键字调用打印值
    def __iter__(self):
        node = self._head._next
        while node:
            yield node.data
            node = node._next

if __name__ == "__main__":

    # 测试单链表
    l = SinglyLinkedList()
    for i in range(15):
        l.insert_value_to_head(i)
    print(l)
    node9 = l.find_by_value(9)
    l.insert_value_to_tail(77)
    node88 = Node(88)
    l.insert_node_to_tail(node88)
    print(l)
    l.insert_value_before_node(node9, 20)
    l.insert_value_before_node(node9, 16)
    l.insert_value_before_node(node9, 16)
    print(l)
    l.delete_by_value(16)
    print(l)
    node11 = l.find_by_index(3)
    l.delete_by_node(node11)
    print(l)
    node66 = Node(66)
    print(node66)
    node67 = l.find_by_index(0)
    print(l)
    l.insert_node_to_head(node66)
    print(l)
    l.delete_by_value(66)
    print(l)
    for value in l:
        print(value)