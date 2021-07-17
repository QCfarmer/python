# 把singly_linked_list的代码复制过来
from abc import ABC


class Node:
    def __init__(self, data, next_node=None):
        self.data = data
        self._next = next_node
    def __repr__(self): #为实现打印链表，重写了节点的打印方法
        if self._next == None:
            return '{}'.format(self.data)
        else:
            return '{}->{}'.format(self.data,self._next)

class ArrayQueue:
    '''
    数组实现的顺序队列
    '''
    def __init__(self,n):
        self._head = 0
        self._tail = 0
        self._n = n
        self._items = [None] * n

    def enqueue(self,value):
        if self._tail == self._n: #队尾没有空间
            if self._head == 0: #队列已满
                print('full, can not enqueue')
                return False
            else:
                for i in range(self._head,self._tail):
                    self._items[i-self._head] = self._items[i]
                self._tail -= self._head
                self._head = 0
        self._items[self._tail] = value
        self._tail += 1
        return True
    
    def dequeue(self):
        if self._head == self._tail: #队列为空
            print('empty queue')
            return False
        else:
            ret = self._items[self._head]
            self._head += 1
            return ret
    
    def __repr__(self):
        if self._head == self._tail: #队列为空
            return 'empty queue'
        else:
            return '{}'.format(self._items[self._head:self._tail])

class LinkedQueue:
    '''
    链表实现的链式队列
    '''
    def __init__(self) -> None:
        self._head = None
        self._tail = None
    
    def enqueue(self,value):
        new_node = Node(value)
        if self._tail == None: #空队列
            self._head = new_node
            self._tail = new_node
        else:
            self._tail._next = new_node
            self._tail = new_node

    def dequeue(self):
        if self._tail == None: #空队列
            print('empty, can not dequeue')
            return False
        elif self._head == self._tail and self._tail != None: #只有一个节点
            ret = self._head
            self._head = None
            self._tail = None
            return ret.data
        else:
            ret = self._head
            self._head = self._head._next
            return ret.data
    
    def __repr__(self):
        if self._head == None:
            return 'empty queue'
        else:
            return '{}'.format(self._head)

class CircularlyQueue:
    '''
    数组实现的循环队列
    '''
    def __init__(self,n):
        self._head = 0
        self._tail = 0
        self._n = n
        self._items = [None] * n
    
    def enqueue(self,value):
        if (self._tail + 1) % self._n == self._head:
            print('full, can not enqueue')
            return False
        else:
            self._items[self._tail] = value
            self._tail = (self._tail + 1) % self._n
            return True
    
    def dequeue(self):
        if self._head == self._tail:
            print('empty, can not dequeue')
            return False
        else:
            ret = self._items[self._head]
            self._head = (self._head + 1) % self._n
            return ret

    def __repr__(self):
        if self._head == self._tail: #队列为空
            return 'empty queue'
        elif self._head < self._tail:
            return '{}'.format(self._items[self._head:self._tail])
        elif self._tail == 0:
            return '{}'.format(self._items[self._head:])
        else:
            return '{}'.format(self._items[self._head:] + self._items[:self._tail+1])

if __name__ == '__main__':
    print('-------------test array queue------------------')
    a = ArrayQueue(5)
    a.enqueue(0)
    a.enqueue(1)
    a.enqueue(2)
    print(a)
    a.enqueue(3)
    a.enqueue(4)
    print(a)
    a.enqueue(5)
    print(a)
    a.dequeue()
    a.dequeue()
    print(a)
    a.enqueue(6)
    print(a)
    a.dequeue()
    print(a)
    print(a.dequeue())
    a.dequeue()
    print(a)
    a.dequeue()
    print(a)

    print('-------------test linked queue------------------')
    b = LinkedQueue()
    b.enqueue('a')
    print(b)
    b.enqueue('b')
    b.enqueue('c')
    b.enqueue('d')
    print(b)
    b.dequeue()
    print(b)
    print(b.dequeue())
    b.dequeue()
    print(b)
    b.dequeue()
    print(b)

    print('-------------test circular queue------------------')
    c = CircularlyQueue(5)
    c.enqueue(0)
    c.enqueue(1)
    c.enqueue(2)
    print(c)
    c.enqueue(3)
    print(c)
    c.enqueue(4)
    print(c)
    c.enqueue(5)
    print(c)
    c.dequeue()
    c.dequeue()
    print(c)
    c.enqueue(6)
    print(c)
    c.dequeue()
    print(c.dequeue())
    c.dequeue()
    print(c)
    c.dequeue()
    print(c)
