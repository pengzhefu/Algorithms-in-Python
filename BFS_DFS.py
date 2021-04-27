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
    parent = {}   ## parent是转换成树的结构，key是当前点，value是他的前一个点的值，有parent就方便找root到一个点的最小距离
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

# 一种比较基本的针对树结构的DFS, 有其他需求可以再在这个上面添加，参考如下
# https://leetcode.jp/leetcode%E5%B8%B8%E8%A7%81%E7%AE%97%E6%B3%95%E4%B9%8B%E6%B7%B1%E5%BA%A6%E4%BC%98%E5%85%88%E6%90%9C%E7%B4%A2dfs%E8%B6%85%E8%AF%A6%E7%BB%86%E7%99%BD%E8%AF%9D%E8%AE%B2%E8%A7%A3%E4%B8%8A/
def DFS_recur(node):  # node是叶子节点
    if node.leftchild == None and node.rightchild == None:
        return
    if node.leftchild != None:
        DFS_recur(node.leftchild)
    if node.rightchild != None:
        DFS_recur(node.rightchild)
#res,parent = BFS(graph,"A")

## 有parent以后，就可以根据这个parent字典，和我们规定的作为root的点，到其他点的最小距离
#destination = 'F'  ## point of destination
#length = -1
#path = []
#while destination != None:
#    path.append(destination)
#    destination = parent[destination]
#    length += 1

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

'''
BFS升级变成Dijkstra算法，要用到priority queue, 用heapq来模拟priority queue
'''
import heapq
graph_w = {
        "A":{"B":5,"C":1},
        "B":{"A":5,"C":2,"D":7},
        "C":{"A":1,"B":2,"D":4,"E":8},
        "D":{"B":1,"C":4,"E":3,"F":6},
        "E":{"C":8,"D":3},
        "F":{"D":6}
        }
def BFS_Dijk(graph_w,s):   ## s是起始点
    pqueue = []  ## 用列表来模拟priority queue
    ret = []   ## 返回结果的列表
    parent = {s:None}   ## 存储每一个点的距离自己最近的上一个点
    dist = {s:0}   ## 存储距离，距离是起始点s到这个点的最短距离, key是点, value是距离 
    heapq.heappush(pqueue,(dist[s], s))
    while len(pqueue) != 0:
        print(pqueue)
        vertex = heapq.heappop(pqueue)   ## vertex just like (1,"A")
        print(vertex)
        print('=====================')
        if vertex[1] not in ret:   ## 已经放在ret里的说明是已经彻底遍历完的点
            ret.append(vertex[1])
            print(graph_w[vertex[1]]) ## graph_w[vertex[1]] just like {'A':4, 'B':5}
            for point_w in graph_w[vertex[1]]:
                if point_w in graph_w:  ## dict的in搜索要快一点，比list快，是O(1)
                                        ## 这一步是说如果和这个vertex相连的点,还没有被完全遍历过的话
                                        ## point_w是和vertex相连的点
                    '''
                    最重要的就是下面这一部！！！再放进heap的时候应该用的是距离之和！
                    '''
                    heapq.heappush(pqueue, (dist[vertex[1]]+graph_w[vertex[1]][point_w], point_w))  ## 应该是距离之和
                    ## 放进priority queue的时候还不用比较，但是更新到dist和parent字典时候，需要比较，比原来小才更新
                    if point_w not in dist:    ## 这里一定要加一段比较！！！
                        dist[point_w] = dist[vertex[1]]+graph_w[vertex[1]][point_w]
                        parent[point_w] = vertex[1]
                    else:
                        if dist[point_w] > dist[vertex[1]]+graph_w[vertex[1]][point_w]: ## important!!!
                            dist[point_w] = dist[vertex[1]]+graph_w[vertex[1]][point_w]
                            parent[point_w] = vertex[1]
                        else:
                            pass
            del graph_w[vertex[1]]   ## 彻底遍历过的点就删掉
        print('dist is',dist)
        print('=======dist======')
    return ret,dist,parent
a,b,c = BFS_Dijk(graph_w, "A")