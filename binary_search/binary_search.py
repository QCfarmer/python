'''
实现一个有序数组的二分查找算法
实现模糊二分查找算法（比如大于等于给定值的第一个元素）
小节思考题：如果有序数组是一个循环有序数组，如何查找值等于给定值的元素？
'''

def binary_search(alist,value):
    '''
    二分查找
    非递归实现
    '''
    if len(alist) < 1:
        # print('empty list')
        return
    else:
        low = 0
        high = len(alist) - 1
        while low <= high:
            mid = low + (high - low) // 2
            if alist[mid] == value:
                return mid
            elif alist[mid] > value:
                high = mid - 1
            else:
                low = mid + 1
        if alist[mid] != value:
            return False

def binary_search_2(alist,value):
    '''
    二分查找
    递归实现
    自己写的，很复杂，判断条件多了复杂度会增加
    '''
    if len(alist) < 1:
        return
    elif len(alist) == 1:
        if alist[0] == value:
            return 0
        else:
            return False
    else:
        low = 0
        high = len(alist) - 1
        mid = low + (high - low) // 2
        if alist[mid] == value:
            return mid
        elif alist[mid] > value:
            res = binary_search_2(alist[low:mid],value)
            if res is False: #大坑，0 == False 结果为True，必须要用0 is False
                return False
            else:
                return res
        else:
            res = binary_search_2(alist[mid+1:],value)
            if res is False:
                return False
            else:
                return res + mid + 1

def bsearch(alist,low,high,value):
    '''
    二分查找内部函数
    书上的写法
    '''
    if low > high:
        return False
    mid = low + (high-low) // 2
    if alist[mid] == value:
        return mid
    elif alist[mid] > value:
        return bsearch(alist,low,mid-1,value)
    else:
        return bsearch(alist,mid+1,high,value)

def binary_search_3(alist,value):
    '''
    二分查找
    递归实现
    书上的写法
    '''
    if len(alist) == 0: #自己加了个空数组返回None，不加的话会返回False
        return
    else:
        return bsearch(alist,0,len(alist)-1,value)

# def binary_search_re(alist,value):
#     '''
#     二分查找第一个等于给定值的元素
#     数组中包含重复元素
#     自己写的
#     '''
#     if len(alist) < 1:
#         return
#     else:
#         low = 0
#         high = len(alist) - 1
#         while low < high:
#             mid = low + (high - low) // 2
#             if alist[mid] >= value:
#                 high = mid
#             else:
#                 low = mid + 1
#         mid = low + (high - low) // 2
#         if alist[mid] != value:
#             return False
#         else:
#             return mid

# def binary_search_re(alist,value):
#     '''
#     二分查找第一个等于给定值的元素
#     数组中包含重复元素
#     书上较难理解的写法
#     '''
#     if len(alist) < 1:
#         return
#     else:
#         low = 0
#         high = len(alist) - 1
#         while low <= high:
#             mid = low + (high - low) // 2
#             if alist[mid] >= value:
#                 high = mid - 1
#             else:
#                 low = mid + 1
#         if low < len(alist) and alist[low] == value:
#             return low
#         else:
#             return False

def binary_search_re(alist,value):
    '''
    二分查找第一个等于给定值的元素
    数组中包含重复元素
    书上另一种比较好理解的写法
    '''
    if len(alist) < 1:
        return
    else:
        low = 0
        high = len(alist) - 1
        while low <= high:
            mid = low + (high - low) // 2
            if alist[mid] > value:
                high = mid - 1
            elif alist[mid] < value:
                low = mid + 1
            else:
                if mid == 0 or alist[mid-1] != value:
                    return mid
                else:
                    high = mid - 1
        return False

def binary_search_re_2(alist,value):
    '''
    二分查找最后一个等于给定值的元素
    数组中包含重复元素
    书上的写法
    '''
    if len(alist) < 1:
        return
    else:
        low = 0
        high = len(alist) - 1
        while low <= high:
            mid = low + (high - low) // 2
            if alist[mid] > value:
                high = mid - 1
            elif alist[mid] < value:
                low = mid + 1
            else:
                if mid == len(alist)-1 or alist[mid+1] != value:
                    return mid
                else:
                    low = mid + 1
        return False
    
def binary_search_re_3(alist,value):
    '''
    二分查找第一个大于等于给定值的元素
    数组中包含重复元素
    书上的写法
    '''
    if len(alist) < 1:
        return
    else:
        low = 0
        high = len(alist) - 1
        while low <= high:
            mid = low + (high - low) // 2
            if alist[mid] >= value:
                if mid == 0 or alist[mid-1] < value:
                    return mid
                else:
                    high = mid - 1
            else:
                low = mid + 1
        return False

