'''
动态规划

0-1背包问题
升级版0-1背包问题
最小路径和

编程实现莱文斯坦最短编辑距离
编程实现查找两个字符串的最长公共子序列
编程实现一个数据序列的最长递增子序列
'''



def pack_01(items,max_weight):
    memo = [False] * (max_weight+1)
    memo[0] = True
    if items[0] <= max_weight:
        memo[items[0]] = True
    for i in range(1,len(items)):
        for j in range(max_weight-items[i],-1,-1):
            if memo[j] == True:
                memo[j+items[i]] = True
    for i in range(max_weight,-1,-1):
        if memo[i] == True:
            return i
    return 0

def pack_01_adv(items,values,max_weight):
    n = len(items)
    memo = [[-1] * (max_weight+1) for i in range(0,n)]
    memo[0][0] = 0
    if items[0] <= max_weight:
        memo[0][items[0]] = values[0]
    for i in range(1,n):
        for j in range(0,max_weight+1):
            if memo[i-1][j] >= 0:
                memo[i][j] = memo[i-1][j]
        for j in range(0,max_weight-items[i]+1):
            if memo[i-1][j] >= 0:
                v = memo[i-1][j] + values[i]
                if v > memo[i][j+items[i]]:
                    memo[i][j+items[i]] = v
    max_value = -1
    for j in range(0,max_weight+1):
        if memo[n-1][j] > max_value:
            max_value = memo[n-1][j]
    # print(memo)
    return max_value



def double11(items,money):
    n = len(items)
    memo = [[False] * (2*money+1) for i in range(n)]
    memo[0][0] = True
    if items[0] <= 2*money:
        memo[0][items[0]] = True
    for i in range(1,n):
        for j in range(0,2*money+1):
            if memo[i-1][j] == True:
                memo[i][j] = memo[i-1][j]
        for j in range(0,2*money-items[i]+1):
            if memo[i-1][j] == True:
                memo[i][j+items[i]] = True
    for j in range(money,2*money+1):
        if memo[n-1][j] == True:
            break
    if j == 2*money+1:
        return
    for i in range(n-1,0,-1):
        if j - items[i] >= 0 and memo[i-1][j-items[i]] == True:
            print(str(items[i]),end=' ')
            j = j - items[i]
    if j != 0:
        print(items[0])
    print('\n')



def min_dist(weight,n):
    min_bt = float('inf')
    min_dp_table = float('inf')
    min_dp_equation = float('inf')
    def min_dist_bt(i,j,dist,weight,n):
        '''
        书上的棋子最短路径回溯代码会越界，得修改
        '''
        nonlocal min_bt
        dist += weight[i][j]
        if i == n-1 and j == n-1:
            if dist < min_bt:
                min_bt = dist
            return
        if i < n-1:
            min_dist_bt(i+1,j,dist,weight,n)
        if j < n-1:
            min_dist_bt(i,j+1,dist,weight,n)
    min_dist_bt(0,0,0,weight,n)

    def min_dist_dp_table(weight,n):
        '''
        状态转移表
        '''
        nonlocal min_dp_table
        memo = [[None] * n for i in range(0,n)]
        memo[0] = weight[0]
        sum = 0
        for i in range(0,n):
            sum += weight[i][0]
            memo[i][0] = sum
        for i in range(1,n):
            for j in range(1,n):
                memo[i][j] = weight[i][j] + min(memo[i][j-1],memo[i-1][j])
        min_dp_table = memo[n-1][n-1]
    min_dist_dp_table(weight,n)

    memo = [[0] * n for i in range(0,n)]
    def min_dist_dp_equation(i,j):
        '''
        状态转移方程
        '''
        nonlocal weight,memo,min_dp_equation
        if i == 0 and j == 0:
            return weight[0][0]
        if memo[i][j] > 0:
            return memo[i][j]
        min_left = float('inf')
        if j-1 >= 0:
            min_left = min_dist_dp_equation(i,j-1)
        min_up = float('inf')
        if i-1 >= 0:
            min_up = min_dist_dp_equation(i-1,j)
        cur_min_dist = weight[i][j] + min(min_left,min_up)
        memo[i][j] = cur_min_dist
        min_dp_equation = cur_min_dist
        return cur_min_dist
    min_dist_dp_equation(n-1,n-1)

    return min_bt,min_dp_table,min_dp_equation



