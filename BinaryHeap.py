# -*- coding: utf-8 -*-
"""
Created on Wed Mar 13 00:04:00 2019

@author: pengz
"""
## 整个binary heap都可以由单个list来实现
class BinHeap():
    def __init__(self):
        self.heapList = [0] ##这个0不是root,(应该不是),但是二叉堆的index应该从1开始，不包括这个0
        self.currentSize = 0  ## current size是表示堆的大小
    
## percUp和insert共同组成一个insert方法    
    def percUp(self,i):
        while i // 2 > 0:    ## i//2是找父节点的方法，向下取整。 当i//2 ==0时，说明到了root
          if self.heapList[i] < self.heapList[i // 2]: ##就是把添加的节点和添加后的父节点进行比较，父节点的值要≤子节点的值
             tmp = self.heapList[i // 2]
             self.heapList[i // 2] = self.heapList[i]
             self.heapList[i] = tmp
          i = i // 2
          
    def insert(self,k):
        self.heapList.append(k)
        self.currentSize = self.currentSize + 1
        self.percUp(self.currentSize)   ##相当于添加到最后，然后从最后开始进行作遍历比较交换
        
## minChild和percDown和delMin共同组成一个delMin方法
    def minChild(self,i):   ##用来找自己左右子节点哪一个较小，返回较小的那一个
        if i * 2 + 1 > self.currentSize:  ##如果都没有右子树的话，直接返回左子树
            return i * 2
        else:
            if self.heapList[i*2] < self.heapList[i*2+1]:
                return i * 2
            else:
                return i * 2 + 1
        
    def percDown(self,i): ##用来向下遍历交换，保证删掉了根节点之后能保证heap的顺序
        while (i * 2) <= self.currentSize:  ##之所以是2*i是因为是binary heap是由完全二叉树表示的，至少有左子树
            mc = self.minChild(i)  ##找到较小子节点的index
            if self.heapList[i] > self.heapList[mc]: ##如果这个父节点的值大于较小的那个子节点，就交换
                                                        ## 所以其实是和较小的那个子树比较交换
                tmp = self.heapList[i]
                self.heapList[i] = self.heapList[mc]
                self.heapList[mc] = tmp
            i = mc
            
    def delMin(self):
        retval = self.heapList[1]  ##因为删掉的肯定是最小的也就是root，所以为1
        self.heapList[1] = self.heapList[self.currentSize] ##然后把Bheap的最后一项放到root的位置，
                                                            ##再用percdown进行遍历调整
        self.currentSize = self.currentSize - 1 ##size -1
        self.heapList.pop()   ##list删掉一项，也是最后一项，反正最后一项也被放到最前面了，其实相当于覆盖了
        self.percDown(1)    ##开始从头遍历调整
        return retval          ##要返回一下删掉的项的值是多少

