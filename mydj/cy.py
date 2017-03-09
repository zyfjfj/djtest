# encoding: utf-8
"""
@version: ??
@author: zhayufeng
@contact: zyfjfj@163.com
@software: PyCharm
@file: cy
@time: 2016/8/17 11:45
"""
#python setup.py build_ext --inplace
def say_hello_to(name):
    print("Hello %s!" % name)
def fib(n):
    """Print the Fibonacci series up to n."""
    a, b = 0, 1
    while b < n:
        print b,
        a, b = b, a + b