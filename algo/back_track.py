'''
回溯
回溯重要的是先进行下一步操作，然后再恢复成上一步状态

利用回溯算法求解八皇后问题
利用回溯算法求解0-1背包问题

为了集中练习，多做了几道力扣上的回溯，掌握了套路

全排列
子集
组合总和
找出所有子集的异或总和再求和
二进制手表
'''



def queens(n):
    '''
    n皇后
    '''
    result = [None] * n
    res_num = 0
    def is_ok(row,col):
        nonlocal result
        leftup = col - 1
        rightup = col + 1

        ##################################################
        # f_pos = [[i,col] for i in range(row-1,-1,-1)] + [[i,j] for i in range(row-1,-1,-1) for j in range(col-1,-1,-1)if i>=0 and j >= 0] + [[i,j] for i in range(row-1,-1,-1) for j in range(col+1,n) if i>=0 and j<n]
        # for i in f_pos:
        #     if result[i[0]] == i[1]:
        #         return False
        ##################################################

        for i in range(row-1,-1,-1):
            if result[i] == col: #整列是否有棋子
                return False
            if leftup >= 0:
                if result[i] == leftup: #整条左上角是否有棋子
                    return False
            if rightup < n:
                if result[i] == rightup: #整条右上角是否有棋子
                    return False
            leftup -= 1
            rightup += 1
        return True
    # def print_queens(result):
    #     nonlocal n
    #     for row in range(0,n):
    #         for col in range(0,n):
    #             if result[row] == col:
    #                 print('Q',end=' ')
    #             else:
    #                 print('*',end=' ')
    #         print('\n')
    #     print('\n')
    def cal_8_queens(row):
        nonlocal n
        nonlocal result
        nonlocal res_num
        if row == n:
            # print_queens(result)
            res_num += 1
            return
        for col in range(0,n):
            if is_ok(row,col):
                result[row] = col
                cal_8_queens(row+1)
    cal_8_queens(0)
    return res_num



def pack_0_1(items,max_weight):
    '''
    01背包问题
    '''
    MAX_W = 0
    pack = []
    res = []
    def back_track(cur_i,cur_weight):
        nonlocal MAX_W,pack,res,max_weight,items
        if cur_weight == max_weight or cur_i == len(items):
            if cur_weight > MAX_W:
                MAX_W = cur_weight
                res = pack[:]
        for i in range(cur_i,len(items)):
            if cur_weight + items[i] <= max_weight:
                cur_weight = cur_weight+items[i]
                pack.append(items[i])
                back_track(i+1,cur_weight)
                cur_weight -= items[i]
                pack.pop()

        # 另一种想法
        # i = cur_i
        # if cur_weight == max_weight or cur_i == len(items):
        #     if cur_weight > MAX_W:
        #         MAX_W = cur_weight
        #         res = pack[:]
        #     return
        # if cur_weight + items[i] <= max_weight:
        #     cur_weight = cur_weight+items[i]
        #     pack.append(items[i])
        #     back_track(i+1,cur_weight)
        #     cur_weight -= items[i]
        #     pack.pop()
        # back_track(i+1,cur_weight)

    back_track(0,0)
    return MAX_W,res



def permutation(alist):
    '''
    全排列
    无重复元素
    递归
    '''
    res = []
    def back_track(restlist):
        path = []
        if len(restlist) <= 1:
            return [restlist]
        else:
            for i in range(len(restlist)):
                current = [[restlist[i]] + j for j in back_track(restlist[:i] + restlist[i+1:])]
                path.extend(current)
        return path
    res = back_track(alist)
    return res

def permute(nums):
    '''
    全排列
    无重复元素
    力扣的官方解法
    修改原数组再撤回减少空间使用
    '''
    def backtrack(first = 0):
        # 所有数都填完了
        if first == n:
            res.append(nums[:])
            return
        for i in range(first, n):
            # 动态维护数组
            nums[first], nums[i] = nums[i], nums[first]
            # 继续递归填下一个数
            backtrack(first + 1)
            # 撤销操作
            nums[first], nums[i] = nums[i], nums[first]
    n = len(nums)
    res = []
    backtrack()
    return res



