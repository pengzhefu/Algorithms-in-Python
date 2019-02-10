# -*- coding: utf-8 -*-
"""
Created on Sun Feb 10 03:30:08 2019

@author: pengz
"""

######### Create a Stack ########## 
class Stack:
     def __init__(self):
         self.items = []

     def isEmpty(self):
         return self.items == []

     def push(self, thing):
         self.items.append(thing)

     def pop(self):
         return self.items.pop()

     def peek(self):
         return self.items[len(self.items)-1]

     def size(self):
         return len(self.items)
     


#######利用stack实现字符串的倒序##########
def revstring(mystr):
    # your code here
    stack1 = Stack()
    str1 = ""
    for chars in mystr:
        stack1.push(chars)
    while not stack1.isEmpty():
        str1 = str1 + stack1.peek()
        stack1.pop()
    return str1

print(revstring('654321'))
#
#
##########利用stack判断括号的匹配########
def ifmatch(mystr):
    stack1 = Stack()
    for chars in mystr:
        if stack1.isEmpty():
            stack1.push(chars)
        else:
            if chars == stack1.peek():
                stack1.push(chars)
            else:
                stack1.pop()
    return stack1.isEmpty()
print(ifmatch('(()))('))
#    
##########利用stack判断多种符号的匹配##################
def parChecker(symbolString):
    s = Stack()
    balanced = True
    index = 0
    while index < len(symbolString) and balanced:
        symbol = symbolString[index]
        if symbol in "([{":
            s.push(symbol)
        else:
            if s.isEmpty():
                balanced = False
            else:
                top = s.pop()
                if not matches(top,symbol):
                       balanced = False
        index = index + 1
    if balanced and s.isEmpty():
        return True
    else:
        return False
#
def matches(open,close):
    opens = "([{"
    closers = ")]}"
    return opens.index(open) == closers.index(close)

print(parChecker('{{([][])}()}'))
print(parChecker('[{()]'))
         
#########10进制转换成2进制###################
def divideBy2(decNumber):
    remstack = Stack()

    while decNumber > 0:
        rem = decNumber % 2  ##如果是转换成别的进制就换这个2
        remstack.push(rem)
        decNumber = decNumber // 2  ####和这个2

    binString = ""
    while not remstack.isEmpty():
        binString = binString + str(remstack.pop())

    return binString

print(divideBy2(42))

######中缀转换成后缀####################
'''

    1.创建一个名为 opstack 的空栈以保存运算符。给输出创建一个空列表。
    2.通过使用字符串方法拆分将输入的中缀字符串转换为标记列表。
    3.从左到右扫描标记列表。
        如果标记是操作数，将其附加到输出列表的末尾。
        如果标记是左括号，将其压到 opstack 上。
        如果标记是右括号，则弹出 opstack，直到删除相应的左括号。将每个运算符附加到输出列表的末尾。
        如果标记是运算符，*，/，+或 - ，将其压入 opstack。但是，首先删除已经在 opstack 中具有更高或相等优先级的任何运算符，并将它们加到输出列表中。
    4.当输入表达式被完全处理时，检查 opstack。仍然在栈上的任何运算符都可以删除并加到输出列表的末尾。

'''
def infixToPostfix(infixexpr):
    prec = {}
    '''规定运算优先级'''
    prec["*"] = 3
    prec["/"] = 3
    prec["+"] = 2
    prec["-"] = 2
    prec["("] = 1
    ##################
    opStack = Stack()
    postfixList = []
    tokenList = infixexpr.split()

    for token in tokenList:
        if token in "ABCDEFGHIJKLMNOPQRSTUVWXYZ" or token in "0123456789":
            postfixList.append(token)
        elif token == '(':
            opStack.push(token)
        elif token == ')':
            topToken = opStack.pop()
            while topToken != '(':
                postfixList.append(topToken)
                topToken = opStack.pop()
        else:
            while (not opStack.isEmpty()) and \
               (prec[opStack.peek()] >= prec[token]):
                  postfixList.append(opStack.pop())
            opStack.push(token)

    while not opStack.isEmpty():
        postfixList.append(opStack.pop())
    return " ".join(postfixList)
print(infixToPostfix("A * B + C * D"))
print(infixToPostfix("( A + B ) * C - ( D - E ) * ( F + G )"))
#
#######计算后缀表达式######
'''

    1.创建一个名为 operandStack 的空栈。
    2.拆分字符串转换为标记列表。
    3.从左到右扫描标记列表。
        如果标记是操作数，将其从字符串转换为整数，并将值压到operandStack。
        如果标记是运算符*，/，+或-，它将需要两个操作数。弹出operandStack 两次。 第一个弹出的是第二个操作数，第二个弹出的是第一个操作数。执行算术运算后，将结果压到操作数栈中。
    4.当输入的表达式被完全处理后，结果就在栈上，弹出 operandStack 并返回值。
#
#'''
def postfixEval(postfixExpr):
    operandStack = Stack()
    tokenList = postfixExpr.split()

    for token in tokenList:
        if token in "0123456789":
            operandStack.push(int(token))
        else:
            operand2 = operandStack.pop()
            operand1 = operandStack.pop()
            result = doMath(token,operand1,operand2)
            operandStack.push(result)
    return operandStack.pop()

def doMath(op, op1, op2):
    if op == "*":
        return op1 * op2
    elif op == "/":
        return op1 / op2
    elif op == "+":
        return op1 + op2
    else:
        return op1 - op2

print(postfixEval('7 8 + 3 2 + /'))