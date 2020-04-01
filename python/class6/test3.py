# coding=utf-8


def sum_xy(x=1, y=2):
    print(x)
    print(y)
    z = x + y
    return


# 函数的调用
print(sum_xy(3, 22))


def test_args(a, b, c=None, d=None, *args, **kwargs):
    print(a)
    print(b)
    print(c)
    print(d)
    print(args)
    print(type(args))
    print(kwargs)
    print(type(kwargs))

test_args(1, 2, 3, 4, 5, 6, 7, 8, 9, e=11, f=45)


# n!表示,n*(n-1)*(n-2)#...*1,成为n的阶乘
def jc(n):
    # 出口
    if n == 1:
        # return:函数在任何位置如果return了，就代码函数执行完了
        # 后的代码都不再执行
        return 1

    return n * jc(n - 1)

print(jc(4))
