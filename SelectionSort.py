# -*- coding: utf-8 -*-
"""
Created on Thu Feb 21 23:09:03 2019

@author: pengz
"""

######选择（Selection）排序##########
def SelectionSort(alist):  ##Writen by my own
       num_pass = len(alist) -1  ##遍历次数总共n-1次
       while num_pass > 0:
           largest_idx = 0
           for i in range(num_pass):
               if alist[largest_idx] < alist[i+1]:
                   largest_idx = i+1
           print(alist[largest_idx]) 
           alist[num_pass], alist[largest_idx] = alist[largest_idx],alist[num_pass]
           num_pass = num_pass - 1
list2 = [54,26,93,17,77,31,44,55,20]
SelectionSort(list2)

def selectionSort(alist):
   for fillslot in range(len(alist)-1,0,-1):
       positionOfMax=0
       for location in range(1,fillslot+1):
           if alist[location]>alist[positionOfMax]:
               positionOfMax = location

       temp = alist[fillslot]
       alist[fillslot] = alist[positionOfMax]
       alist[positionOfMax] = temp

alist = [54,26,93,17,77,31,44,55,20]
selectionSort(alist)
print(alist)
print(list2 == alist)