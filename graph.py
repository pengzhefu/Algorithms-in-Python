# -*- coding: utf-8 -*-
"""
Created on Tue Apr  9 16:24:05 2019

@author: pengz
"""

class Vertex():    ## 一个vertex就是一个顶点，他的key就相当于他的号码他的id
    def __init__(self,key):
        self.id = key
        self.connectedTo = {}    ## 他连接的点以及权重，用dict表示

    def addNeighbor(self,nbr,weight=0):   ## weight如果没写默认等于0，所以添加的时候要写上
        self.connectedTo[nbr] = weight

    def __str__(self):
        return str(self.id) + ' connectedTo: ' + str([x.id for x in self.connectedTo])   ## 就以list形式返回这个dict里的每个key的id

    def getConnections(self):    ## 找出这个点都和那些点连接，只要keys就只是需要点，不需要权重
        return self.connectedTo.keys()

    def getId(self):
        return self.id

    def getWeight(self,nbr):
        return self.connectedTo[nbr]   ## 返回dict[key]
    
    
class Graph():
    def __init__(self):
        self.vertList = {}     ## 整个邻接表用dict来表示
        self.numVertices = 0

    def addVertex(self,key):
        self.numVertices = self.numVertices + 1
        newVertex = Vertex(key)
        self.vertList[key] = newVertex
        return newVertex

    def getVertex(self,n):
        if n in self.vertList:   ## 这里是查看的key,直接的in是看key而不是看value
            return self.vertList[n]
        else:
            return None

    def __contains__(self,n):
        return n in self.vertList

    def addEdge(self,f,t,cost=0):    ## f是起点，t是终点, cost就是weight
        if f not in self.vertList:     ## 如果f不在里面，就先添加
            nv = self.addVertex(f)     ## 这里用一个nv的变量是为了保证添加以后不跳出函数
        if t not in self.vertList:     ## 如果t不在里面，就先添加
            nv = self.addVertex(t)
        self.vertList[f].addNeighbor(self.vertList[t], cost)    ## 然后就利用顶点自身添加neighbor的函数

    def getVertices(self):
        return self.vertList.keys()

    def __iter__(self):
        return iter(self.vertList.values())
    
g = Graph()
for i in range(5):
    g.addVertex(i)
print(g.numVertices)
#print(g.vertList)
g.addEdge(0,1,5)
g.addEdge(0,4,3)
g.addEdge(1,3,1)
print(g.getVertices())

## 展示一下已经有所连接的点
for v in g:
    print(v)
## 第二种
for v in g:
    for w in v.getConnections():    ## 这里拿到的v和w都是一个实例instance，要得到他的信息需要用getId这个函数
        print(v.getId(),w.getId())  
        