def binary_search_re_4(alist,value):
    '''
    二分查找最后一个小于等于给定值的元素
    数组中包含重复元素
    书上的写法
    '''
    if len(alist) < 1:
        return
    else:
        low = 0
        high = len(alist) - 1
        while low <= high:
            mid = low + (high - low) // 2
            if alist[mid] <= value:
                if mid == len(alist) or alist[mid+1] > value:
                    return mid
                else:
                    low = mid + 1
            else:
                high = mid - 1
        return False

# 思考题
def binary_search_cir(alist,value):
    '''
    二分查找第一个等于给定值的元素
    循环有序数组
    数组中不包含重复元素
    书上的答案
    '''
    if len(alist) < 1:
        return
    else:
        low = 0
        high = len(alist) - 1
        while low <= high:
            mid = low + (high-low) // 2
            if alist[mid] == value:
                return mid
            elif alist[low] > alist[mid]: #右边有序
                if alist[mid] < value and value <= alist[high]:
                    low = mid + 1
                else:
                    high = mid - 1
            else: #左边有序
                if alist[low] <= value and value < alist[mid]:
                    high = mid - 1
                else:
                    low = mid + 1
        return False

def binary_search_re_cir(alist,value):
    '''
    二分查找第一个等于给定值的元素
    循环有序数组
    数组中包含重复元素
    根据书上的答案改写
    '''
    if len(alist) < 1:
        return
    else:
        low = 0
        high = len(alist) - 1
        while low <= high:
            mid = low + (high-low) // 2
            if alist[mid] == value:
                if mid == 0 or alist[mid-1] != value:
                    return mid
                else:
                    high = mid - 1
            elif alist[low] > alist[mid] and alist[mid] != value: #右边有序
                if alist[mid] < value and value <= alist[high]:
                    low = mid + 1
                else:
                    high = mid - 1
            else: #左边有序
                if value < alist[mid] and alist[low] <= value:
                    high = mid - 1
                else:
                    low = mid + 1
        return False

