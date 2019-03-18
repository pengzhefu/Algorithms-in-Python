# -*- coding: utf-8 -*-
"""
Created on Sun Mar 17 00:55:11 2019

@author: pengz
"""

## Array rotation
## arr[]是list, d是要移动的个数,n是总个数
def rotate1(list1,d):  ## 这个方法的空间复杂度为O(d),时间复杂度为O(N)
    new_list = list1[d:]
    for i in range(d):
        new_list.append(list1[i])
    return new_list

#print(rotate1([1,2,3,4,5,6,7],2))

## 下面这个方法的时间复杂度为O(n*d),但是空间复杂度为O(1),只用了一个变量
def rotate2(list1,d):
    for i in range(d):
        left_move(list1)
    return list1

def left_move(list1):
    tmp = list1[0]
    for i in range(len(list1)-1):
        list1[i] = list1[i+1]
    list1[len(list1)-1] = tmp
    return list1
#print(rotate2([1,2,3,4,5,6,7],2))

## 下面这个方法其实是方法2的延申，先找出n和d的最小公约数gcd,一共移动gcd轮,每轮一共移动n/gcd次
## 空间复杂度为O(1),时间复杂度为O(N)
def gcd(a,b):
    for i in range(b,0,-1):
        if a % i == 0 and b % i == 0:
            return i

def rotate3(arr, d, n): 
    for i in range(gcd(d, n)): ## i代表这是第几次移动
                                ## 所以一共移动gcd轮
        # move i-th values of blocks  
        temp = arr[i] 
        j = i 
        count = 0
        while 1:
            
            k = j + d   ## d代表间隔，也就是总共要移走几个 
            if k >= n: ## 这两个if共同是防止超出index的，如果超出，就减n,回到正常水平
                            ## 然后跳出这一轮的交换，进行下一轮的交换
                k = k - n 
            if k == i: 
                break
            arr[j] = arr[k]  ## 进行一个交换
            count +=1
            print(count)
            j = k ## j移到下一个要被赋值的点，
        arr[j] = temp
    return arr         
#print(rotate3([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15],6,15))

## 第四个方法用到了reversal的想法
## 这里面也包含了基本的要自己reverse一个列表该怎么写的步骤
## 最重要是知道BA = (ArBr)r
def reversal(list1,start,last):  ## 加上两个参数start和last帮助reversal函数能够只reverse part of list
#    start = 0
#    last = len(list1) - 1
    while start < last:
        tmp = list1[start]
        list1[start] = list1[last]
        list1[last] = tmp
        start += 1
        last -= 1
    return list1
arr = [1,2,3,4,5]
a = reversal(arr,0,3)
#list1 = [1,2,3,4,5]
def rotate4(list1,d):
    reversal(list1,0,d-1)   ## 因为index是从0开始的，所以前d个是0--d-1
    reversal(list1,d,len(list1)-1)
    reversal(list1,0,len(list1)-1)
    return list1

arr=[1,2,3,4,5,6,7,8,9,10]
print(rotate4(arr,9))

## rightRotate就是和left反过来
def RightRotate(list1,d):
    reversal(list1,0,len(list1)-1)   
    reversal(list1,0,d-1)
    reversal(list1,d,len(list1)-1)
    return list1
arr=[1,2,3,4,5,6,7,8,9,10]
#print(RightRotate(arr,3))

'''

Print left rotation of array in O(n) time and O(1) space

Given an array of size n and multiple values around 
which we need to left rotate the array. How to quickly print multiple left rotations?
Input : arr[] = {1, 3, 5, 7, 9}
        k1 = 14 
Output : 9 1 3 5 7
'''
def leftRotate(arr,k1):
    d = k1%len(arr)
    if d == 0:
        return arr
    else:
        reversal(arr,0,d-1)
        reversal(arr,d,len(arr)-1)
        reversal(arr,0,len(arr)-1)
    return arr
#print(leftRotate([1,3,5,7,9],14))
    
##  