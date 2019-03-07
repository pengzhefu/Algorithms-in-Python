# -*- coding: utf-8 -*-
"""
Created on Wed Feb 27 01:25:26 2019

@author: pengz
"""

###########Trees############
   ######用列表表示树########
myTree = ['a',   #root
      ['b',  #left subtree
       ['d', [], []],
       ['e', [], []] ],
      ['c',  #right subtree
       ['f', [], []],
       [] ]
     ]
#print(myTree)
#print('left subtree = ', myTree[1])
#print('root = ', myTree[0])
#print('right subtree = ', myTree[2])


def BinaryTree(r):
    return [r, [], []]  ##跟r同一个level，紧贴着r后面的逗号的括号里的内容，就是左子树和有子树的内容
                        ##一般一个点后面会跟两个list:(a,[],[])这是一个完整的节点，说明这个节点没有子节点，为空，
                        ##但是空的也要把[]带上
#print(BinaryTree('a')[2])
def insertLeft(root,newBranch): ##root可以是你要插进去的那个Tree
                                ##这个方法是往离你要插的点的下一层插一个点（左或右，这个是左）
    t = root.pop(1)
    if len(t) > 1:
        root.insert(1,[newBranch,t,[]]) ##原来的点的左子树（包括原来那个点本身）变成新加上去的点的左子树
    else:
        root.insert(1,[newBranch, [], []]) ##没有的话就加上一个
    return root ##root其实就是整个tree

def insertRight(root,newBranch):   ##just like the insertleft
    t = root.pop(2)
    if len(t) > 1:
        root.insert(2,[newBranch,[],t])
    else:
        root.insert(2,[newBranch,[],[]])
    return root

def getRootVal(root): 
    return root[0]

def setRootVal(root,newVal): ##更改根节点的值
    root[0] = newVal

def getLeftChild(root):
    return root[1]

def getRightChild(root):
    return root[2]


#a = BinaryTree('a')
#print(a)
#print(a[0])
#b= insertLeft(a,'b')
#print(b)
#print(b[0])
#print(b[1])
#print(b[2])
#c = insertRight(b,'c')
#print(c)
#print(c[1])
#print(c[2])
#d= insertLeft(c,'d')
#print(d)
#print(d[1])
#print(d[2])
#e = insertRight(d,'e')
#print(e)
#print(e[1])
#print(e[2])
#f = insertRight(a[1],'f')  ##这样相当于给d点添加一个右节点f
#print(a)
#print(a[1][1][0])   ##打印出a的左节点的左节点的不带子点，相当于b
#print(a[1][2])   ##打印出a的左节点的右节点带上子点，相当于f
#print(a[2][0])   ##打印出a的右节点的唯一的点不带子点，相当于e
#print(a[2][2])   ##打印出a的右节点的右节点带上子点，相当于c
#g = insertLeft(a[2],'g') ##给e点添加一个左节点g
#print(a)
#o = insertRight(a[2][1],'o') ##给g点添加一个左节点o
#print(a)
#t = insertLeft(a[1],'t')
#print(a)
#print('#######################################')
#print(getLeftChild(a[2]))
#print(getRootVal(d))

'''用节点表示树'''
####用节点表示树回非常像用节点表示ordered/unordered list
class BinaryTree1():
    def __init__(self,rootObj):
        self.rootObj = rootObj
#        self.key = rootObj    ##用节点的名称作为root的value
        self.leftChild = None
        self.rightChild = None
        
        
        '''插入左子树和右子树有点像在ordered/unordered list里的头插入点'''
    def insertLeft(self,newNode):  
        if self.leftChild == None:
            self.leftChild = BinaryTree1(newNode)
        else:##还是一样的，如果本来左子树有东西，就把要插的点放在离根最接近的地方，原来的左子树作为新的点的左子树
            t = BinaryTree1(newNode)
            t.leftChild = self.leftChild
            self.leftChild = t
            
    def insertRight(self,newNode):
        if self.rightChild == None:
            self.rightChild = BinaryTree1(newNode)
        else:
            t = BinaryTree1(newNode)   ##先创造要插入的点的树的对象
            t.rightChild = self.rightChild  ##然后把已经有的作为要插入的点的右子树
            self.rightChild = t ##然后在根部插入新插入的点
            
    def getRightChild(self):
        return self.rightChild

    def getLeftChild(self):
        return self.leftChild
    
    def setRootVal(self,obj):
        self.rootObj = obj
    
    def getRootVal(self):
        return self.rootObj

