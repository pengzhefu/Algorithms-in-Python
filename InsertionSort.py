# -*- coding: utf-8 -*-
"""
Created on Fri Feb 22 14:38:28 2019

@author: pengz
"""

#####插入(Insertion)######
def InsertionSort(alist): #Written by my own
    sublist = [alist[0]]
    num_comp = len(alist) - 1
    x = 1
    while num_comp > 0 and x < len(alist):
        sublist.append(alist[x])
        start = len(sublist) - 1
        for i in range(start,0,-1):
            if sublist[i] < sublist[i-1]:
                sublist[i],sublist[i-1] = sublist[i-1],sublist[i]  ##其实真正的不应该交换，应该做移位（单一赋值）
        x = x+1
        num_comp = num_comp -1
    return sublist
#
#alist = [54,26,93,17,77,31,44,55,20]
#new = InsertionSort(alist)
#list1 = [20,30,40,90,50,60,70,80,100,110]
#new1 = InsertionSort(list1)             

def insertionSort(alist):
   for index in range(1,len(alist)):

     currentvalue = alist[index] ##先把要排序的这个值存下来
     position = index

     while position>0 and alist[position-1]>currentvalue:
         alist[position]=alist[position-1]  ##只做移位，把前一个的值(position-1)往后挪一位
         position = position-1

     alist[position]=currentvalue ##找到位置以后，把之前要排序的存下来的值再放进去

#alist = [54,26,93,17,77,31,44,55,20]
#insertionSort(alist)
#print(alist)

######希尔(Shell)########
def shellSort(alist):
    sublistcount = len(alist)//2
    while sublistcount > 0:

      for startposition in range(sublistcount):
        gapInsertionSort(alist,startposition,sublistcount)

      print("After increments of size",sublistcount,
                                   "The list is",alist)

      sublistcount = sublistcount // 2

def gapInsertionSort(alist,start,gap):
    for i in range(start+gap,len(alist),gap):

        currentvalue = alist[i]
        position = i

        while position>=gap and alist[position-gap]>currentvalue:
            alist[position]=alist[position-gap]
            position = position-gap

        alist[position]=currentvalue

alist = [54,26,93,17,77,31,44,55,20]
shellSort(alist)
print(alist)