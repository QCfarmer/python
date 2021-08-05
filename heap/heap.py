'''
实现一个小顶堆、大顶堆、优先级队列
实现堆排序
未实现：利用优先级队列合并K个有序数组
实现求静态数组的最大Top K（动态数组最大top k，如果要实现同时更新数组和top k，要写个类，懒，就不写了）
'''

class BigHeap:
    '''
    大顶堆
    无重复元素
    支持动态扩容
    便于测试把默认容量写成5
    '''
    def __init__(self,capacity=5):
        self.n = capacity
        self.count = 0
        self.array = [None] * (capacity+1)
    
    def _resize(self):
        new = [None] * (self.n*2 + 1)
        new[:self.n+1] = self.array[:]
        self.array = new
        self.n = self.n * 2
        return
    
    def insert(self,data):
        if self.count >= self.n: #堆满了
            self._resize()
        self.count += 1
        self.array[self.count] = data
        i = self.count
        self._heapify_up(i)
        return
    
    def remove_max(self):
        if self.count == 0: #堆中没有数据
            return
        else:
            self.array[1] = self.array[self.count]
            self.count -= 1
            self._heapify_down(1)
    
    def _heapify_up(self,i):
        '''
        自下而上堆化
        '''
        while i//2 > 0 and self.array[i] > self.array[i//2]: #自下而上的堆化
                self.array[i],self.array[i//2] = self.array[i//2],self.array[i]
                i = i//2
    
    def _heapify_down(self,i):
        '''
        自上而下堆化
        '''
        while True:
            maxPos = i
            if i*2 <= self.count and self.array[i] < self.array[i*2]:
                maxPos = i*2
            if i*2+1 <= self.count and self.array[maxPos] < self.array[i*2+1]:
                maxPos = i*2+1
            if maxPos == i:
                break
            self.array[i],self.array[maxPos] = self.array[maxPos],self.array[i]
            i = maxPos
        
    def delete_by_index(self,index):
        if index <= 0 or index > self.count:
            print('wrong index')
            return
        delete_item = self.array[index]
        replace_item = self.array[self.count]
        self.array[index] = replace_item
        self.count -= 1
        if delete_item < replace_item:
            self._heapify_up(index)
        elif delete_item > replace_item:
            self._heapify_down(index)
        else:
            pass
        return delete_item
        
    def max(self):
        return self.array[1]
    
    def delete_by_value(self,value):
        if value > self.array[1]: #比堆顶大
            return
        elif value == self.array[1]: #恰好是堆顶
            self.remove_max()
            return
        else:
            for i in range(1,self.count+1):
                if value == self.array[i]:
                    self.delete_by_index(i)
                    return
    
    def __str__(self):
        return '{}'.format(self.array[:self.count+1])

class SmallHeap:
    '''
    小顶堆
    无重复元素
    为了实现top k，注释掉支持动态扩容的代码
    便于测试把默认容量写成5
    '''
    def __init__(self,capacity=5):
        if capacity <= 0:
            print('wrong capacity')
            return
        self.n = capacity
        self.count = 0
        self.array = [None] * (capacity+1)
    
    # def _resize(self):
    #     new = [None] * (self.n*2 + 1)
    #     new[:self.n+1] = self.array[:]
    #     self.array = new
    #     self.n = self.n * 2
    #     return
    
    def insert(self,data):
        if self.count >= self.n: #堆满了
            # self._resize()
            return
        self.count += 1
        self.array[self.count] = data
        i = self.count
        self._heapify_up(i)
        return
    
    def remove_min(self):
        if self.count == 0: #堆中没有数据
            return
        else:
            self.array[1] = self.array[self.count]
            self.count -= 1
            self._heapify_down(1)
    
    def _heapify_up(self,i):
        '''
        自下而上堆化
        '''
        while i//2 > 0 and self.array[i] < self.array[i//2]: #自下而上的堆化
                self.array[i],self.array[i//2] = self.array[i//2],self.array[i]
                i = i//2
    
    def _heapify_down(self,i):
        '''
        自上而下堆化
        '''
        while True:
            minPos = i
            if i*2 <= self.count and self.array[i] > self.array[i*2]:
                minPos = i*2
            if i*2+1 <= self.count and self.array[minPos] > self.array[i*2+1]:
                minPos = i*2+1
            if minPos == i:
                break
            self.array[i],self.array[minPos] = self.array[minPos],self.array[i]
            i = minPos
        
    def delete_by_index(self,index):
        if index <= 0 or index > self.count:
            print('wrong index')
            return
        delete_item = self.array[index]
        replace_item = self.array[self.count]
        self.array[index] = replace_item
        self.count -= 1
        if delete_item > replace_item:
            self._heapify_up(index)
        elif delete_item < replace_item:
            self._heapify_down(index)
        else:
            pass
        return delete_item
        
    def min(self):
        return self.array[1]
    
    def delete_by_value(self,value):
        if value < self.array[1]: #比堆顶小
            return
        elif value == self.array[1]: #恰好是堆顶
            self.remove_min()
            return
        else:
            for i in range(1,self.count+1):
                if value == self.array[i]:
                    self.delete_by_index(i)
                    return
    
    def __str__(self):
        return '{}'.format(self.array[:self.count+1])

# 大顶堆从小到大排序
def heapify_big_down(array:list,n:int,i:int):
    while True:
        maxPos = i
        if i*2 <= n and array[i] < array[i*2]:
            maxPos = i*2
        if i*2+1 <= n and array[maxPos] < array[i*2+1]:
            maxPos = i*2+1
        if maxPos == i:
            break
        array[i],array[maxPos] = array[maxPos],array[i]
        i = maxPos

def build_big_heap(alist:list):
    n = len(alist) - 1
    for i in range(n//2,0,-1):
        heapify_big_down(alist,n,i)

def sort_small_big(alist:list):
    '''
    从小到大排序
    '''
    build_big_heap(alist)
    k = len(alist) - 1
    while k>1:
        alist[1],alist[k] = alist[k],alist[1]
        k -= 1
        heapify_big_down(alist,k,1)

# 小顶堆从大到小排序
def heapify_small_down(array:list,n:int,i:int):
    while True:
        minPos = i
        if i*2 <= n and array[i] > array[i*2]:
            minPos = i*2
        if i*2+1 <= n and array[minPos] > array[i*2+1]:
            minPos = i*2+1
        if minPos == i:
            break
        array[i],array[minPos] = array[minPos],array[i]
        i = minPos

def build_small_heap(alist:list):
    n = len(alist) - 1
    for i in range(n//2,0,-1):
        heapify_small_down(alist,n,i)

def sort_big_small(alist:list):
    '''
    由大到小排序
    '''
    build_small_heap(alist)
    k = len(alist) - 1
    while k>1:
        alist[1],alist[k] = alist[k],alist[1]
        k -= 1
        heapify_small_down(alist,k,1)

def top_k(alist:list,k):
    '''
    静态数据top k
    '''
    if k <= 0:
        print('wrong capacity')
        return
    top = SmallHeap(k)
    for i in alist:
        if top.count < k:
            top.insert(i)
        elif top.count == k:
            min = top.min()
            if i > min:
                top.remove_min()
                top.insert(i)
            else:
                continue
    return top.array[1:]

if __name__ == "__main__":
    print('-----测试堆-----')
    # a = BigHeap()
    a = SmallHeap()
    print(a)
    a.insert(6)
    print(a)
    a.insert(7)
    a.insert(5)
    a.insert(4)
    print(a)
    a.insert(8)
    print(a)
    a.insert(9)
    print(a)
    a.insert(3)
    print(a)
    a.insert(2)
    a.insert(1)
    print(a)
    # print(a.max())
    print(a.min())
    # a.remove_max()
    a.remove_min()
    print(a)
    # print(a.max())
    print(a.min())
    # a.remove_max()
    a.remove_min()
    print(a)
    a.delete_by_index(0)
    print(a)
    a.delete_by_index(8)
    print(a)
    a.delete_by_index(7)
    print(a)
    a.delete_by_index(1)
    print(a)
    a.delete_by_index(3)
    print(a)
    a.delete_by_value(0)
    print(a)
    a.delete_by_value(4)
    print(a)
    a.delete_by_value(6)
    print(a)
    a.delete_by_value(1)
    print(a)

    print('----测试堆排序----')
    b = [None,6,8,3,0,1,7]
    sort_small_big(b)
    print(b)
    sort_big_small(b)
    print(b)

    print('-------测试top k-------')
    c = [6,8,3,0,1,7]
    print(top_k(c,7))
    print(top_k(c,6))
    print(top_k(c,5))
    print(top_k(c,4))
    print(top_k(c,3))
    print(top_k(c,2))
    print(top_k(c,1))
    print(top_k(c,0))
