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
#arr = [1,2,3,4,5]
#a = reversal(arr,0,3)
#list1 = [1,2,3,4,5]
def rotate4(list1,d):
    reversal(list1,0,d-1)   ## 因为index是从0开始的，所以前d个是0--d-1
    reversal(list1,d,len(list1)-1)
    reversal(list1,0,len(list1)-1)
    return list1

#arr=[1,2,3,4,5,6,7,8,9,10]
#print(rotate4(arr,9))

## rightRotate就是和left不同的地方在于，先整体调换，然后转前半部分，然后转后半部分
def RightRotate(list1,d):
    reversal(list1,0,len(list1)-1)   
    reversal(list1,0,d-1)
    reversal(list1,d,len(list1)-1)
    return list1
#arr=[1,2,3,4,5,6,7,8,9,10]
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
    
##  Devise a way to find an element in the rotated array in O(log n) time.
'''
The idea is to find the pivot point, divide the array in two sub-arrays and call binary search.
The main idea for finding pivot is – for a sorted (in increasing order) and pivoted array, 
pivot element is the only element for which next element to it is smaller than it.
Using above criteria and binary search methodology we can get pivot element in O(logn) time
'''
# Function to get pivot. For array  
# 3, 4, 5, 6, 1, 2 it returns 3  
# (index of 6) 

## 所以是找pivot用O(logn),再二分法找用O(logn),两个O(logn)就是O(logn) 
def findPivot(arr, low, high):   ## 用二分法的思想来找pivot点，所以也是O(logn)
      
    # base cases 
    if high < low: 
        return -1
    if high == low: 
        return low 
      
    mid = int((low + high)/2) 
      
    if mid < high and arr[mid] > arr[mid + 1]: #加上mid<high和mid > low的条件是防止mid到了边界,pivot不可能在首尾
        return mid 
    if mid > low and arr[mid] < arr[mid - 1]: 
        return (mid-1)
    ## 如果没找到，接着分
    if arr[low] >= arr[mid]: ## 列表首位的很大，说明前面很短，pivot在前半段 
        return findPivot(arr, low, mid-1) 
    return findPivot(arr, mid + 1, high)  ## 列表的首位不大，说明前面比较长，pivot在后半段
def binarySearch(arr,k):
    start = 0
    last = len(arr)-1
    find = False
    while not find:
        mid = (start + last)//2
        if arr[mid] == k:
            return mid
        elif arr[mid] > k:
            last = mid - 1
        else:
            start = start + 1
#arr1 = [3,4,5,6,1,2]
#b = findPivot(arr1,0,4)
#arr2 = [1,2,3,4,5]
#c = binarySearch(arr2,4)
def findElement(arr,n,key):
    pivot = findPivot(arr,0,n-1)
    if key < arr[0]:
        return pivot+1+binarySearch(arr[pivot+1:],key)
    elif key > arr[0]:
        return binarySearch(arr[:pivot+1],key)
    else:
        return pivot

#arr = [4,5,6,7,8,9,10,1,2,3]
#b = findElement(arr,10,1)
    
'''
Given a sorted and rotated array, find if there is a pair with a given sum

Given an array that is sorted and then rotated around an unknown point. Find if the array 
has a pair with a given sum ‘x’. 
It may be assumed that all elements in the array are distinct.  
'''
## 很简单，还是用双指针，只是要先找到pivot，也就是last,往后一位就是first
def findPair(arr,k):
    last = findPivot(arr,0,len(arr)-1)
    first = last+1
    find = False
    while not find:
        ## 先调整,把last和first换成正常的index
        if first < 0:
            i = first + len(arr)
        elif first >= len(arr):
            i = first - len(arr)
        else:
            i = first
        if last < 0:
            j = last + len(arr)
        elif last >= len(arr):
            j = last - len(arr)
        else:
            j = last
        ## 再进行比较，然后移动坐标
        if i != j:  ## 如果两个的index相等了，说明找了一圈没找到了，就直接break
            if arr[i] + arr[j] == k:
                find = True
            elif arr[i] + arr[j] < k:
                first = first+1
            else:
                last = last-1
        else:
            break
#    print(first,last)
#    print(i,j)
    return find
#a = findPair([4,5,6,7,1,2,3],9)