#Tree = BinaryTree1('a')
#print(Tree.leftChild)
#print(Tree.getRootVal())
#
#Tree.insertLeft('c')
##print(Tree.leftChild)
#print(Tree.getLeftChild().getRootVal())   
#print('==================================')
#Tree.insertLeft('b')
#print(Tree.getLeftChild().getRootVal())  
#print(Tree.getLeftChild().getLeftChild().getRootVal())  
#print('==================================')
#Tree.getLeftChild().insertLeft('d') ##在a（根节点）的下一个左节点插入一个左节点d
#print(Tree.getLeftChild().getRootVal())  
#print(Tree.getLeftChild().getLeftChild().getRootVal())   
#print(Tree.getLeftChild().getLeftChild().getLeftChild().getRootVal())

'''树的遍历'''
###Preorder pass

## 递归版
def preorder(tree):   ##其实递归的里面就对三种顺序解释很清楚
                        ## 先序就是先根，然后再左子树，左完了再右
    if tree:
        print(tree.getRootVal())
        preorder(tree.getLeftChild())
        preorder(tree.getRightChild())
## 非递归版
'''
1. 使用列表保存结果；
2. 使用栈（列表实现）存储结点； ##这个第二步是重点，要用栈来保存我们已经遍历的节点，然后直到这个节点的左子树为空，我们在看右子树
3. 当根结点存在，保存结果，根结点入栈；
4. 将根结点指向左子树；
5. 根结点不存在，栈顶元素出栈，并将根结点指向栈顶元素的右子树；
6. 重复步骤3-6，直到栈空。
'''
def preorderTraversal(root):
    """
    :type root: TreeNode
    :rtype: List[int]
    """
    ret = []
    stack = []
    while root or stack:   ##根节点不为空，就是整个的起始条件
                            ##但后面只要还有没遍历完的
                            
                            ###也就是说，root为None但是stack不为空的时候，就会进入 if stack,回到父节点进行查看右子树
                            
        while root:         ##有根节点的时候，就一直进行这个循环
            ret.append(root.getRootVal)  ##把根节点的值存在ret列表里
            stack.append(root)    ##然后把这个已经遍历了的root存下来放stack里，可能后面还要用
            root = root.getLeftChild()      ##然后去看这个root的左子树的根节点
            
        if stack: ##直到上面的发现没有左子树了，就来找父节点（刚刚遍历的那个点上面的点）的右子树
                    ##此时，root = None
            t = stack.pop()
            root = t.getRightChild()
    return ret ##最后列表里面的元素顺序就是先序的顺序

###Inorder Pass
## 递归版
def inorder(tree):
  if tree != None:
      inorder(tree.getLeftChild())
      print(tree.getRootVal())
      inorder(tree.getRightChild())

##非递归版      
def inorderTraversal(root):
    """
    :type root: TreeNode
    :rtype: List[int]
    """
    ret = []    ##返回中序顺序结果
    stack = []  ##用来存节点
    while root or stack:   ##根节点不为空，就是整个的起始条件
                            ##但后面只要还有没遍历完的点，就会继续循环遍历
                            ###也就是说，root为None但是stack不为空的时候，就会进入 if stack,回到父节点进行查看右子树
                            
        while root:         ##有根节点的时候，就一直进行这个循环
            stack.append(root)
            root = root.getLeftChild()
        if stack: ##直到上面的发现没有左子树了，就把这个结果存下来，并且找这个点的右子树
                    ##此时root = None
            t = stack.pop()
            ret.append(t.getRootVal())   ##和先序最大的不同就是，直到这个点(root)没有左子树了，才把这个点(root)存在结果里
            root = t.getRightChild()
    return ret ##最后列表里面的元素顺序就是中序的顺序

##Postorder Pass
## 递归版
def postorder(tree):
    if tree != None:
        postorder(tree.getLeftChild())
        postorder(tree.getRightChild())
        print(tree.getRootVal())
        
## 非递归版,后序的比中序和先序都难很多
        ##所以采用了一种逆序版本，就是先把逆序顺序中最后的存下来
        ##但是！！！！！因为后序就相当于把先序的根左右变成根右左，然后再倒过来，所以改一下先序的，再逆输出就行了
def postorderTraversal(root):
    """
    :type root: TreeNode
    :rtype: List[int]
    """
    ret = []    ##返回中序顺序结果
    stack = []  ##用来存节点
    while root:
        ret.append(root.getRotVal())
        stack.append(root)
        root.getRightChild()##这里和先序反过来，先去找左子树
    if stack:
        t = stack.pop()
        root = t.getLeftChild() ##这里也和先序反过来，右边找完了再去找左边
    ret.reverse()        ##因为是逆序，所以要反过来
    return ret 