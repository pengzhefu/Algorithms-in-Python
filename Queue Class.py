# -*- coding: utf-8 -*-
"""
Created on Thu Feb  7 23:03:11 2019

@author: UPenn-BU-01
"""
#import numpy as np
#
#s = np.array([[3,4,5],[4,3,2]])
#print("23432")

#for i in range(4):
#    print(i)
#    i = 10
#    print(i)


class Queue: ##列表的末端是front,列表头是rear
    def __init__(self):
        self.items = []
    def isEmpty(self):
        return self.items == []
    def enqueue(self,item):
        self.items.insert(0,item) ##入队的复杂度为O(N)
    def dequeue(self):
        return self.items.pop()
    def size(self):
        return len(self.items)
    
#q = Queue()
#q.enqueue(1)
#q.enqueue(2)
#q.enqueue(12)
#print(q.size())
#print(q.items)

#####模拟烫手山芋###########
def hotPotato(*names,n):
    q = Queue()
    for name in names:
        q.enqueue(name)
    while q.size() > 1:
        num = n
        while num > 0:
            item = q.dequeue()
            q.enqueue(item)
            num = num -1
        q.dequeue()
    print(q.items)
        
    
hotPotato('1','2','3','4','5','6','7','8','9','10',n=3)

############模拟打印机##############
class Printer:
    def __init__(self, ppm):
        self.pagerate = ppm
        self.currentTask = None
        self.timeRemaining = 0

    def tick(self):
        if self.currentTask != None:
            self.timeRemaining = self.timeRemaining - 1
            if self.timeRemaining <= 0:
                self.currentTask = None

    def busy(self):
        if self.currentTask != None:
            return True
        else:
            return False

    def startNext(self,newtask):
        self.currentTask = newtask
        self.timeRemaining = newtask.getPages() * 60/self.pagerate

import random

class Task:
    def __init__(self,time):
        self.timestamp = time
        self.pages = random.randrange(1,21)

    def getStamp(self):
        return self.timestamp

    def getPages(self):
        return self.pages

    def waitTime(self, currenttime):
        return currenttime - self.timestamp
    

def simulation(numSeconds, pagesPerMinute):

    labprinter = Printer(pagesPerMinute)
    printQueue = Queue()
    waitingtimes = []

    for currentSecond in range(numSeconds):

      if newPrintTask():
         task = Task(currentSecond)
         printQueue.enqueue(task)

      if (not labprinter.busy()) and (not printQueue.isEmpty()):
        nexttask = printQueue.dequeue()
        waitingtimes.append(nexttask.waitTime(currentSecond))
        labprinter.startNext(nexttask)

      labprinter.tick()

    averageWait=sum(waitingtimes)/len(waitingtimes)
    print("Average Wait %6.2f secs %3d tasks remaining."%(averageWait,printQueue.size()))

def newPrintTask():
    num = random.randrange(1,181)
    if num == 180:
        return True
    else:
        return False
    

for i in range(10):
      simulation(3600,5)