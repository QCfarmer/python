'''
编程实现斐波那契数列求值f(n)=f(n-1)+f(n-2)
编程实现求阶乘n!
编程实现一组数据集合的全排列
'''

# 备忘录字典
solved_fib_list = dict()
def fib(n):
    '''
    斐波那契
    '''
    if n < 1:
        return 'wrong number'
    if n == 1:
        return 0
    elif n == 2:
        return 1
    elif n in solved_fib_list:
        return solved_fib_list[n]
    else:
        ret = fib(n-1) + fib(n-2)
        solved_fib_list[n] = ret
        return ret

def fact(n):
    '''
    阶乘n!
    '''
    if n < 1:
        return 'wrong number'
    elif n == 1:
        return 1
    else:
        return n * fact(n-1)

def permutation(num_list):
    '''
    全排列
    '''
    if len(num_list) < 1:
        return 'empty list'
    elif len(num_list) == 1:
        return num_list
    elif len(num_list) == 2:
        return [[num_list[0],num_list[1]],[num_list[1],num_list[0]]]
    else:
        ret = []
        for i in range(len(num_list)):
            rest = num_list[:]
            rest.pop(i)
            next = permutation(rest)
            for j in next:
                ret.append([num_list[i]] + j)
        return ret

if __name__ == '__main__':
    print('----------测试斐波那契-----------')
    print(fib(0))
    print(fib(1))
    print(fib(2))
    print(fib(3))
    print(fib(4))
    print(fib(5))
    print(fib(6))
    print(fib(7))

    print('-----------测试阶乘-----------')
    print(fact(0))
    print(fact(1))
    print(fact(2))
    print(fact(3))
    print(fact(4))
    print(fact(5))

    print('-----------测试全排列-----------')
    print(permutation([]))
    print(permutation([1]))
    print(permutation([1,2]))
    print(permutation([1,2,3]))
    print(permutation([1,2,3,4]))
