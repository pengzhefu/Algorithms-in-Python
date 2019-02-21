# -*- coding: utf-8 -*-
"""
Created on Thu Feb 21 13:12:40 2019

@author: pengz
"""

class HashTable():
    def __init__(self):
        self.size = 11   ##HashTable的大小尽量是prime number
        self.slots = [None] * self.size
        self.data = [None] * self.size
    
    def hashfunction(self,key,size):
        return key%size

    def rehash(self,oldhash,size): ##采用线性探测的方法进行rehash
        return (oldhash+1)%size
    
    def put(self,key,data):
      hashvalue = self.hashfunction(key,len(self.slots)) ##算出key应该是第几个槽
    
      if self.slots[hashvalue] == None: ##如果key对应的槽是空的，就把key放进slot的列表，data放进data列表
        self.slots[hashvalue] = key   
        self.data[hashvalue] = data
      else: ##如果对应的槽不是空的，那就要重新找槽或者看看占着槽的key是不是要放的key
        if self.slots[hashvalue] == key: ##占着现在这个槽的key和我们想要放的key是一样的
          self.data[hashvalue] = data  #replace，那么就直接把data替换了
        else:  ##如果key不一样
          nextslot = self.rehash(hashvalue,len(self.slots))
          while self.slots[nextslot] != None and \
                          self.slots[nextslot] != key:  ##直到找到空的槽或者发现新的槽的key和要放的key是一样的
            nextslot = self.rehash(nextslot,len(self.slots))
    
          if self.slots[nextslot] == None: ##找到空的槽了
            self.slots[nextslot]=key
            self.data[nextslot]=data
          else:  ##如果拿到的新的slot有key，而且和我们要放的key一样，那么就直接把data替换了
            self.data[nextslot] = data #replace
    
    def get(self,key): ##通过key来找data
      startslot = self.hashfunction(key,len(self.slots))
    
      data = None
      stop = False
      found = False
      position = startslot
      while self.slots[position] != None and  \
                           not found and not stop:   ##循环的中止条件为遇到了一个空槽，或者是找到了，或者是找了一整个table循环了，
         if self.slots[position] == key:
           found = True
           data = self.data[position]
         else:
           position=self.rehash(position,len(self.slots))
           if position == startslot:  ##找了一整个table循环了
               stop = True
      return data
    
    def __getitem__(self,key):  ##重载列表的方法，让这个方法相当于调用函数
        return self.get(key)
    
    def __setitem__(self,key,data):  ##重载列表的方法，让这个方法相当于调用函数，也能通过索引进行插入或者查找
        self.put(key,data)


H = HashTable()
#print(H.slots)
H[54]="cat"
H[26]="dog"
H[93]="lion"
H[17]="tiger"
print(H.slots)
print(H.data)