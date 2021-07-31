'''
实现一个二叉查找树，并且支持插入、删除、查找操作
实现查找二叉查找树中某个节点的后继、前驱节点
实现二叉树前、中、后序以及按层遍历
'''

class TNode():
    '''
    树节点
    '''
    def __init__(self,data):
        self.data = data
        self._left = None
        self._right = None

class BinarySearchTree:
    '''
    无重复数据的二叉树
    '''
    def __init__(self):
        self.root = None
    
    def find(self,data):
        if self.root is None:
            return
        p = self.root
        while p is not None:
            if data > p.data:
                p = p._right
            elif data < p.data:
                p = p._left
            else:
                return p
        return False

    def insert(self,data):
        if self.root is None:
            self.root = TNode(data)
            return
        p = self.root
        while p is not None:
            if data > p.data:
                if p._right is None:
                    p._right = TNode(data)
                    return
                p = p._right
            else:
                if p._left is None:
                    p._left = TNode(data)
                    return
                p = p._left

    def delete(self,data):
        if self.root is None:
            return
        p = self.root
        fp = None
        while p is not None and p.data != data: #没到叶节点。要把p is not none写在前面！！！
            fp = p
            # print(p.data)
            if data > p.data:
                p = p._right
            else:
                p = p._left
        if p is None: #没找到
            return
        # 有两个子节点，找后继节点
        if p._left is not None and p._right is not None:
            minP = p._right
            minFP = p
            while minP._left is not None:
                minFP = minP
                minP = minP._left
            p.data = minP.data
            p = minP
            fp = minFP
        # 是叶子节点或者仅有一个子节点
        if p._left is not None:
            child = p._left
        elif p._right is not None:
            child = p._right
        else:
            child = None
        # 根节点
        if fp is None:
            self.root = child
        elif fp._left == p:
            fp._left = child
        else:
            fp._right = child
    
    def find_max(self):
        if self.root is None:
            return
        else:
            p = self.root
            while p._right is not None:
                p = p._right
            return p.data

    def find_min(self):
        if self.root is None:
            return
        else:
            p = self.root
            while p._left is not None:
                p = p._left
            return p.data
    
def prev(node:TNode):
    '''
    前驱节点
    '''
    if node is None or node is False:
        print('wrong node')
        return
    p = node
    if p._left is not None:
        p = p._left
        while p._right is not None:
            p = p._right
        print('prev data:',p.data)
        return p
    else:
        print('prev data:',None)
        return
    
def next(node:TNode):
    '''
    后继节点
    '''
    if node is None or node is False:
        print('wrong node')
        return
    p = node
    if p._right is not None:
        p = p._right
        while p._left is not None:
            p = p._left
        print('next data:',p.data)
        return p
    else:
        print('next data:',None)
        return

def ldr(tree:BinarySearchTree):
    '''
    中序遍历
    '''
    if tree.root is None:
        return
    p = tree.root
    def ldr_node(root:TNode):
        if root is None:
                return
        ldr_node(root._left)
        print(root.data,end=' ')
        ldr_node(root._right)
    ldr_node(p)
    print('\n')

def dlr(tree:BinarySearchTree):
    '''
    前序遍历
    '''
    if tree.root is None:
        return
    p = tree.root
    def dlr_node(root:TNode):
        if root is None:
                return
        print(root.data,end=' ')
        dlr_node(root._left)
        dlr_node(root._right)
    dlr_node(p)
    print('\n')

def lrd(tree:BinarySearchTree):
    '''
    后序遍历
    '''
    if tree.root is None:
        return
    p = tree.root
    def lrd_node(root:TNode):
        if root is None:
                return
        lrd_node(root._left)
        lrd_node(root._right)
        print(root.data,end=' ')
    lrd_node(p)
    print('\n')

def level_order(tree:BinarySearchTree):
    '''
    层遍历
    '''
    if tree.root is None:
        return
    level_queue = []
    p = tree.root
    level_queue.append(p)
    i = 0
    while len(level_queue) != 0:
        if level_queue[0]._left is not None:
            level_queue.append(level_queue[0]._left)
        if level_queue[0]._right is not None:
            level_queue.append(level_queue[0]._right)
        print(level_queue.pop(0).data,end=' ')
    print('\n')

if __name__ == "__main__":
    a = BinarySearchTree()
    ldr(a)
    a.insert(3)
    a.insert(1)
    a.insert(5)
    a.insert(2)
    a.insert(4)
    a.insert(6)
    a.insert(0)
    print('-------中序遍历-------')
    ldr(a)
    print('-------前序遍历-------')
    dlr(a)
    print('-------后序遍历-------')
    lrd(a)
    print('-------层遍历-------')
    level_order(a)
    a.delete(6)
    a.delete(7)
    a.delete(0)
    a.delete(3)
    a.delete(1)
    ldr(a)
    a.insert(8)
    ldr(a)
    a.insert(7)
    ldr(a)
    print(a.find_max())
    print(a.find_min())
    b = a.find(1)
    prev(b)
    next(b)
    c = a.find(4)
    prev(c)
    d = next(c)
    prev(d)
    next(d)
