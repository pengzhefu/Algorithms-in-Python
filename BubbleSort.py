# -*- coding: utf-8 -*-
"""
Created on Thu Feb 21 15:29:35 2019

@author: pengz
"""

def bubbleSort(alist):
    for passnum in range(len(alist)-1,0,-1): ##passnum是遍历次数, 0是终点（不达到），-1是step
        for i in range(passnum):
            if alist[i]>alist[i+1]:
                temp = alist[i]
                alist[i] = alist[i+1]
                alist[i+1] = temp
                

list1 = [54,26,93,17,77,31,44,55,20]
bubbleSort(list1)
print(list1)

def BubbleSort(alist):  ##Write by my own
    num_pass = len(alist) -1 ## 遍历次输总共是n-1
    n = 1
    x = 1
    while n <= num_pass:
        for i in range(len(alist)-x):##每一次遍历的项的数目都不同，第一次最多，最后一次最少
            if alist[i] > alist[i+1]:
                alist[i],alist[i+1] = alist[i+1],alist[i]  ##针对Python的特性
        print(n)
        n = n+1
        x = x+1
list2 = [54,26,93,17,77,31,44,55,20,19,8,100]
BubbleSort(list2)
print(list2)
print(list1 == list2)

def shortBubbleSort(alist): ##冒泡排序的改进版，当发现列表已经排好了，就自动结束
    exchanges = True
    passnum = len(alist)-1
    while passnum > 0 and exchanges:
       exchanges = False
       for i in range(passnum):
           if alist[i]>alist[i+1]:
               exchanges = True  ##只要发现有一项换了，那就说明没complete
               temp = alist[i]
               alist[i] = alist[i+1]
               alist[i+1] = temp
       passnum = passnum-1

alist=[20,30,40,90,50,60,70,80,100,110]
shortBubbleSort(alist)
print(alist)