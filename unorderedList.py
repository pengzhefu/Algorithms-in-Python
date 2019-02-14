# -*- coding: utf-8 -*-
"""
Created on Thu Feb 14 00:52:15 2019

@author: pengz
"""

##############Node(节点)#############
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
        
#temp = Node(93)
#print(temp.getData())
#print(temp.getNext())

########生成无序列表(unorderedlist)###########
class UnorderedList():

    def __init__(self):
        self.head = None
        
    def isEmpty(self):
        return self.head == None
    
    def add(self,item):
        temp = Node(item)       ##先创造节点
        ###下面这两步一定不能搞混
        temp.setNext(self.head)   ## 然后让现在的head指向的对象变成刚刚创造的节点的下一指向对象
        self.head = temp    ##然后让现在的head指向的对象变成刚刚创造的节点
        
    def size(self):
        current = self.head
        count = 0   ##一开始要是0这个很重要，要数一次才能+1
        while current != None:
            count = count + 1
            current = current.getNext()  ##先+1,再往下走
    
        return count
    
    def search(self,item):  
        current = self.head    ##遍历一开始的current都要从head开始
        found = False
        while current != None and not found:  ##如果到了最后一个节点,那么getNext()之后就是None，就会跳出while循环
            if current.getData() == item:
                found = True
            else:
                current = current.getNext()
    
        return found
    
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
    
    def insert(self,idx,item):
        current = self.head
        previous = None
        temp = Node(item)
        if idx == 0:
            temp.setNext(self.head)
            self.head = temp
        else:
            for i in range(idx):
                previous  = current
                current = current.getNext()
            temp.setNext(current)
            previous.setNext(temp)

    
    def append(self,item):
        temp = Node(item)
        current = self.head
        while current.getNext() != None:
            current = current.getNext()
        temp.setNext(current.getNext())
        current.setNext(temp)

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


mylist = UnorderedList()
print(mylist.size())
mylist.add(31)
print("Now the first point is: ",mylist.head.getData())
print("The next after last point is: ",mylist.head.getNext()) ##31这个节点下一个指向的就是None,所以最后一个节点对象 Node.getNext()跟的就是None
mylist.add(62)
mylist.add(30)
mylist.add(624)
mylist.add(343)
mylist.add(698)
print('The size of list is',mylist.size())
print("The second point is : ",mylist.head.getNext().getData())
print(mylist.search(31))
print(mylist.search(1))
mylist.remove(32)
print('The size of list is',mylist.size())
print(mylist.index(698))
mylist.insert(0,100)
print('The size of list is',mylist.size())
print("Now the first point is: ",mylist.head.getData())
mylist.insert(1,101)
print('The size of list is',mylist.size())
print("Now the second point is: ",mylist.head.getNext().getData())

print("*******************************************************")

list1 = UnorderedList()
list1.add(100)
list1.add(200)
list1.add(300)
print("Initial size is",list1.size())
list1.insert(1,22.4)
print("After inserting Size is",list1.size())
print(list1.head.getData())
print(list1.head.getNext().getData())
print(list1.head.getNext().getNext().getData())
print(list1.head.getNext().getNext().getNext().getData())
list1.pop(1)
print("After popping Size is",list1.size())
print(list1.head.getData())
print(list1.head.getNext().getData())
print(list1.head.getNext().getNext().getData())
list1.append(400)
print("After appending Size is",list1.size())
print(list1.head.getData())
print(list1.head.getNext().getData())
print(list1.head.getNext().getNext().getData())
print(list1.head.getNext().getNext().getNext().getData())