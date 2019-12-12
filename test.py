"""python进阶的一些用法"""
# *args 的用法
#*args可以发送一个非键值对的可变数量的参数列表给一个函数

def test_var_args(f_arg,*argv):
    print("first nomal arg is",f_arg)
    for arg in argv:
        print("another arg through *argv",arg)

test_var_args('yasoob','python','eggs','test')

#**kwargs的用法
#**kwargs允许你将不定长度的键值对作为参数传递给一个函数

def greet_me(**kwargs):
    for key,value in kwargs.items():
        print("{0} == {1}".format(key,value))

greet_me(name ="yasoob")
#如果想在函数中使用这三种参数，顺序是这样的：
#some_func(fargs,*args,**kwargs)

#生成器也是一种迭代器，但只能迭代一次，因为它们并没有把所有的值存在内存中，而是运行时生成值
#python2里的标准库函数都会返回列表而python3修改返回生成器，因为生成器占用更少的资源
#计算斐波那契数列的生成器
#generator version
def fibon(n):
    a = b = 1
    for i in range(n):
        yield a
        a, b = b, a+b

for x in fibon(10):
    print(x)

# Map讲一个函数映射到一个输入列表的所有元素上
#大多的时候，我们讲列表中的元素一个个传递给函数，但Map用一种简单而漂亮的多的方法来实现

# items = [1,2,3,4,5]
# squared = []
# for i in items:
#     squared.append(i**2)
#
# print(squared)
#加入list转换是因为Python3返回迭代器
items = [1,2,3,4,5,6]
squared = list(map(lambda x: x**2,items))
print(squared)

#Filter过滤列表中的元素，并返回所有符合要求的元素构成的列表
#加入list转换是因为Python3返回迭代器
number_list = range(-5,5)
less_than_zero = filter(lambda x: x<0,number_list)
print(list(less_than_zero))
#这个filter类似一个for循环，但他是一个内置函数，更快

#Reduce对一个列表进行计算并返回结果
from functools import reduce
product = reduce((lambda x,y: x*y),[1,2,3,4])
print(product)

#set是一个非常有用的数据结构，它与list列表的行为类似，但它不能包含重复的值
#检查列表中是否包含重复的值
some_list = ['a','b','c','d','b','f']
duplicates = set([x for x in some_list if some_list.count(x) > 1])
print(duplicates)

#三元运算符,如果条件为真，返回真，否则返回假,用一行代码快速判断，而不是使用多行if语句
is_fat = True
state = "fat" if is_fat else "not fat"
#使用元组的三元运算符
#(if_test_is_False, if_test_is_True)[test]

#装饰器是修改其他函数功能的函数
#可以将一个函数赋值给一个变量，我们没有使用小括号所以不是在调用函数，而是讲它放在greet变量里面
#在函数中定义函数
#在函数中定义函数。创建嵌套的函数，调用外层函数时，内层函数也会运行，但是不能直接调用内部函数

#从函数中返回函数
def hi(name = "yasoob"):
    def greet():
        return "now you are in the greet() function"

    def welcome():
        return "now you are in the welcome() function"

    if name == "yasoob":
        #这里没有加()是因为有()函数就会执行，不加就只是被传递
        return greet
    else:
        return welcome

a = hi()
print(a)

#把函数作为参数传递给另一个函数
def hi():
    return "hi yasoob"

def dosomethingBeforeHi(func):
    print("i am doing some thing boring work before hi")
    print(func)

dosomethingBeforeHi(hi)

#装饰器使用场景
from functools import wraps
def decorator_name(f):
    @wraps(f)
    def decorated(*args,**kwargs):
        if not can_run:
            return "Funcation will not runn"
        return f(*args,**kwargs)
    return decorated

@decorator_name
def func():
    return ("Funcation is running")

can_run = True
print(func)

#类也可以用来构建装饰器，装饰器类

class logit(object):
    def __init__(self, logfile='out.log'):
        self.logfile = logfile

    def __call__(self, func):
        @wraps(func)
        def wrapped_function(*args,**kwargs):
            log_string = func.__name__+"was called"
            print(log_string)
            #打开logfile并写入
            with open(self.logfile, 'a') as opened_file:
                #现在将日志打到指定的文件
                opened_file.write(log_string+ '\n')
            #现在，发送一个通知
            self.notify()
            return func(*args,**kwargs)
        return wrapped_function

    def notify(self):
        #logit只打日志，不做别的
        pass

@logit()
def myfunc1():
    pass

#global全局变量，意味着在函数以外的区域访问
def add(value1,value2):
    global result
    result = value1 + value2

add(3,5)
print(result)

#对象变动Mutation
#将boo赋值为bar，对bar的改动会反映到两个变量中去
foo = ['hi']
print(foo)

bar = foo
bar += ['bye']
print(foo)

#容器Collections
#defaultdict与dict不同，它不需要检查key是否存在
from collections import defaultdict

colours = (('yasoob','yellow'),
           ('ali','blue'),
           ('arham','black'),
           ('ali','black'),
           ('yasoob','red'),
           )
favourite_colours = defaultdict(list)

for name, colour in colours:
    favourite_colours[name].append(colour)

print(favourite_colours)

#Counter是一个计数器，它帮助我们针对某项数据进行计数
from collections import Counter

colours = (
    ('yasoob','yellow'),
    ('ali','blue'),
    ('ali','blue'),
)
favs = Counter(name for name,colour in colours)
print(favs)

#deque提供了一个双端队列，你可以从头/尾两端添加删除元素
from collections import deque
d = deque(range(5))
print(len(d))

d.popleft()
d.pop()
