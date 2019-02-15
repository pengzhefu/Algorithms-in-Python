# -*- coding: utf-8 -*-
"""
Created on Fri Feb 15 01:58:51 2019

@author: pengz
"""

class Stack():
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


'''递归(Recursion)'''
def listsum(numList):
   if len(numList) == 1:
        return numList[0]
   else:
        return numList[0] + listsum(numList[1:])

print(listsum([1,3,5,7,9,11,13,15]))

def fact(n):
    if n <= 1:
        return n
    else:
        return n*fact(n-1)
    
print(fact(5))

#####字符串逆序########
def reverse(s):
    if len(s) <= 1:
        return s
    else:
        return s[-1] + reverse(s[:-1])
print(reverse('iloveu'))

######回文检查#######
def is_palindrome(s):
    match = True
    if len(s) <= 1:
        return match
    else:
        if s[0] == s[-1]:
            return is_palindrome(s[1:-1])
        else:
            match = False
    return match

print(is_palindrome('12521'))

rStack = Stack()

#####基数转换######（利用栈帧）
def toStr(n,base):
    convertString = "0123456789ABCDEF"
    while n > 0:
        if n < base:
            rStack.push(convertString[n])
        else:
            rStack.push(convertString[n % base])
        n = n // base
    res = ""
    while not rStack.isEmpty():
        res = res + str(rStack.pop())
    return res

print(toStr(1453,16))

##########动态规划#########
def dpMakeChange(coinValueList,change,minCoins,coinsUsed):
   for cents in range(change+1):
      coinCount = cents
      newCoin = 1
      for j in [c for c in coinValueList if c <= cents]:
            if minCoins[cents-j] + 1 < coinCount:
               coinCount = minCoins[cents-j]+1
               newCoin = j
      minCoins[cents] = coinCount
      coinsUsed[cents] = newCoin
   return minCoins[change]

def printCoins(coinsUsed,change):
   coin = change
   while coin > 0:
      thisCoin = coinsUsed[coin]
      print(thisCoin)
      coin = coin - thisCoin

def main():
    amnt = 64
    clist = [1,5,10,21,25]
    coinsUsed = [0]*(amnt+1)
    coinCount = [0]*(amnt+1)

    print("Making change for",amnt,"requires")
    print(dpMakeChange(clist,amnt,coinCount,coinsUsed),"coins")
    print("They are:")
    printCoins(coinsUsed,amnt)
    print("The used list is as follows:")
    print(coinsUsed)

main()