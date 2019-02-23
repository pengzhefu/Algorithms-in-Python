# -*- coding: utf-8 -*-
"""
Created on Sat Feb 23 02:14:12 2019

@author: pengz
"""

#def quickSort(alist):
#   quickSortHelper(alist,0,len(alist)-1)

def quickSort(alist,first,last):
   if first<last:

       splitpoint = partition(alist,first,last)

       quickSort(alist,first,splitpoint-1)
       quickSort(alist,splitpoint+1,last)
   else:
       return alist
        


def partition(alist,first,last):
   pivotvalue = alist[first]

   leftmark = first+1
   rightmark = last

   done = False
   while not done:
       #####一定要先移动left!
       while leftmark <= rightmark and alist[leftmark] <= pivotvalue:
           leftmark = leftmark + 1
          
        ####这个条件的大于等于，就是为了找到离leftmark最近的那个rightmark的跳出点，就是split point
        ####因为split point一般其实都在leftmark的附近，也就是离leftmark最近的rightmark,一般为left-1
       while alist[rightmark] >= pivotvalue and rightmark >= leftmark:
           rightmark = rightmark -1

       if rightmark < leftmark:##发现如果已经是cross了，那就跳出，进行pivot的swap
                               ##在移动了left和right之后再检查,给right<left的一个机会
           done = True
       else:
#           print("Now we exchange:",alist[leftmark], alist[rightmark])
           ##进行一次普通交换
           alist[leftmark], alist[rightmark] = alist[rightmark], alist[leftmark]

#   print("left is,",leftmark)
   ##把pivot和split point的值互换，让pivot做分割点 
   alist[first], alist[rightmark] = alist[rightmark], alist[first]


   return rightmark

alist = [58,26,93,17,77,31,44,55,20,78]
quickSort(alist,0,len(alist)-1)
print(alist)
#a = partition(alist,0,len(alist)-1)
#print(alist)