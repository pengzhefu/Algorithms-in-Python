# -*- coding: utf-8 -*-
"""
Created on Mon Feb 18 19:29:45 2019

@author: UPenn-BU-01
"""

###The Sequential Search### 复杂度为O(N)
def sequentialSearch(alist, item):
    found = False
#        pos = 0
#        found = False
#        length = len(alist)
#        while pos <= length-1 and not found:
#            if alist[pos] == item:
#                found = True
#            else:
#                pos+=1
#        return found
    for thing in alist:
        if thing == item:
            found = True
            break
    return found

list1 = [1,2,3,4,5,6,7,8,9]
print(sequentialSearch(list1, 5))

def orderedSequentialSearch(alist, item):
        pos = 0
        found = False
        stop = False
        length = len(alist)
        while pos < length-1 and not found and not stop:
            if alist[pos] == item:
                found = True
            elif alist[pos] > item:
                stop = True
            else:
                pos+=1
        return found
    
list1 = [2,3,4,6,7,8,9]
print(orderedSequentialSearch(list1, 5))