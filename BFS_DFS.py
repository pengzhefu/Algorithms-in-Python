# -*- coding: utf-8 -*-
"""
Created on Sun May  5 03:54:54 2019

@author: pengz
"""

'''
BFS DFS
'''
## first using dict to complete the graph, 里面不用dict是因为不需要权重
graph = {
        "A":["B","C"],
        "B":["A","C","D"],
        "C":["A","B","D","E"],
        "D":["B","C","E","F"],
        "E":["C","D"],
        "F":["D"]
        }

def BFS(graph, s):  ## graph是图, s是起始点
    queue = []   ## 用一个列表模拟队列, 每一次把当前正在走的相邻的点放进队列里,保证每层的顺序
    ret = []
    parent = {}   ## parent是转换成树的结构，key是当前点，value是他的前一个点的值
    parent[s] = None
    queue.append(s)  ## 先把起点放进队列
    while queue != []:
        print(queue)
        print("====================")
        vertex = queue.pop(0)
#        if vertex not in ret:
        ret.append(vertex)
        for point in graph[vertex]:
#            if point not in queue:
            if point in graph and point not in queue:   ## 如果这个点的连接点没被遍历过，也不在之前点的相邻点里
                queue.append(point)   ## 如果都遍历过了, 那最后一个点的所有邻接点都不能放进队列了
                parent[point] = vertex
        del graph[vertex]   ## 遍历这个点就删掉了
#        print(vertex)
    return ret,parent

res,parent = BFS(graph,"A")
    
def DFS(graph, s): ## graph是图, s是起点
    stack = []  ## using a list to act like stack
    ret = []
    stack.append(s)  ## 先把起点放进栈里
    while stack != []:
        print(stack)
        print('================')
        vertex = stack.pop()
        if vertex not in ret:
            ret.append(vertex)   ## 因为每次都会把上一个点的所有邻接点放进去stack,然后这一步再从stack拿出来,
                                    ## 所以其实是邻接的
            for point in graph[vertex]:
                if point in graph and point not in stack:   ## 放入邻接点, 要是没遍历过的和之前不是别人的邻接点
                    stack.append(point)  ## 如果都遍历过了, 那最后一个点的所有邻接点都不能放进队列了
        del graph[vertex]    ## 遍历过的点就删除
    return ret

#res = DFS(graph,"A")
    