def permutation2(nums):
    '''
    全排列
    有重复元素
    '''
    nums.sort()
    n = len(nums)
    res = []
    path = []
    visited = [0] * n
    def back_track(cur):
        if cur == n:
            res.append(path[:])
            return
        for i in range(0, n):
            if visited[i] == 1:
                continue
            elif i > 0 and nums[i] == nums[i-1] and visited[i-1] == 0:
                continue
            else:
                path.append(nums[i])
                visited[i] = 1
                back_track(cur + 1)
                path.pop()
                visited[i] = 0
    back_track(0)
    return res



def subset1(nums):
    '''
    所有子集
    原数组不含重复元素
    '''
    res = []
    n = len(nums)
    now_set = nums[:]
    def back_track(cur):
        nonlocal res,n,now_set

        res.append([i for i in now_set if i is not None])
        for i in range(cur,n):
            now_set[i] = None
            back_track(i+1)
            now_set[i] = nums[i]
        # 另一种想法
        # if cur == n:
        #     res.append([i for i in now_set if i is not None])
        #     return
        # i = cur
        # if now_set[i] is not None:
        #     now_set[i] = None
        #     back_track(i+1)
        #     now_set[i] = nums[i]
        # back_track(i+1)
    back_track(0)
    return res

def subset2(nums):
    '''
    所有子集
    原数组含重复元素
    '''
    res = []
    n = len(nums)
    path = []
    new_nums = sorted(nums)
    def back_track(cur):
        nonlocal res,n,path,new_nums
        if path not in res:
            res.append(path[:])
        for i in range(cur,n):
            if i > cur and new_nums[i] == new_nums[i-1]:
                continue
            path.append(new_nums[i])
            back_track(i+1)
            path.pop()
    back_track(0)
    return res

def subset(nums):
    '''
    所有子集
    力扣上的解法
    '''
    path = []
    res = []
    n = len(nums)
    def back_track(cur):
        nonlocal res,path,n
        res.append(path[:])
        for i in range(cur,n):
            path.append(nums[i])
            back_track(i+1)
            path.pop()
    back_track(0)
    return res



def combinationSum(candidates, target):
    '''
    组合总和
    '''
    res = []
    path = []
    candidates.sort()
    n = len(candidates)
    sum = 0
    def back_track(cur):
        nonlocal res,path,candidates,target,sum
        if sum == target:
            res.append(path[:])
            return
        for i in range(cur,n):
            if sum + candidates[i] > target:
                return
            if i > cur and candidates[i] == candidates[i-1]:
                continue #不可以重复
            else:
                path.append(candidates[i])
                sum += candidates[i]
                # back_track(i) #可以包含重复数字
                back_track(i+1) #不可以重复
                path.pop()
                sum -= candidates[i]
    back_track(0)
    return res



def subsetXORSum(nums: list) -> int:
    '''
    找出所有子集的异或总和再求和
    '''
    path = 0
    res = 0
    n = len(nums)
    def back_track(cur):
        nonlocal res,path,n
        res += path
        for i in range(cur,n):
            tmp = path
            path ^= nums[i]
            back_track(i+1)
            path = tmp
    back_track(0)
    return res



def readBinaryWatch(turnedOn: int):
    '''
    二进制手表
    '''
    path = []
    minutes = [1,2,4,8,16,32]
    hours = [1,2,4,8]
    time_hours = 0
    time_minute = 0
    res = []
    num = 0
    def back_track(cur):            
        nonlocal res,path,turnedOn,num,time_hours,time_minute
        if num == turnedOn:
            if time_hours > 11 or time_minute > 59 or num > turnedOn:
                return
            res.append("%d:%02d" % (time_hours,time_minute))
            return
        for i in range(cur,10):
            num += 1
            if i < 6:
                time_minute += minutes[i]
                back_track(i+1)
                time_minute -= minutes[i]
            else:
                time_hours += hours[i-6]
                back_track(i+1)
                time_hours -= hours[i-6]
            num -= 1
    back_track(0)
    return res



