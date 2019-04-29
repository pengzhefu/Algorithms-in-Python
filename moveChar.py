# -*- coding: utf-8 -*-
"""
Created on Sun Apr 28 22:14:05 2019

@author: pengz
"""
'''
这题目是模拟一道题：给一个字符串，怎么把他变成一个小写字母在前，大写字母在后的形式，并且保持原始顺序。
我改成一个列表，怎么把一个列表改成字母在前，数字在后的形式；
方法就是用两个指针，每一次都找到这个列表里最末尾的字母，然后从这个字母往前去找最近的那个数字（或者从之前的数字之前找也行），
找到以后，在这两个指针之间，进行item的往前移，把那个数字插入到最后一个字母在的位置就行了。注意循环条件是要and了
'''
def moveChar(s:list):   ## 模拟成一个列表里,字母在前,数字在后
    i = len(s)-1  ## 从后往前找第一个是字母的位置
    j = len(s)-1  ## 然后从字母往前找数字,
    if i < 0:
        return []
    if j < 0:
        return s
    while i >=0 and j >=0:
        if s[i].isdigit() == True:
            i = i-1
            continue
        if j >=i:
            j = i-1
        while j>=0 and s[j].isalpha() == True:
            j = j-1
        tmp = s[j]
        for index in range(j,i):  ## j更靠前，这题是要把后一个变成前一个，所以是从前往后遍历
            s[index] = s[index+1]
        s[i] = tmp
        i = i-1
        j = j-1


s = ['3','a','b','c','4','5','d','z']
moveChar(s)

        
            