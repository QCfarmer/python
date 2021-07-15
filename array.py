class MyArray:
    '''
    支持动态扩容的数组,
    初始大小为10
    '''
    def __init__(self,capacity=10):
        self.data = [None]*capacity
        self.capacity = capacity
    def __getitem__(self,i):
        return self.data[i]
    def __setitem__(self,i,number):
        self.data[i] = number
    def __len__(self):
        return len(self.data)
    def __iter__(self):
        for item in self.data:
            yield item

    # 按索引查找
    # 感觉没有存在必要
    # def find(self,i):
    #     return self.data[i]
    
    def delete(self,i):
        # for rest in range(i,len(self.data)-1):
        #     self.data[rest] = self.data[rest+1]
        # self.data.pop()
        return self.data.pop(i)
    def insert(self,i,number):
        # self.data.append(0)
        # for rest in range(len(self.data)-1,i,-1):
        #     self.data[rest] = self.data[rest-1]
        # self.data[i] = number
        while i >= len(self.data):
            new = MyArray(2*self.capacity)
            for n in range(len(self.data)):
                new.data[n] = self.data[n]
            self.data = new.data
            self.capacity = new.capacity
        else:
            self.data.insert(i,number)
    def __str__(self):
        return 'array: {}'.format(self.data)

class SortedArray(MyArray):
    '''
    大小固定的有序数组
    未解决：
    当面对不同类型的数据的时候如何排序
    '''
    def __init__(self, capacity=10):
        super().__init__(capacity)
    def __setitem__(self,i,number):
        #这个函数不确定还需不需要索引i
        super().__setitem__(i,number)
        self.data.sort()
    def insert(self,number):
        if float('inf') in self.data:
            self.data.pop()
            self.data.append(number)
            self.data.sort()
        else:
            raise IndexError
    def __add__(self,another):
        '''
        实现两个有序数组合并为一个有序数组
        '''
        newarray = SortedArray(self.capacity + another.capacity)
        newarray.data = [i for i in self.data] + [j for j in another.data]
        self.data = newarray.data
        self.data.sort()
        self.capacity = newarray.capacity

if __name__ == '__main__':
    a = MyArray()
    a = SortedArray()
    print(a[3])
    a[1] = 55
    print(a)
    a[3] = 1
    print(a)
    # print(len(a))
    # a.delete(4)
    a.insert(3)
    print(a)
    a.insert(6)
    print(a)
    a.insert(66)
    print(a)
    a.insert(43)
    print(a)
    a.insert(87)
    print(a)
    print('k' in a)
    b = SortedArray()
    b.insert(99)
    b.insert(100)
    b.insert(2333)
    print(b)
    a + b
    print(a)
    print(a.capacity)
    print(len(a))