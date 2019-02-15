# -*- coding: utf-8 -*-
"""
Created on Thu Feb 14 22:57:37 2019

@author: pengz
"""

class Node():
    def __init__(self,initdata):
        self.data = initdata  #初始数据值
        self.next = None   ##最初创建的时候节点的next节点是None

    def getData(self):  #访问数据
        return self.data

    def getNext(self): #访问下一节点
        return self.next

    def setData(self,newdata):#修改数据
        self.data = newdata

    def setNext(self,newnext): #修改下一节点
        self.next = newnext


class OrderedList():
    def __init__(self):
        self.head = None
        
    def isEmpty(self):
        return self.head == None
    
    def size(self):
        current = self.head
        count = 0
        while current != None:
            count += 1
            current = current.getNext()
        return count
    
    def add(self,item):
        temp = Node(item)       ##先创造节点
        if self.head == None:    ##当列表为空的时候，直接添加
            temp.setNext(self.head)
            self.head = temp
        else:
            current = self.head
            previous = None
            while current != None and item > current.getData():##如果current==None，说明要插入的数比任何一个都大
                previous = current
                current = current.getNext()
            if previous != None:
                temp.setNext(current)   
                previous.setNext(temp)
            else:   ##previous == None的话，就说明要插入的数据比现存的任何一个都小，就直接插入
                temp.setNext(current)
                self.head = temp
                
    def search(self,item): ##有序列表的search和无序有点不同，可以不用遍历全部
        stop = False
        found = False
        current = self.head
        while current != None and not stop and not found:
            if current.getData() == item:
                found = True
            elif current.getData() > item:
                stop = True
            else:
                current = current.getNext()
        return found
    
    def pop(self,idx = None):
        current = self.head
        previous = None
        if idx == None:
            length = self.size()
            i = 1
            while i < length:
                previous = current
                current = current.getNext()
                i = i+1
            previous.setNext(current.getNext())
            
        elif idx == 0:
            self.head = current.getNext()
        else:
            i = 0
            while i < idx:
                previous = current
                current = current.getNext()
                i = i+1
            previous.setNext(current.getNext())
    
    def index(self,item):
        idx = 0
        current = self.head
        found = False
        while current != None and not found:
            if current.getData() == item:
                found = True
            else:
                current = current.getNext()
                idx += 1
        if current == None:
            print("not in the list")
        else:
            return idx
        
    def remove(self,item):
        if self.search(item):            
            current = self.head
            previous = None     ##previous一开始设置为None
            found = False
            while not found:
                if current.getData() == item:
                    found = True
                else:                         ##没找到目标item就要往前移previous和current
                    previous = current        ##previsou变成现在这个节点
                    current = current.getNext()  ##current往下移一个
        
            if previous == None:  ##就是第一个head.getData()就是目标item时候，previous就是None,所以修改的就是self.head
                self.head = current.getNext()
            else:
                previous.setNext(current.getNext()) ##previous本来的下一个是current，但现在忽略current直接变成current的下一个
        else:
            print(item," not here")



list2 = OrderedList()
list2.add(12)
list2.add(11)
list2.add(23)
list2.add(50)
print("The length is",list2.size())
print(list2.head.getData())
print(list2.head.getNext().getData())
print(list2.head.getNext().getNext().getData())
print(list2.head.getNext().getNext().getNext().getData())
print("Adding 100")
list2.add(100)
print("The length is",list2.size())
print(list2.head.getData())
print(list2.head.getNext().getData())
print(list2.head.getNext().getNext().getData())
print(list2.head.getNext().getNext().getNext().getData())
print(list2.head.getNext().getNext().getNext().getNext().getData())
print("Adding 1")
list2.add(1)
print("The length is",list2.size())
print(list2.head.getData())
print(list2.head.getNext().getData())
print(list2.head.getNext().getNext().getData())
print(list2.head.getNext().getNext().getNext().getData())
print(list2.head.getNext().getNext().getNext().getNext().getData())
print(list2.head.getNext().getNext().getNext().getNext().getNext().getData())
print("Adding 34")
list2.add(34)
print("The length is",list2.size())
print(list2.head.getData())
print(list2.head.getNext().getData())
print(list2.head.getNext().getNext().getData())
print(list2.head.getNext().getNext().getNext().getData())
print(list2.head.getNext().getNext().getNext().getNext().getData())
print(list2.head.getNext().getNext().getNext().getNext().getNext().getData())
print(list2.head.getNext().getNext().getNext().getNext().getNext().getNext().getData())
print(list2.search(110))
print(list2.index(1))
list2.pop()
print("The length is",list2.size())
print(list2.head.getData())
print(list2.head.getNext().getData())
print(list2.head.getNext().getNext().getData())
print(list2.head.getNext().getNext().getNext().getData())
print(list2.head.getNext().getNext().getNext().getNext().getData())
print(list2.head.getNext().getNext().getNext().getNext().getNext().getData())
list2.pop(0)
list2.pop(1)
print("The length is",list2.size())
print(list2.head.getData())
print(list2.head.getNext().getData())
print(list2.head.getNext().getNext().getData())
print(list2.head.getNext().getNext().getNext().getData())
print(list2.isEmpty())
list2.remove(23)
print("The length is",list2.size())
print(list2.head.getData())
print(list2.head.getNext().getData())
print(list2.head.getNext().getNext().getData())