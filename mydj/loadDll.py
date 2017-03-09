#coding=utf-8
import ctypes
from ctypes import *
from numpy import *

'''cdecl格式的调用要用ctypes.cdll.LoadLibrary,ctypes.CDll'''
''' ctypes.windll.LoadLibrary, ctypes.WinDll'''
'''http://www.cnblogs.com/wuchang/archive/2010/04/04/1704456.html'''
DoubleArrayType = c_double * 10  # 相当于定义了一个double[10]类型

class ReturnData(Structure):
    _fields_ = [
        ("dArray", c_double * 2)
    ]
class PrintDriver():
    def __init__(self):
        try:
            self.dll = ctypes.cdll.LoadLibrary("Analysis.dll")
        except WindowsError as e:
            self.dll = None
            print(u'加载dll失败')
            raise e
    def Add(self,a,b):
        return self.dll.add(a,b)
    def myprint(self):
        return self.dll.show_text()
    def GetStructInfo(self):
        return self.dll.GetStructInfo
    def getAverage(self,list):
        getAverage=self.dll.getAverage
        getAverage.restype = c_double
        return getAverage(list,10)
    def doubleAdd(self,d1,d2):
        add_double = printD.dll.add_double
        '''下边这句设置返回数据类型'''
        add_double.restype = c_double
        return add_double(c_double(d1),c_double(d2))

    '''两种方式传数组进去
       1、利用自己定义数组
       2、用numpy的数组'''
    def Myavervar_one(self,list):
        myavervar=self.dll.myavervar
        #这里定义输入的类型,这里设置是的自己定义数组
        myavervar.argtypes = [DoubleArrayType,c_int,POINTER(ReturnData)]
        objectStruct = ReturnData()
        # invoke api GetStructInfo
        myavervar(list,10,byref(objectStruct))
        # check result
        for i, val in enumerate(objectStruct.dArray):
             print 'dArray[i]: ', val

    def Myavervar_tow(self, list):
         myavervar = self.dll.myavervar
         # 这里定义输入的类型，这里要设置输入的是指针
         myavervar.argtypes = [c_void_p, c_int, POINTER(ReturnData)]
         objectStruct = ReturnData()
         # invoke api GetStructInfo
         myavervar(list, 10, byref(objectStruct))
         # check result
         for i, val in enumerate(objectStruct.dArray):
             print 'dArray[%d]: '%i, val
# define struct

if __name__=="__main__":
    printD=PrintDriver()
    print printD.Add(1,2)
    show_text=printD.myprint()
    size = -1
    rst = ctypes.string_at(show_text, size)
    print(rst)
    #
    # ARRAY_NUMBER = 20
    # STR_LEN = 20
    # # define type
    # INTARRAY20 = ctypes.c_int * ARRAY_NUMBER;
    # CHARARRAY20 = ctypes.c_char * STR_LEN;
    #
    #
    # # define struct
    # class StructTest(Structure):
    #     _fields_ = [
    #         ("number", ctypes.c_int),
    #         ("pChar", ctypes.c_char_p),
    #         ("str", CHARARRAY20),
    #         ("iArray", INTARRAY20)
    #     ]
    #
    #
    # # load dll and get the function object
    # GetStructInfo = printD.GetStructInfo()
    # # set the return type
    # GetStructInfo.restype = ctypes.c_char_p
    # # set the argtypes
    # GetStructInfo.argtypes = [POINTER(StructTest)]
    # objectStruct = StructTest()
    # # invoke api GetStructInfo
    # retStr = GetStructInfo(byref(objectStruct))
    # # check result
    # print "number: ", objectStruct.number
    # print "pChar: ", objectStruct.pChar
    # print "str: ", objectStruct.str
    # for i, val in enumerate(objectStruct.iArray):
    #     print 'Array[i]: ', val
    # print retStr;

    a_list=array([1.1, 3.6, 3.3, 7.4, 95,1.6, 88.7, 1.8, 8.9, 1.2], dtype=c_double)
    #求平均值
    print "平均值",a_list.mean()
    print "方差",a_list.var()
    arr = DoubleArrayType(1.1,3.6, 3.3, 7.4, 95,1.6, 88.7, 1.8, 8.9, 1.2)
    #用
    print printD.getAverage(a_list.ctypes.data)
    print "第一种方式:",printD.Myavervar_one(arr)
    print "第二种方式:",printD.Myavervar_tow(a_list.ctypes.data)