def max_time(nums):
    '''
    笔试题，和力扣949相似
    给定一个数组，里面有6个整数，求这个数组能够表示的最大24进制的时间是多少，输出这个时间，无法表示输出invalid。
    输入为一个整数数组，数组内有六个整数。输入整数数组长度为6，不需要考虑其他长度，元素值为0或者正整数，6个数字每个数字只能使用一次。
    输出一个为24小时格式的时间，或者字符串"invalid"。
    输入
    [0,2,3,0,5,6]
    输出
    23:56:00
    输入
    [9,9,9,9,9,9]
    输出
    invalid
    忽略输入写下解法
    '''
    res = []
    path = []
    visited = [0] * 6
    def back_track(cur):
        nonlocal nums,path,res
        if cur == 6:
            if path[0:2] > [2,3] or path[2:4] > [5,9] or path[4:6] > [5,9]:
                return
            if path > res:
                res = path[:]
        for i in range(0,6):
            if visited[i] == 1:
                continue
            path.append(nums[i])
            visited[i] = 1
            back_track(cur+1)
            visited[i] = 0
            path.pop()
    back_track(0)
    if res != []:
        return '{}{}:{}{}:{}{}'.format(res[0],res[1],res[2],res[3],res[4],res[5])
    else:
        return 'invalid'

def largestTimeFromDigits(arr:list) -> str:
    '''
    力扣949
    '''
    res = []
    path = []
    visited = [0] * 4
    def back_track(cur):
        nonlocal arr,path,res
        if cur == 4:
            if path[0:2] > [2,3] or path[2:4] > [5,9]:
                return
            if path > res:
                res = path[:]
        for i in range(0,4):
            if visited[i] == 1:
                continue
            path.append(arr[i])
            visited[i] = 1
            back_track(cur+1)
            visited[i] = 0
            path.pop()
    back_track(0)
    if res != []:
        return '{}{}:{}{}'.format(res[0],res[1],res[2],res[3])
    else:
        return ''




if __name__ == "__main__":
    # print(queens(8))
    # print(pack_0_1([2,4,5,6],14))

    # print(permutation([]))
    # print(permutation([1]))
    # print(permutation([1,2,3,4]))
    print(permutation2([]))
    print(permutation2([1]))
    print(permutation2([1,1,2]))

    # print(subset1([1,2,3]))
    # print(subset([1,2,3]))
    # print(subset2([1,2,3]))
    # print(subset2([1,2,2]))
    # print(subset2([4,4,4,1,4]))

    # print(combinationSum([2,3,5],8))
    # print(combinationSum([2,3,6,7],7))
    # print(combinationSum([2],1))
    # print(combinationSum([1],1))

    # print(combinationSum([10,1,2,7,6,1,5],8))
    # print(combinationSum([2,5,2,1,2],5))

    # print(subsetXORSum([1,3]))
    # print(subsetXORSum([5,1,6]))
    # print(subsetXORSum([3,4,5,6,7,8]))

    # print(readBinaryWatch(1))
    # print(readBinaryWatch(9))

    # print(max_time([2,3,0,0,5,9]))
    # print(max_time([9,9,9,9,9,9]))
    # print(max_time([4,9,1,6,9,2]))
    # print(max_time([3,2,2,3,6,0]))
    # print(max_time([1,8,6,4,5,8]))
    # print(max_time([9,8,9,0,0,0]))
    # print(max_time([1,8,9,0,0,9]))
    # print(max_time([0,0,0,0,0,0]))
