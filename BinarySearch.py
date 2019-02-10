# -*- coding: utf-8 -*-
"""
Created on Mon Aug 27 11:46:00 2018

@author: pengz
"""

print("有序数组中的二分查找")
key=int(input("请输入您要查找的整数："))
c=[10,11,12,17,19,21,22,24,32,38,49,51,66,77,90]
def BinarySearch(key,c):
    lo,hi= 0,len(c)-1
    while lo<=hi:
        mid = int(lo+(hi-lo)/2) ## 这一步最为重要
        if key<c[mid]:
            hi = mid-1
        elif key>c[mid]:
            lo = mid+1
        else:
            return print("%s在数组中的索引为%s"%(key,mid))
    return print("%s不在该数组中"%key)
BinarySearch(key,c)