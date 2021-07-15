class Node:
    def __init__(self, data, next_node=None):
        self.data = data
        self._next = next_node
    def __repr__(self):
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
        # !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
        if new_node:
            # 原书代码       
            # new_node._next = self._head
            # self._head = new_node

            # 通过复制插入名称重复的节点
            copy_node = Node(new_node.data)
            copy_node._next = self._head
            self._head = copy_node
        else:
            print('empty node')

    def insert_value_to_tail(self,value:int):
        new_node = Node(value)
        self.insert_node_to_tail(new_node)

    def insert_node_to_tail(self,new_node:Node):
        if not new_node:
            return
        else:
            p = self._head
            while p._next != None:
                p = p._next
            # 原书代码
            # p._next = new_node

            #通过复制插入名称重复的节点
            copy_node = Node(new_node.data)
            p._next = copy_node

    def insert_value_after_node(self, node: Node, value: int):
        new_node = Node(value)
        self.insert_node_after_node(node, new_node)

    def insert_node_after_node(self, node: Node, new_node: Node):
        # !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
        if not node or not new_node:
            return
        else:
            # 原书代码
            # new_node._next = node._next
            # node._next = new_node

            #通过复制插入名称重复的节点
            copy_node = Node(new_node.data)
            copy_node._next = node._next
            node._next = copy_node

    def insert_value_before_node(self, node: Node, value: int):
        new_node = Node(value)
        self.insert_node_before_node(node, new_node)

    def insert_node_before_node(self, node: Node, new_node: Node):
        # !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
        if not self._head or not node or not new_node:#空链表
            print('empty linked list or')
            return
        elif self._head == node:#该节点为头节点
            self.insert_node_to_head(new_node)
            return
        else:
            current = self._head
            while current._next and current._next != node:#在尾节点之前寻找该节点
                current = current._next
            if not current._next:  #没有找到该节点
                print('no such node')
                return
            else:
                # 原书代码
                # new_node._next = node
                # current._next = new_node

                # 通过复制插入名称重复的节点
                copy_node = Node(new_node.data)
                copy_node._next = node
                current._next = copy_node
    
    #原书代码
    # def delete_by_node(self, node: Node):
    #     # !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
    #     if not self._head or not node:#空链表
    #         print('empty linked list')
    #         return
    #     elif node._next:#要删除的节点不是尾节点
    #         #将要删除的节点直接修改为下一节点，即改变了当前位置的数据
    #         node.data = node._next.data
    #         node._next = node._next._next
    #         return
    #     else:
    #         current = self._head
    #         # !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
    #         while current and current._next != node:
    #             current = current._next
    #         if not current:#遍历完整个链表没有找到该节点current=None
    #             print('no such node')
    #             return
    #         else:
    #             current._next = node._next

    def delete_by_node(self, node: Node):
        value = node.data
        self.delete_by_value(value)

    def delete_by_value(self, value: int):#删除所有为该值的节点，不会显示链表中是否存在该值
        if not self._head or not value:#空链表或删除的值为空
            print('empty linked list or value')
            return
        else:
            fake_head = Node(value + 1)
            fake_head._next = self._head
            prev, current = fake_head, self._head
            while current:#当前值不为尾节点
                if current.data != value:
                    prev._next = current
                    prev = prev._next
                current = current._next
            if prev._next:
                prev._next = None
            self._head = fake_head._next#该值正好是头节点

    # def __repr__(self) -> str:
    #     nums = []
    #     current = self._head
    #     while current:
    #         nums.append(current.data)
    #         current = current._next
    #     return "->".join(str(num) for num in nums)
    
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

    # def print_all(self):
    #     current = self._head
    #     if current:
    #         print(f"{current.data}", end="")
    #         current = current._next
    #     while current:
    #         print(f"->{current.data}", end="")
    #         current = current._next
    #     print("\n", flush=True)

if __name__ == "__main__":
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
    node66 = Node(66)
    print(node66)
    node67 = l.find_by_index(0)
    l.insert_node_before_node(node67,node66)
    l.insert_node_before_node(node67,node66)
    l.insert_node_to_head(node66)
    print(l)
    l.insert_node_to_head(node66)
    print(l)
    l.delete_by_value(66)
    print(l)
    for value in l:
        print(value)