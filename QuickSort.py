# -*- coding: utf-8 -*-
"""
Created on Mon Aug 27 11:12:01 2018

@author: pengz
"""
## 第一种方法
def QuickSort(myList,start,end):  # 这个方法会递归太深，不行
   #判断low是否小于high,如果为false,直接返回
   if start < end:
       i,j = start,end
       #设置基准数
       base = myList[i]

       while i < j:
           #如果列表后边的数,比基准数大或相等,则前移一位直到有比基准数小的数出现
           while (i < j) and (myList[j] >= base):
               j = j - 1

           #如找到,则把第j个元素赋值给第个元素i,此时表中i,j个元素相等
           myList[i] = myList[j]

           #同样的方式比较前半区
           while (i < j) and (myList[i] <= base):
               i = i + 1
           myList[j] = myList[i]
       #做完第一轮比较之后,列表被分成了两个半区,并且i=j,需要将这个数设置回base
       myList[i] = base

       #递归前后半区
       QuickSort(myList, start, i - 1)
       QuickSort(myList, j + 1, end)
   return myList
#
#
#myList = [49,38,65,97,76,13,27,49]
#print("Quick Sort: ")
#QuickSort(myList,0,len(myList)-1)
#print(myList)

## 第二种方法
# https://chinese.freecodecamp.org/news/sorting-in-python/
def QuickSort_recur(arr,firstIndex,lastIndex):
    if firstIndex<lastIndex:
        divIndex=Partition(arr,firstIndex,lastIndex)

        ## 相当于在递归，分成两组后每次都进行同样的处理
        QuickSort_recur(arr,firstIndex,divIndex)       
        QuickSort_recur(arr,divIndex+1,lastIndex)
    else:
        return
 
## 将数组分为两组，第一个基准数复位
def Partition(arr,firstIndex,lastIndex):
    i=firstIndex-1
    pivot = arr[lastIndex]
    for j in range(firstIndex,lastIndex):
        if arr[j]<=pivot:
            i=i+1
            arr[i],arr[j]=arr[j],arr[i]
    arr[i+1],arr[lastIndex]=arr[lastIndex],arr[i+1]  # i+1相当于i和j的相遇的位置
    return i
 
 
arr=[1,4,7,1,5,5,3,85,34,75,23,75,2,0]
 
print("initial array:\n",arr)
QuickSort_recur(arr,0,len(arr)-1)
print("result array:\n",arr)