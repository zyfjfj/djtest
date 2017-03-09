# encoding: utf-8
"""
@version: ??
@author: zhayufeng
@contact: zyfjfj@163.com
@software: PyCharm
@file: setup
@time: 2016/8/17 11:45
"""
from distutils.core import setup
from Cython.Build import cythonize
'''
用于生成pyd库
'''
setup(
  ext_modules = cythonize("computeScore.py"),
)