def levenshtein(a,b):
    '''
    莱文斯坦距离
    '''
    n = len(a)
    m = len(b)
    min_dist_bt = float('inf')
    def dist_bt(i,j,edist,a,b):
        nonlocal min_dist_bt
        if i == n or j == m:
            if i < n:
                edist += n-i
            if j < m:
                edist += m-j
            if edist < min_dist_bt:
                min_dist_bt = edist
            return
        if a[i] == b[j]:
            dist_bt(i+1,j+1,edist,a,b)
        else:
            dist_bt(i+1,j,edist+1,a,b)
            dist_bt(i,j+1,edist+1,a,b)
            dist_bt(i+1,j+1,edist+1,a,b)
    dist_bt(0,0,0,a,b)

    def dist_dp(a,n,b,m):
        min_dist = [[None] * (n+1) for i in range(0,m+1)]
        for i in range(0,n+1):
            min_dist[i][0] = i
        for j in range(0,m+1):
            min_dist[0][j] = j
        for i in range(1,n+1):
            for j in range(1,m+1):
                if a[i-1] == b[j-1]:
                    min_dist[i][j] = min(min_dist[i-1][j]+1,min_dist[i][j-1]+1,min_dist[i-1][j-1])
                else:
                    min_dist[i][j] = min(min_dist[i-1][j]+1,min_dist[i][j-1]+1,min_dist[i-1][j-1]+1)
        return min_dist[n][m]
    min_dist_dp = dist_dp(a,n,b,m)

    return min_dist_bt,min_dist_dp



def lcs(a,b):
    '''
    最长公共子序列
    '''
    n = len(a)
    m = len(b)
    max_lcs = [[None] * (n+1) for i in range(0,m+1)]
    for i in range(0,n+1):
        max_lcs[i][0] = 0
    for j in range(0,m+1):
        max_lcs[0][j] = 0
    for i in range(1,n+1):
        for j in range(1,m+1):
            if a[i-1] == b[j-1]:
                max_lcs[i][j] = max(max_lcs[i-1][j],max_lcs[i][j-1],max_lcs[i-1][j-1]+1)
            else:
                max_lcs[i][j] = max(max_lcs[i-1][j],max_lcs[i][j-1],max_lcs[i-1][j-1])
    return max_lcs[n][m]



def yanghui_sanjiao(triangle):
    '''
    10.4.6思考题
    杨辉三角改造版
    '''
    n = len(triangle)
    min_dist = [[0] * (i+1) for i in range(0,n+1)]
    for i in range(1,n+1):
        for j in range(1,i+1):
            if j == i:
                min_dist[i][j] = triangle[i-1][j-1] + min_dist[i-1][j-1]
            else:
                min_dist[i][j] = triangle[i-1][j-1] + min(min_dist[i-1][j],min_dist[i-1][j-1])
            min_dist[i][0] = min_dist[i][1]
    print(min_dist)
    return min(min_dist[n][1:])

def min_coin(coin_list,money):
    '''
    思考题10.5.6
    最少需要几个硬币
    '''
    least_list = [0] * (money+1)
    m = len(coin_list)
    for i in range(1,money+1):
        tmp = []
        for j in coin_list:
            if i >= j:
                tmp.append(least_list[i-j]+1)
        least_list[i] = min(tmp)
    return least_list[money]

def lis(a):
    '''
    思考题10.6.6
    最长递增子序列
    '''
    n = len(a)
    max_lis = [1] * n
    for i in range(0,n):
        max_len = 0
        for j in range(0,i):
            if a[i] > a[j] and max_len < max_lis[j]:
                max_len = max_lis[j]
        max_lis[i] = max_len + 1
    return max_lis[n-1]



if __name__ == '__main__':
    print(pack_01([4,7,2,8],16))
    print(pack_01_adv([4,7,2,8],[9,6,4,5],16))
    double11([23,40,57,90,68,30,76,52,99],300)
    print(min_dist([[1,3,5,9],[2,1,3,4],[5,2,6,7],[6,8,4,3]],4))
    print(levenshtein('mitcmu','mtacnu'))
    print(lcs('mitcmu','mtacnu'))
    triangle = [[5],[7,8],[2,3,4],[4,9,6,1],[2,7,9,4,5]]
    print(yanghui_sanjiao(triangle))
    print(min_coin([1,3,5],15))
    print(lis([6,5,7,1,2,3]))