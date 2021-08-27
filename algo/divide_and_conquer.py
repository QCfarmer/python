'''
分治
利用分治算法求一组数据的逆序对个数
'''



def count_inversion(alist):
    num = 0
    n = len(alist)
    def merge(alist,p,q,r):
        i = p
        j = q+1
        k = 0
        nonlocal num
        tmp = [None] * (r-p+1)
        while i<=q and j<=r:
            if alist[i] <= alist[j]:
                tmp[k] = alist[i]
                k += 1
                i += 1
            else:
                num += (q-i+1)
                tmp[k] = alist[j]
                k += 1
                j += 1
        # while i <= q:
        #     tmp[k] = alist[i]
        #     k += 1
        #     i += 1
        # while j <= r:
        #     tmp[k] = alist[j]
        #     k += 1
        #     j += 1
        # for i in range(0,r-p+1):
        #     alist[p+i] = tmp[i]

        tmp[k:k+q+1-i] = alist[i:q+1]
        tmp[k+q+1-i:] = alist[j:]
        alist[p:] = tmp[:]
    def merge_sort_counting(alist,p,r):
        if p >= r:
            return
        q = (p+r)//2
        merge_sort_counting(alist,p,q)
        merge_sort_counting(alist,q+1,r)
        merge(alist,p,q,r)
    merge_sort_counting(alist,0,n-1)
    print(alist)
    return num



if __name__ == '__main__':
    print(count_inversion([1,5,6,2,3,4]))
    print(count_inversion([2,4,3,1,5,6]))
