class ArrayStack:
    '''
    数组实现的顺序栈
    '''
    def __init__(self,n):
        self.items = [None]*n
        self.count = 0
        self.n = n
    def push(self,item):
        if self.count == self.n:
            return False
        self.items[self.count] = item
        self.count += 1
        return True
    def pop(self):
        if self.count == 0:
            return False
        tmp = self.items[self.count-1]
        self.items[self.count-1] = None
        self.count -= 1
        return tmp
    def __str__(self):
        return str(self.items)

class ArrayStack2:
    '''
    支持动态扩容的数组实现的顺序栈
    '''
    def __init__(self):
        self.items = [None]*10
        self.count = 0
        self.n = 10
    def push(self,item):
        if  self.count < self.n:
            self.items[self.count] = item
            self.count += 1
            # return True
        else:
            print('expanse')
            new = [None]*(self.n*2)
            new[0:self.count] = self.items[:]
            new[self.count] = item
            self.items = new
            self.count += 1
            self.n = self.n * 2
    def pop(self):
        if self.count == 0:
            return False
        tmp = self.items[self.count-1]
        self.items[self.count-1] = None
        self.count -= 1
        return tmp
    def __str__(self):
        return str(self.items)

# 把singly_linked_list里面的代码复制过来
class Node:
    def __init__(self, data, next_node=None):
        self.data = data
        self._next = next_node
    def __repr__(self): #为实现打印链表，重写了节点的打印方法
        if self._next == None:
            return '{}'.format(self.data)
        else:
            return '{}->{}'.format(self.data,self._next)

class LinkedStack:
    '''
    用链表实现的栈
    '''
    def __init__(self):
        sentinel = Node(None)
        self._top = sentinel
    def push(self,value):
        new_node = Node(value)
        new_node._next = self._top
        self._top = new_node
    def pop(self):
        if self._top == None:
            print('empty linked stack can not pop')
        else:
            tmp = self._top.data
            self._top = self._top._next
            return tmp
    def __repr__(self):
        if self._top == None:
            return 'empty stack'
        else:
            return '{}'.format(self._top)
    
if __name__ == '__main__':
    a = ArrayStack2()
    print(a)
    a.push(1)
    print(a)
    a.push(2)
    a.push(3)
    a.push(4)
    a.push(5)
    a.push(6)
    a.push(7)
    a.push(8)
    a.push(9)
    a.push(10)
    a.push(11)
    print(a)
    print(a.pop())
    print(a.pop())
    print(a.pop())
    print(a.pop())
    print(a)
    print(a.pop())
    print(a.pop())
    print(a.pop())
    print(a)
    print(a.pop())
    print(a.pop())
    print(a.pop())
    print(a.pop())
    print(a)
    print(a.pop())
    print(a)

    b = LinkedStack()
    b.push('a')
    b.push('b')
    b.push('c')
    print(b)
    b.pop()
    print(b)
    print(b.pop())
    print(b)
    b.pop()
    print(b)
