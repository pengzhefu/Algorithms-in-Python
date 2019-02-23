# -*- coding: utf-8 -*-
"""
Created on Fri Feb 22 17:29:51 2019

@author: pengz
"""

####归并算法######
def mergeSort(alist):
    print("Splitting ",alist)
    if len(alist)>1:
        mid = len(alist)//2 ##向下取整
        lefthalf = alist[:mid]
        righthalf = alist[mid:]

        mergeSort(lefthalf)
        
        mergeSort(righthalf)
       

        i=0
        j=0
        k=0
        while i < len(lefthalf) and j < len(righthalf):
            if lefthalf[i] < righthalf[j]:
                alist[k]=lefthalf[i]
                i=i+1
            else:
                alist[k]=righthalf[j]
                j=j+1
            k=k+1

        while i < len(lefthalf):
            alist[k]=lefthalf[i]
            i=i+1
            k=k+1

        while j < len(righthalf):
            alist[k]=righthalf[j]
            j=j+1
            k=k+1
    print("Merging ",alist)

#alist = [54,26,93,17,77,31,44,55,20]
#mergeSort(alist)
#print(alist)



lista = [2,4,5,7,10]
listb = [1,3,6,8,9]
        
def mergelist(list1,list2):    ##Written by my own, and this is the only merge function
    list3 = []
    i = 0   ##i,j分别为list1,list2的index，思想有些类似于指针
    j = 0
    while i < len(list1) or j < len(list2):
        if i >= len(list1): ##当list1里的元素全都被拿出来的时候
            for item in list2[j:]:
                list3.append(item)
                j = j+1
        elif j >=len(list2): ##当list2里的元素全都被拿出来的时候
            for item in list1[i:]:
                list3.append(item)
                i = i+1
        else: ##正常情况
            if list1[i] <= list2[j]:
                list3.append(list1[i])
                i = i+ 1
            else:
#                list1[i] > list2[j]
                list3.append(list2[j])
                j = j + 1
    return list3
print(mergelist(lista,listb))    


def MergeSort(alist):  ##Split部分由递归来实现, written by my own
    if len(alist) <= 1:
        return alist
    else:
        mid = int(len(alist)/2)
        lefthalf = MergeSort(alist[:mid])
        righthalf = MergeSort(alist[mid:])
        
#        final_list = merge_sorted_list(lefthalf,righthalf)
        
        final_list = mergelist(lefthalf,righthalf)
        
        return final_list

list1 = [7,26,93,17,77,31,44,55,20]
print(MergeSort(list1))