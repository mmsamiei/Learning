#in the name of God

#use "def" for define func

def add(x, y):
    return x+y

#how to call?
#1:
add(5, 6)
#2:
add(y=5 ,x=6)

#how to def func with tuple:
def func1(*args):
    return args

#how to def func with dict:
def func2(**args):
    return args.values()


#set global var

x = 5

def set_x(num):
    x = num
    print x


def set_global_x(num):
    global x
    print x     #prints 5
    x = num
    print x

set_x(44)
set_global_x(6)


#in python we can return FUNCTIONS!:D

def create_adder(x):
    def adder(y):
        return x+y
    return adder

add_10 = create_adder(10)
print add_10(3)


#in python we can use  Higher order function!:D
map(add_10,[1,2,3])     #prints 11,12,13
map(max,[1,2,3],[4,3,2])    #prints 4,3,3

#also
[add_10(i) for i in [1,2,3]] #  [11,12,13]

#we can return dict!!!!! :/

{x:x**2 for x in range(5)}  # {0:0 , 1:1 , 2:4, 3:9, 4:16}



