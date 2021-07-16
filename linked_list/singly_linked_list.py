'''
改自原书代码 python/06_linkedlist/singly_linked_list.py
https://github.com/wangzheng0822/algo/blob/b2c1228ff915287ad7ebeae4355fa26854ea1557/python/06_linkedlist/singly_linked_list.py
为理解给原书代码添加了注释和部分打印消息
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
    '''
    def __init__(self):
        self._head = None

    def find_by_value(self, value: int) -> Node:
        p = self._head
        while p != None and p.data != value:
            p = p._next
        return p
    
    # 有按值查找，也应有按节点查找
    # 用找节点的值的方法
    def find_by_node(self,node:Node):
        return self.find_by_value(node.data)

    def find_by_index(self, index: int) -> Node:
        p = self._head
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
            new_node._next = self._head
            self._head = new_node
        else:
            print('empty node')
            
    # 既然有从头插入，理应也有尾插
    def insert_value_to_tail(self,value:int):
        new_node = Node(value)
        self.insert_node_to_tail(new_node)

    def insert_node_to_tail(self,new_node:Node):
        if not new_node:
            return
        elif self._head == None: #空链表
            self.insert_node_to_head(new_node)
        else:
            p = self._head
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
        if not self._head or not node or not new_node: #空链表
            print('empty linked list or node or new_node')
            return
        elif self._head == node: #该节点为头节点
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
                new_node._next = node
                current._next = new_node
    
    #原书代码
    # def delete_by_node(self, node: Node):
    #     if not self._head or not node:#空链表
    #         print('empty linked list or empty node')
    #         return
    #     elif node._next: #要删除的节点不是尾节点
    #         #将要删除的节点直接修改为下一节点，即改变了当前位置的数据
    #         node.data = node._next.data
    #         node._next = node._next._next
    #         return
    #     else:
    #         current = self._head
    #         while current and current._next != node:
    #             current = current._next
    #         if not current: #遍历完整个链表没有找到该节点current=None
    #             print('no such node')
    #             return
    #         else:
    #             current._next = node._next

    # 重写一个删除节点的方法，参照插入值的方法，用删除值实现
    def delete_by_node(self, node: Node):
        value = node.data
        self.delete_by_value(value)

    def delete_by_value(self, value: int): #删除所有为该值的节点，不会显示链表中是否存在该值
        if not self._head or value == None: #空链表或删除的值为空
            # 大坑，不能写成 not value，如果value=0,那么not value就会进入下面的选择，实际数字0是有意义的
            print('empty linked list or value')
            return
        else:
            # 原书代码
            # 假定节点的值都为int
            # fake_head = Node(value + 1)
            
            fake_head = Node('fake')
            
            fake_head._next = self._head
            prev, current = fake_head, self._head
            while current: #当前值不为空，即尾节点得next
                if current.data != value:
                    prev._next = current
                    prev = prev._next
                current = current._next
            if prev._next:
                
                # 原书代码
                # prev._next = None
                #实际上这里的current就是等于None，因为上面的while就是在current=None的时候停止的，但后面写循环链表的时候发现这里写current好些

                prev._next = current
            self._head = fake_head._next #该值正好是头节点
    
    def __add__(self,another):
        '''
        合并链表
        '''
        new = SinglyLinkedList()
        for i in self:
            new.insert_node_to_tail(Node(i))
        for i in another:
            new.insert_node_to_tail(Node(i))
        return new

    # 原书代码
    # 通过复制链表节点的值实现打印
    # def __repr__(self) -> str:
    #     nums = []
    #     current = self._head
    #     while current:
    #         nums.append(current.data)
    #         current = current._next
    #     return "->".join(str(num) for num in nums)
    
    # 改写的方法，通过打印节点的信息打印整个链表
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
            
    # 原书代码
    # 感觉用不到
    # def print_all(self):
    #     current = self._head
    #     if current:
    #         print(f"{current.data}", end="")
    #         current = current._next
    #     while current:
    #         print(f"->{current.data}", end="")
    #         current = current._next
    #     print("\n", flush=True)

def reverse_linked_list(linked_list):
    '''
    反转单链表
    '''
    if linked_list._head == None:#原链表为空
        return 'empty linked list'
    elif linked_list._head._next == None:#原链表仅有一个节点
        return linked_list
    else:
        rev = None
        prev = None
        new = SinglyLinkedList()
        p = linked_list._head
        while p._next != None:
            rev = prev
            prev = p
            p = p._next
            prev._next = rev
        p._next = prev
        new._head = p
        linked_list._head = p
        return linked_list

def middle_node(linked_list:SinglyLinkedList) -> Node:
    '''
    实现求链表的中间结点
    '''
    if linked_list._head == None:
        print('empty linked list')
        return
    elif linked_list._head._next == None: #只有一个节点
        return linked_list._head
    else:
        slow_p = linked_list._head
        fast_p = linked_list._head
        while fast_p._next != None and fast_p._next._next != None:
            slow_p = slow_p._next
            fast_p = fast_p._next._next
        # 偶数时取前一个
        return slow_p
        # 偶数时取后一个
        # return slow_p._next

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
    print(node11)
    print(l)
    l.delete_by_value(88)
    print(l)
    node66 = Node(66)
    print(node66)
    node67 = l.find_by_index(0)
    l.delete_by_node(node67)
    print(l)
    l.insert_node_to_head(node66)
    print(l)
    l.delete_by_value(66)
    print(l)
    for value in l:
        print(value)

    k = reverse_linked_list(l)
    print(k)
    # 测试原链表是否反转
    print(l)

    m = l + k
    print(m)

    print(middle_node(m))
