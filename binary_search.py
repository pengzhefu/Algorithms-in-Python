# -*- coding: utf-8 -*-
"""
Created on Mon Feb 18 21:21:11 2019

@author: UPenn-BU-01
"""

######Binary Search######
def binarySearch(alist, item):
    first = 0
    final = len(alist) -1
    found = False
    while not found and first <= final:  ##这个中止条件一定要记牢！
        mid = int((first+final)/2)
        if alist[mid] == item:
            found = True
        elif alist[mid] < item:
            first = mid + 1
        else:
            final = mid - 1
    
    return found
#    return first  ## 此时如果没找到的话，那么return的first的值就是这个数插入这个列表的index

list2 = [1,4,5,7,10,14,15,17]
print(binarySearch(list2,4.5))

############Recursive version##########
def RebinarySearch(alist,item):
    first = 0
    final = len(alist)-1
    mid = int((first+final)/2)
    if len(alist) == 0:  ###这个是最基本情况，the base case
        return False
    else:
        if alist[mid] == item:
            return True
        elif alist[mid] > item:
            return RebinarySearch(alist[:mid],item)
        else:
            return RebinarySearch(alist[mid+1:],item)
testlist = [0, 1, 2, 8, 13, 17, 19, 32, 42]
#print(RebinarySearch(testlist,30))