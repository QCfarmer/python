'''
改自原书代码 python/06_linkedlist/singly_linked_list.py
https://github.com/wangzheng0822/algo/blob/b2c1228ff915287ad7ebeae4355fa26854ea1557/python/06_linkedlist/singly_linked_list.py
为理解给原书代码添加了注释和部分打印消息
循环链表的实现
改写了find方法，返回为bool，和单链表实现有亿点差别
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

class CLinkedList:
    '''
    循环链表
    '''
    def __init__(self) -> None:
        self._head = None

    def find_by_value(self, value: int) -> bool:
        p = self._head
        while p._next != self._head and p.data != value:
            p = p._next
        if p._next == self._head and p.data != value:
            print('no such node')
            return False
        else:
            return True

    def find_by_node(self, node: Node) -> bool:
        return self.find_by_value(node.data)

    # 循环链表不知道按索引查找是否还有意义
    def find_by_index(self, index: int) -> bool:
        p = self._head
        position = 0
        while p._next != self._head and position != index:
            p = p._next
            position += 1
        if position < index:
            print('index out of range')
            return False
        else:
            print('{}->{}'.format(p.data,p._next.data))
            return True
    
    def insert_value_to_head(self, value: int):
        new_node = Node(value)
        self.insert_node_to_head(new_node)

    def insert_node_to_head(self, new_node: Node):
        if new_node:
            if self._head == None:
                self._head = new_node
                new_node._next = new_node
            else:
                new_node._next = self._head
                p = self._head
                while p._next != self._head:
                    p = p._next
                p._next = new_node
                self._head = new_node
        else:
            print('empty node')
    
    def insert_value_to_tail(self,value:int):
        self.insert_value_to_head(value)
        self._head = self._head._next
    
    def insert_node_to_tail(self,new_node:Node):
        self.insert_node_to_head(new_node)
        self._head = self._head._next

    def insert_value_after_node(self, node: Node, value: int):
        new_node = Node(value)
        self.insert_node_after_node(node,new_node)

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
        if not self._head or not node or not new_node: #空链表
            print('empty linked list or node or new_node')
            return
        elif self._head.data == node.data: #该节点为头节点
            self.insert_node_to_head(new_node)
            return
        else:
            current = self._head
            while current._next != self._head and current._next.data != node.data: #在尾节点之前寻找该节点
                current = current._next
            if current._next == self._head and current.data != node.data: #没有找到该节点
                print('no such node')
                return
            else:
                new_node._next = current._next #大坑，不能写成new_node._next = node，如果写了会指向None也就是node._next，那么链表就断了
                current._next = new_node

    def delete_by_node(self, node: Node):
        value = node.data
        self.delete_by_value(value)

    def delete_by_value(self, value: int):
        if not self._head or value == None: #空链表或删除的值为空
            # 大坑，不能写成 not value，如果value=0,那么not value就会进入下面的选择，实际数字0是有意义的
            print('empty linked list or value')
            return
        else:            
            fake_head = Node('fake')
            fake_head._next = self._head
            prev, current = fake_head, self._head
            while current._next != self._head: #当前值不为尾节点
                if current.data != value:
                    prev._next = current
                    prev = prev._next
                current = current._next

            # 其实下面的判断条件是经验得来的，主要为了应对value是尾节点的data的情况，手写了好几个过程，才确认这个条件，如果按照单链表的条件去推循环链表的：
            # if prev._next:
            #     prev._next = None
            # 就会发现差得离谱

            if current.data != value: 
                prev._next = current
            else:
                current = prev
            self._head = fake_head._next #该值正好是头节点
            current._next = self._head

    def __repr__(self):
        if self._head == None:
            return 'empty linked list'
        else:
            nums = []
            current = self._head
            nums.append(self._head.data)
            while current._next != self._head:
                current = current._next
                nums.append(current.data)
            nums.append(self._head.data)
            return "->".join(str(num) for num in nums)

    def __iter__(self):
        # 感觉这个函数写得不是很好
        # iter和next的用法还没彻底理解
        node = self._head
        yield node.data
        while node._next != self._head:
            node = node._next
            yield node.data

if __name__ == "__main__":

    # 测试单链表
    l = CLinkedList()
    print(l)
    for i in range(15):
        l.insert_value_to_head(i)
    print(l)
    node9 = l.find_by_value(9)
    print(node9)
    l.insert_value_to_tail(77)
    node88 = Node(88)
    l.insert_node_to_tail(node88)
    print(l)
    node10 = Node(10)
    l.insert_value_before_node(node10, 20)
    print(l)
    l.insert_value_before_node(node10, 16)
    print(l)
    l.insert_value_before_node(node10, 16)
    print(l)
    l.delete_by_value(16)
    print(l)
    node11 = Node(11)
    l.delete_by_node(node11)
    print(node11)
    print(l)
    node66 = Node(66)
    l.delete_by_node(Node(14))
    print(l)
    l.insert_node_to_head(node66)
    print(l)
    l.delete_by_value(66)
    print(l)
    l.delete_by_value(0)
    print(l)
    for value in l:
        print(value)