if __name__ == '__main__':
    a = []
    b = [1]
    c = [0,1,1,1,2,2,2,3,3,3,3,4,5]
    d = [-2,-1,0,4,6,8,11]
    e = [4,5,6,7,1,2,3]
    f = [4,5,5,6,6,6,7,1,1,1,2,3,3]

    # print('------测试二分查找非递归实现-----')
    # print(binary_search(a,7))
    # print(binary_search(b,1))
    # print(binary_search(b,7))
    # print(binary_search(d,-2))
    # print(binary_search(d,-1))
    # print(binary_search(d,0))
    # print(binary_search(d,4))
    # print(binary_search(d,6))
    # print(binary_search(d,8))
    # print(binary_search(d,11))
    # print(binary_search(d,12))

    # print('------测试二分查找自己写的递归实现-----')
    # print(binary_search_2(a,7))
    # print(binary_search_2(b,1))
    # print(binary_search_2(b,7))
    # print(binary_search_2(d,-2))
    # print(binary_search_2(d,-1))
    # print(binary_search_2(d,0))
    # print(binary_search_2(d,4))
    # print(binary_search_2(d,6))
    # print(binary_search_2(d,8))
    # print(binary_search_2(d,11))
    # print(binary_search_2(d,12))

    # print('------测试二分查找的递归实现-----')
    # print(binary_search_3(a,7))
    # print(binary_search_3(b,1))
    # print(binary_search_3(b,7))
    # print(binary_search_3(d,-2))
    # print(binary_search_3(d,-1))
    # print(binary_search_3(d,0))
    # print(binary_search_3(d,4))
    # print(binary_search_3(d,6))
    # print(binary_search_3(d,8))
    # print(binary_search_3(d,11))
    # print(binary_search_3(d,12))
    
    # print('------测试二分查找第一个值等于给定值的含重复元素的数组-----')
    # print(binary_search_re(a,7))
    # print(binary_search_re(b,1))
    # print(binary_search_re(b,7))
    # print(binary_search_re(d,-2))
    # print(binary_search_re(d,-1))
    # print(binary_search_re(d,0))
    # print(binary_search_re(d,4))
    # print(binary_search_re(d,6))
    # print(binary_search_re(d,8))
    # print(binary_search_re(d,11))
    # print(binary_search_re(d,12))
    # print(binary_search_re(c,0))
    # print(binary_search_re(c,1))
    # print(binary_search_re(c,2))
    # print(binary_search_re(c,3))
    # print(binary_search_re(c,4))
    # print(binary_search_re(c,5))
    # print(binary_search_re(c,6))

    # print('------测试二分查找最后一个值等于给定值的含重复元素的数组-----')
    # print(binary_search_re_2(a,7))
    # print(binary_search_re_2(b,1))
    # print(binary_search_re_2(b,7))
    # print(binary_search_re_2(d,-2))
    # print(binary_search_re_2(d,-1))
    # print(binary_search_re_2(d,0))
    # print(binary_search_re_2(d,4))
    # print(binary_search_re_2(d,6))
    # print(binary_search_re_2(d,8))
    # print(binary_search_re_2(d,11))
    # print(binary_search_re_2(d,12))
    # print(binary_search_re_2(c,0))
    # print(binary_search_re_2(c,1))
    # print(binary_search_re_2(c,2))
    # print(binary_search_re_2(c,3))
    # print(binary_search_re_2(c,4))
    # print(binary_search_re_2(c,5))
    # print(binary_search_re_2(c,6))

    # print('------测试二分查找第一个值大于等于给定值的含重复元素的数组-----')
    # print(binary_search_re_3(a,7))
    # print(binary_search_re_3(b,1))
    # print(binary_search_re_3(b,7))
    # print(binary_search_re_3(d,-2))
    # print(binary_search_re_3(d,-1))
    # print(binary_search_re_3(d,0))
    # print(binary_search_re_3(d,4))
    # print(binary_search_re_3(d,6))
    # print(binary_search_re_3(d,8))
    # print(binary_search_re_3(d,11))
    # print(binary_search_re_3(d,12))
    # print(binary_search_re_3(c,0))
    # print(binary_search_re_3(c,1))
    # print(binary_search_re_3(c,2))
    # print(binary_search_re_3(c,3))
    # print(binary_search_re_3(c,4))
    # print(binary_search_re_3(c,5))
    # print(binary_search_re_3(c,6))

    # print('------测试二分查找最后一个值小于等于给定值的含重复元素的数组-----')
    # print(binary_search_re_3(a,7))
    # print(binary_search_re_3(b,1))
    # print(binary_search_re_3(b,7))
    # print(binary_search_re_3(d,-2))
    # print(binary_search_re_3(d,-1))
    # print(binary_search_re_3(d,0))
    # print(binary_search_re_3(d,4))
    # print(binary_search_re_3(d,6))
    # print(binary_search_re_3(d,8))
    # print(binary_search_re_3(d,11))
    # print(binary_search_re_3(d,12))
    # print(binary_search_re_3(c,0))
    # print(binary_search_re_3(c,1))
    # print(binary_search_re_3(c,2))
    # print(binary_search_re_3(c,3))
    # print(binary_search_re_3(c,4))
    # print(binary_search_re_3(c,5))
    # print(binary_search_re_3(c,6))

    print('------测试二分查找循环有序含重复元素的数组中第一个等于给定值的元素-----')
    print(binary_search_re_cir(a,7))
    print(binary_search_re_cir(b,1))
    print(binary_search_re_cir(b,7))
    print(binary_search_re_cir(d,-2))
    print(binary_search_re_cir(d,-1))
    print(binary_search_re_cir(d,0))
    print(binary_search_re_cir(d,4))
    print(binary_search_re_cir(d,6))
    print(binary_search_re_cir(d,8))
    print(binary_search_re_cir(d,11))
    print(binary_search_re_cir(d,12))
    print(binary_search_re_cir(c,0))
    print(binary_search_re_cir(c,1))
    print(binary_search_re_cir(c,2))
    print(binary_search_re_cir(c,3))
    print(binary_search_re_cir(c,4))
    print(binary_search_re_cir(c,5))
    print(binary_search_re_cir(c,6))
    print(binary_search_re_cir(e,1))
    print(binary_search_re_cir(e,2))
    print(binary_search_re_cir(e,3))
    print(binary_search_re_cir(e,4))
    print(binary_search_re_cir(e,5))
    print(binary_search_re_cir(e,6))
    print(binary_search_re_cir(e,7))
    print(binary_search_re_cir(e,8))
    print(binary_search_re_cir(f,1))
    print(binary_search_re_cir(f,2))
    print(binary_search_re_cir(f,3))
    print(binary_search_re_cir(f,4))
    print(binary_search_re_cir(f,5))
    print(binary_search_re_cir(f,6))
    print(binary_search_re_cir(f,7))
    print(binary_search_re_cir(f,8))