## 升级难度
'''
How to count all pairs having sum x?
'''
def countPair(arr,k):
    last = findPivot(arr,0,len(arr)-1)
    first = last + 1
    finding = True
    cnt = 0
    while finding:
        ## 先调整,把last和first换成正常的index
        if first < 0:
            i = first + len(arr)
        elif first >= len(arr):
            i = first - len(arr)
        else:
            i = first
        if last < 0:
            j = last + len(arr)
        elif last >= len(arr):
            j = last - len(arr)
        else:
            j = last
        if i != j:  ## 如果两个的index相等了，说明找了一圈没找到了，就直接break
            if arr[i] + arr[j] == k:
                cnt = cnt+1   ## 找到了以后，计数+1
                first = first+1  ## 并且移动其中一个，继续找
            elif arr[i] + arr[j] < k:
                first = first+1
            else:
                last = last-1
        else:  ## 直到首尾的index相等了，才跳出循环
            break
    return cnt

#b = countPair([4,5,6,7,1,2,3],14)  
    
'''

Find maximum value of Sum( i*arr[i]) with only rotations on given array allowed

Given an array, only rotation operation is allowed on array. We can rotate the 
array as many times as we want. Return the maximum possbile of summation of i*arr[i].

Examples :

Input: arr[] = {1, 20, 2, 10}
Output: 72
We can 72 by rotating array twice.
{2, 10, 1, 20}
20*3 + 1*2 + 10*1 + 2*0 = 72

Input: arr[] = {10, 1, 2, 3, 4, 5, 6, 7, 8, 9};
Output: 330
We can 330 by rotating array 9 times.
{1, 2, 3, 4, 5, 6, 7, 8, 9, 10};
0*1 + 1*2 + 2*3 ... 9*10 = 330
'''
def maxSum(arr):     ## 相当于只用遍历列表两次，time complexity is O(n)
    times = len(arr)-1
    n = len(arr)
    arrsum = 0
    res = 0
    j = 0
    while j < len(arr):  ## 把初始结果和arrsum一起算！
        res += j*arr[j]
        arrsum += arr[j]
        j +=1
    i = 1
    cur_res = res
    while i <= times:
        cur_res = cur_res + arrsum-n*arr[n-i]
        res = max(res,cur_res)
        i = i+1
    return res
#a = maxSum([1,2,3,4,5,6,7,8,9,10])

## 找一个乱序序列的前k个最大的数
'''
For example, if given array is [1, 23, 12, 9, 30, 2, 50] and you are 
asked for the largest 3 elements i.e., k = 3 then your program should print 50, 30 and 23.
'''
def findMax1(arr,k):    ## Written by my own, time complexity is O(k*n)
    for j in range(k):
        res1 = arr[0]
        for i in range(len(arr)-j):
            if arr[i] > res1:
                res1 = arr[i]
                index = i
        arr[i], arr[index] = arr[index], arr[i]
    for k in range(len(arr)-1,len(arr)-1-k,-1):
        print(arr[k], end= ',')
arr = [1,23,12,9,30,2,50,43]
#findMax1(arr,3)

## 先尝试找第k小
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
## 找第k小
   ## 比如现在我要找第2小，那就是index为1
#arr = [58,26,93,17,77,31,44,55,20,78,109,225,8,10,11,45,87,23]

def findKthMin(arr,k):
    a = partition(arr,0,len(arr)-1)
    while a != k-1:
        if a >k-1:
            a = partition(arr,0,a-1)
        elif a < k-1:
            a = partition(arr,a+1,len(arr)-1)
#    partition(arr[:a+1],0,k-1)
    return arr[a]
#res = findKthMin(arr,7)
#print(res)
## 找第k大，其实就相当于找第(len(arr)-k)小
def findKthMax(arr,k):
    idx = partition(arr,0,len(arr)-1)
    target = len(arr)-k   ## 就这一步转换一下，其他都和找第k小一样
    while idx != target:
        if idx > target:
            idx = partition(arr,0,idx-1)
        elif idx < target:
            idx = partition(arr,idx+1,len(arr)-1)
        
    return arr[idx:]
#res = findKthMax(arr,8)
#print(res)
'''
找到第k大或者第k小后，就对这之后的一段进行quicksort就行了，
大的:arr[k:]
小的:arr[:k+1]
整体复杂度的平均值为O(n),因为要进行quicksort的序列短了很多
'''
