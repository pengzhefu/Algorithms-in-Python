# -*- coding: utf-8 -*-
"""
Created on Mon Apr 29 00:28:56 2019

@author: pengz
"""
## 用了动态规划的思想,实现求一个字符串，要最少删掉多少个字符才能构成回文
'''
第一种思路就是申请s2变量，使得s2是s1的反转，如果是回文串的话，那么就等价于求s2和s1的LCS(最大公共子序列，不是子串，不用连续)，
例如s1=abca,s2=acba,公共子串的长度为3（aba ,aca），所以需要删除的字符串个数就是4-3=1。
'''

## 现在写一个可以求两个字符之间的最大子序列长度的DP,写好以后可以直接调用,可以不需要这个mat_c矩阵
def findLCS(a,b):
    num_a = len(a) ## 构造的矩阵的长宽，是实际个数的加1
    num_b = len(b)   ## len(b)+1是长度，len(a)+1是宽度
    mat_l = [[0 for i in range(num_b+1)] for i in range(num_a+1)]  ##记录长度的矩阵
    mat_c = [[0 for i in range(num_b+1)] for i in range(num_a+1)]  ##记录选择方向的矩阵,用来输出字符串
    ## 矩阵的遍历生成是一行一行来的
    for i in range(num_a):   ## i是宽度(高)
        for j in range(num_b):   ## j是长度(横坐标)
            if a[i] == b[j]:
                mat_l[i+1][j+1] = mat_l[i][j] + 1
                mat_c[i+1][j+1] = 'match'
            else:
                mat_l[i+1][j+1] = max(mat_l[i][j+1],mat_l[i+1][j])
                if mat_l[i+1][j] > mat_l[i][j+1]:   ## 这个相当于选择[i,j-1]的那个
                    mat_c[i+1][j+1] = 'left'
                else:
                    mat_c[i+1][j+1] = 'up'
    ## 可以先把最大长度输出了,最大长度就是长度矩阵的最右下角
    maxlength = mat_l[num_a][num_b]  ## 注意长宽高,num_a是高度(宽度),num_b才是矩阵的一行的长度
    x = num_a  ## x在这里相当于纵坐标，因为会先看是第几个列表，再看是里面的哪一个
    y = num_b  ## y才是横坐标
    tmp_list = []
    while mat_c[x][y] !=0:
        tmp = mat_c[x][y]
        if tmp == 'match':
            tmp_list.append(a[x-1])
            x = x-1
            y = y-1
        elif tmp == 'up':    
            x = x-1
        elif tmp == 'left':
            y = y-1
    tmp_list.reverse()
    ret = ''
    for item in tmp_list:
        ret = ret+item
    return maxlength,ret

a,b= findLCS('adfg','abcdfga')