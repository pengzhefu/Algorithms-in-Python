# -*- coding: utf-8 -*-
"""
Created on Wed Feb 13 00:27:23 2019

@author: pengz
"""

####################Deque##################
        ####尾部是front,头部是rear#########
class Deque:
    def __init__(self):
        self.items = []
    
    def isEmpty(self):
        return self.items == []
    
    def addFront(self,item):
        self.items.append(item)
        
    def addRear(self,item):
        self.items.insert(0,item)
        
    def removeFront(self):
        return self.items.pop()
    
    def removeRear(self):
        return self.items.pop(0)
    
    def size(self):
        return len(self.items)
    

deque1 = Deque()
deque1.addFront('123')
deque1.addRear('345')
print(deque1.items)
deque1.addFront('678')
print(deque1.items)
deque1.addFront('000')
print(deque1.items)
deque1.removeFront()
print(deque1.items)
deque1.removeRear()
print(deque1.items)


#############Palindrome-Checker(回文检查)##################
def palchecker(word):
    chardeque = Deque()
    for char in word:
        chardeque.addFront(char)
    stillEqual = True

    while chardeque.size() > 1 and stillEqual: ####这个长度大于1是key,包含了奇数和偶数的可能,类似于大于等于2
        first = chardeque.removeFront()
        last = chardeque.removeRear()
        if first != last:
            stillEqual = False

    return stillEqual
        
print(palchecker('abd'))
print(palchecker("lsdkjfskf"))
print(palchecker("radar"))