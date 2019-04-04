# -*- coding: utf-8 -*-
"""
Created on Thu Mar 14 18:05:01 2019

@author: pengz
"""
## 先定义一个tree node，才能组成tree
class TreeNode():
    def __init__(self,key,val,left=None,right=None,
                                       parent=None):   ## 一开始是root，默认没有父节点，没有左右子节点
        self.key = key
        self.payload = val
        self.leftChild = left
        self.rightChild = right
        self.parent = parent

    def hasLeftChild(self):
        return self.leftChild

    def hasRightChild(self):
        return self.rightChild
    
    def isLeftChild(self):
        return self.parent and self.parent.leftChild == self
    
    def isRightChild(self):
        return self.parent and self.parent.rightChild == self
    
    def isRoot(self):
        return not self.parent
    
    def isLeaf(self):
        return not (self.rightChild or self.leftChild)
    
    def hasAnyChildren(self):
        return self.rightChild or self.leftChild
    
    def hasBothChildren(self):
        return self.rightChild and self.leftChild
    
    def replaceNodeData(self,key,value,lc,rc):
        self.key = key
        self.payload = value
        self.leftChild = lc
        self.rightChild = rc
        if self.hasLeftChild():
            self.leftChild.parent = self   ##就是新的这个node的子节点的父节点要是自己
        if self.hasRightChild():
            self.rightChild.parent = self  ##就是新的这个node的子节点的父节点要是自己
            
class BinarySearchTree():

    def __init__(self):
        self.root = None
        self.size = 0

    def length(self):
        return self.size

    def __len__(self):
        return self.size

    def __iter__(self):
        return self.root.__iter__()
    
    def put(self,key,val):    ##  put(插入)要调用_put函数
                                ## put的遍历是从树的root开始，从上到下来比较
        if self.root:   ## 如果当前有节点存在(树有root,不是空的)，那就用_put去比较
            self._put(key,val,self.root)
        else:   ## 如果当前没有节点了(树没有root，是空的),那就是在这里插入
            self.root = TreeNode(key,val)
        self.size = self.size + 1

    def _put(self,key,val,currentNode):     
        if key < currentNode.key:    ## 如果小于当前节点，
            if currentNode.hasLeftChild():    ## 如果存在左子节点，就去和左子节点比较
                   self._put(key,val,currentNode.leftChild)
            else:   ## 小于当前节点而且当前节点没有左子节点的话，
                   currentNode.leftChild = TreeNode(key,val,parent=currentNode)   ## 插入到当前节点的左子节点
        else:   ## 如果大于当前节点
            if currentNode.hasRightChild():  ## 如果存在右子节点
                   self._put(key,val,currentNode.rightChild)  ## 继续和右子节点比较
            else:
                   currentNode.rightChild = TreeNode(key,val,parent=currentNode)
                   
    def __setitem__(self,k,v):
        self.put(k,v)
    

    ## 寻找节点    
    def get(self,key):
        if self.root:
            res = self._get(key,self.root)   ## 从root开始找
            if res:
                   return res.payload
            else:
                   return None
        else:
            return None
    
    def _get(self,key,currentNode):
        if not currentNode:
            return None
        elif currentNode.key == key:
            return currentNode
        elif key < currentNode.key:
            return self._get(key,currentNode.leftChild)
        else:
            return self._get(key,currentNode.rightChild)
    
    def __getitem__(self,key):
        return self.get(key)
    
    def __contains__(self,key):
       if self._get(key,self.root):
           return True
       else:
           return False
    ## 删除节点
    def delete(self,key):   ## delete方法要调用remove方法，remove才是真正在删除     
        ## delete方法主要是确认树的长度，防止出错
       if self.size > 1:
          nodeToRemove = self._get(key,self.root)   ## 先根据输入的key找到node的位置
          if nodeToRemove:
              self.remove(nodeToRemove)
              self.size = self.size-1
          else:
              raise KeyError('Error, key not in tree')
       elif self.size == 1 and self.root.key == key:  ##树就只有root时
          self.root = None
          self.size = self.size - 1
       else:
          raise KeyError('Error, key not in tree')
    
    def __delitem__(self,key):
        self.delete(key)
        
    '''
    1.如果节点有右子节点，则后继节点是右子树中的最小的键。
    2.如果节点没有右子节点并且是父节点的左子节点，则父节点是后继节点。
    3.如果节点是其父节点的右子节点，并且它本身没有右子节点，则此节点的后继节点是其父节点的后继节点，不包括此节点。
    '''
    def spliceOut(self):
       if self.isLeaf():
           if self.isLeftChild():
                  self.parent.leftChild = None
           else:
                  self.parent.rightChild = None
       elif self.hasAnyChildren():
           if self.hasLeftChild():
                  if self.isLeftChild():
                     self.parent.leftChild = self.leftChild
                  else:
                     self.parent.rightChild = self.leftChild
                  self.leftChild.parent = self.parent
           else:
                  if self.isLeftChild():
                     self.parent.leftChild = self.rightChild
                  else:
                     self.parent.rightChild = self.rightChild
                  self.rightChild.parent = self.parent

    def findSuccessor(self):    ## 找后继节点
      succ = None
      if self.hasRightChild():
          succ = self.rightChild.findMin()
      else:
          if self.parent:
                 if self.isLeftChild():
                     succ = self.parent
                 else:
                     self.parent.rightChild = None
                     succ = self.parent.findSuccessor()
                     self.parent.rightChild = self
      return succ

    def findMin(self):
      current = self
      while current.hasLeftChild():
          current = current.leftChild
      return current

    def remove(self,currentNode):
         if currentNode.isLeaf(): #leaf
           if currentNode == currentNode.parent.leftChild:
               currentNode.parent.leftChild = None
           else:
               currentNode.parent.rightChild = None
         elif currentNode.hasBothChildren(): #interior
           succ = currentNode.findSuccessor()
           succ.spliceOut()
           currentNode.key = succ.key
           currentNode.payload = succ.payload

         else: # this node has one child
           if currentNode.hasLeftChild():
             if currentNode.isLeftChild():
                 currentNode.leftChild.parent = currentNode.parent
                 currentNode.parent.leftChild = currentNode.leftChild
             elif currentNode.isRightChild():
                 currentNode.leftChild.parent = currentNode.parent
                 currentNode.parent.rightChild = currentNode.leftChild
             else:
                 currentNode.replaceNodeData(currentNode.leftChild.key,
                                    currentNode.leftChild.payload,
                                    currentNode.leftChild.leftChild,
                                    currentNode.leftChild.rightChild)
           else:
             if currentNode.isLeftChild():
                 currentNode.rightChild.parent = currentNode.parent
                 currentNode.parent.leftChild = currentNode.rightChild
             elif currentNode.isRightChild():
                 currentNode.rightChild.parent = currentNode.parent
                 currentNode.parent.rightChild = currentNode.rightChild
             else:
                 currentNode.replaceNodeData(currentNode.rightChild.key,
                                    currentNode.rightChild.payload,
                                    currentNode.rightChild.leftChild,
                                    currentNode.rightChild.rightChild)
    
