# -*- coding: utf-8 -*-
"""
Created on Wed Mar 13 00:04:00 2019

@author: pengz
"""
## 整个binary heap都可以由单个list来实现
class BinHeap_min():  ##这是最小堆，最小值在最前面，
    def __init__(self):
        self.heapList = [0] ##这个0不是root,(应该不是),但是二叉堆的index应该从1开始，不包括这个0
        self.currentSize = 0  ## current size是表示堆的大小
    
## percUp和insert共同组成一个insert方法    
    def percUp(self,i):
        while i // 2 > 0:    ## i//2是找父节点的方法，向下取整。 当i//2 ==0时，说明到了root
                                ## 所以，要先保证有父节点，才进入循环进行比较
          if self.heapList[i] < self.heapList[i // 2]: ##就是把添加的节点和添加后的父节点进行比较，父节点的值要≤子节点的值
             ## 交换的过程，没有用Python的直接交换
             tmp = self.heapList[i // 2]
             self.heapList[i // 2] = self.heapList[i]
             self.heapList[i] = tmp
          i = i // 2  ##向上移一步，到自己的父节点那个位置
          
    def insert(self,k):
        self.heapList.append(k)
        self.currentSize = self.currentSize + 1
        self.percUp(self.currentSize)   ##相当于添加到最后，然后从最后一个开始进行作遍历比较交换
        
## minChild和percDown和delMin共同组成一个delMin方法
    def minChild(self,i):   ##用来找自己左右子节点哪一个较小，返回较小的那一个
        if i * 2 + 1 > self.currentSize:  ##如果都没有右子树的话，直接返回左子树
            return i * 2
        else:
            if self.heapList[i*2] < self.heapList[i*2+1]:
                return i * 2
            else:
                return i * 2 + 1
    
    ## percDown这个函数会从他的起始点i一直遍历完这个i的所有子节点，保证都对了从那个点开始的排序都是对的    
    def percDown(self,i): ##用来向下遍历交换，保证删掉了根节点之后能保证heap的顺序
        while (i * 2) <= self.currentSize:  ##之所以是2*i是因为是binary heap是由完全二叉树表示的，至少有左子树
            mc = self.minChild(i)  ##找到较小子节点的index
            if self.heapList[i] > self.heapList[mc]: ##如果这个父节点的值大于较小的那个子节点，就交换
                                                        ## 所以其实是和较小的那个子树比较交换
                ## 交换的过程，没有用Python的直接交换
                tmp = self.heapList[i]
                self.heapList[i] = self.heapList[mc]
                self.heapList[mc] = tmp
            i = mc
            
    def delMin(self):    ##总结delMin方法就是，先用heap的最后一个把root的覆盖掉，再重新排序依次，向下遍历
        retval = self.heapList[1]  ##因为删掉的肯定是最小的也就是root，所以为1
        self.heapList[1] = self.heapList[self.currentSize] ##然后把Bheap的最后一项放到root的位置，
                                                            ##再用percdown进行遍历调整
        self.currentSize = self.currentSize - 1 ##size -1
        self.heapList.pop()   ##list删掉一项，也是最后一项，反正最后一项也被放到最前面了，其实相当于覆盖了
        self.percDown(1)    ##开始从头遍历调整
        return retval          ##要返回一下删掉的项的值是多少
    
    def buildHeap(self,alist):   ## 复杂度为O(N)
      i = len(alist) // 2      ##从中间的那个节点开始进行排序调整
      self.currentSize = len(alist)
      self.heapList = [0] + alist[:]   ## 就相当于先创造一个乱序的堆，然后从中间的点开始排，直到从root最后再排一遍
                                          ## 这里涉及到一个性质，Python的列表合并就是直接相加
      while (i > 0):
          self.percDown(i)
          i = i - 1
    
bh_min = BinHeap_min()
bh_min.buildHeap([9,6,5,2,3])
print(bh_min.heapList)   ## 显示出heap的正确顺序
print(bh_min.delMin())   ##    
print(bh_min.heapList)
bh_min.insert(8)
print(bh_min.heapList)
print("=============================")

class BinHeap_max():  ##这是最小堆，最小值在最前面，
    def __init__(self):
        self.heapList = [0] ##这个0不是root,(应该不是),但是二叉堆的index应该从1开始，不包括这个0
        self.currentSize = 0  ## current size是表示堆的大小
    
## percUp和insert共同组成一个insert方法    
    def percUp(self,i):
        while i // 2 > 0:    ## i//2是找父节点的方法，向下取整。 当i//2 ==0时，说明到了root
          if self.heapList[i] > self.heapList[i // 2]: ##就是把添加的节点和添加后的父节点进行比较，父节点的值要≥子节点的值
                                                          ## 如果子节点大于父节点了，要交换，一直换到头
             tmp = self.heapList[i // 2]
             self.heapList[i // 2] = self.heapList[i]
             self.heapList[i] = tmp
          i = i // 2
          
    def insert(self,k):
        self.heapList.append(k)
        self.currentSize = self.currentSize + 1
        self.percUp(self.currentSize)   ##相当于添加到最后，然后从最后一个开始进行作遍历比较交换
        
## maxChild和percDown和delMin共同组成一个delMin方法
    def maxChild(self,i):   ##用来找自己左右子节点哪一个较大，返回较大的那一个
        if i * 2 + 1 > self.currentSize:  ##如果都没有右子树的话，直接返回左子树
            return i * 2
        else:
            if self.heapList[i*2] > self.heapList[i*2+1]:
                return i * 2
            else:
                return i * 2 + 1
    
    ## percDown这个函数会从他的起始点i一直遍历完这个i的所有子节点，保证都对了从那个点开始的排序都是对的    
    def percDown(self,i): ##用来向下遍历交换，保证删掉了根节点之后能保证heap的顺序
        while (i * 2) <= self.currentSize:  ##之所以是2*i是因为是binary heap是由完全二叉树表示的，至少有左子树
            mc = self.maxChild(i)  ##找到较大子节点的index
            if self.heapList[i] < self.heapList[mc]: ##如果这个父节点的值小于较大的那个子节点，就交换
                                                        ## 所以其实是和较大的那个子树比较交换
                tmp = self.heapList[i]
                self.heapList[i] = self.heapList[mc]
                self.heapList[mc] = tmp
            i = mc
            
    def delMax(self):    ##总结delMax方法就是，先用heap的最后一个把root的覆盖掉，再重新排序依次，向下遍历
        retval = self.heapList[1]  ##因为删掉的肯定是最大的也就是root，所以为1
        self.heapList[1] = self.heapList[self.currentSize] ##然后把Bheap的最后一项放到root的位置，
                                                            ##再用percdown进行遍历调整
        self.currentSize = self.currentSize - 1 ##size -1
        self.heapList.pop()   ##list删掉一项，也是最后一项，反正最后一项也被放到最前面了，其实相当于覆盖了
        self.percDown(1)    ##开始从头遍历调整
        return retval          ##要返回一下删掉的项的值是多少
    
    def buildHeap(self,alist):  ## 复杂度为O(N)
      i = len(alist) // 2      ##从中间的那个节点开始进行排序调整
      self.currentSize = len(alist)
      self.heapList = [0] + alist[:]   ## 就相当于先创造一个乱序的堆，然后从中间的点开始排，直到从root最后再排一遍
                                          ## 这里涉及到一个性质，Python的列表合并就是直接相加
      while (i > 0):
          self.percDown(i)
          i = i - 1
    
bh_max = BinHeap_max()
bh_max.buildHeap([2,6,9,5,3,4])
print(bh_max.heapList)   ## 显示出heap的正确顺序
print(bh_max.delMax())       
print(bh_max.heapList)