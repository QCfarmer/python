'''
实现冒泡排序、插入排序、选择排序、归并排序、快速排序
'''

def bubble_sort(alist):
    '''
    冒泡排序
    '''
    if len(alist) <= 1:
        return
    else:
        for i in range(len(alist)):
            flag = False
            for j in range(0,len(alist)-i-1):
                if a[j] > a[j+1]: #稳定排序
                    tmp = alist[j]
                    alist[j] = alist[j+1]
                    alist[j+1] = tmp
                    flag = True
            if not flag:
                break

def insertion_sort(alist):
    '''
    插入排序
    '''
    if len(alist) <= 1:
        return
    else:
        for i in range(1,len(alist)):
            value = alist[i]
            j = i - 1
            while j >= 0:
                if alist[j] > value: #稳定排序
                    alist[j+1] = alist[j]
                    j -= 1
                else:
                    break
            alist[j+1] = value
    
def selection_sort(alist):
    '''
    选择排序
    '''
    if len(alist) <= 1:
        return alist
    else:
        for i in range(0,len(alist)-1):
            minus = i
            for j in range(i+1,len(alist)):
                if alist[j] < alist[minus]:
                    minus = j
            tmp = alist[i]
            alist[i] = alist[minus]
            alist[minus] = tmp

# def merge_sort(alist):
#     '''
#     归并排序
#     '''
#     if len(alist) < 2:
#         return alist
#     else:
#         mid = len(alist) // 2
#         left = alist[0:mid]
#         right = alist[mid:]
#         left = merge_sort(left)
#         right = merge_sort(right)
#         alist = [i for i in left] + [j for j in right]
#         i = 0
#         j = mid
#         tmp = []
#         while i<mid and j<len(alist):
#             if alist[i] <= alist[j]:
#                 tmp.append(alist[i])
#                 i += 1
#             else:
#                 tmp.append(alist[j])
#                 j += 1
#         if i < mid:
#             for item in alist[i:mid]:
#                 tmp.append(item)
#         else:
#             for item in alist[j:]:
#                 tmp.append(item)
#         return tmp

def merge_sort(alist):
    '''
    归并排序
    '''
    if len(alist) < 2:
        return
    else:
        mid = len(alist) // 2
        left = alist[0:mid]
        right = alist[mid:]
        merge_sort(left)
        merge_sort(right)
        i = 0
        j = 0
        k = 0
        while i<len(left) and j<len(right):
            if left[i] <= right[j]:
                alist[k] = left[i]
                i += 1
            else:
                alist[k] = right[j]
                j += 1
            k += 1
        if i < len(left):
            for item in left[i:]:
                alist[k] = item
                k += 1
        if j < len(right):
            for item in right[j:]:
                alist[k] = item
                k += 1
        return

def quick_sort(alist):
    '''
    快速排序
    '''
    if len(alist) < 2:
        return alist
    else:
        pivot = len(alist)//2 - 1
        tmp = alist[pivot]
        alist.pop(pivot)
        small = [i for i in alist if i <= tmp]
        big = [i for i in alist if i > tmp]
        return quick_sort(small) + [tmp] + quick_sort(big)

if __name__ == '__main__':
    print('-------测试冒泡排序-------')
    a = [4,5,6,3,2,1]
    bubble_sort(a)
    print(a)

    print('-------测试插入排序-------')
    a = [4,5,6,3,2,1]
    insertion_sort(a)
    print(a)

    print('-------测试选择排序-------')
    a = [4,5,6,3,2,1]
    selection_sort(a)
    print(a)

    print('-------测试归并排序-------')
    a = [3,2,1]
    merge_sort(a)
    print(a)

    print('-------测试快速排序-------')
    a = [4,5,6,3,2,1]
    print(quick_sort(a))
