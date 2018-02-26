# -*- coding: utf-8 -*-
"""
Created on Sat Nov 25 01:11:07 2017

@author: wangxinji
"""

class Node:
    def __init__(self, content=None, next=None,number=1):
        self.content = content
        self.number = number
        self.next = next
def fib(x):
    if x > 2:
        number = fib(x-1)+fib(x-2)
    elif x == 2:
        number = 1
    elif x == 1:
        number = 0
    return number
#question1
class fibq:
    def __init__(self, top=Node(), bot=Node()):
        self.top = bot
        self.bot = bot
        self.bot = self.top
    def insert(self, content):
        self.bot.content = content
        self.bot.next = Node()
        self.bot.next.number=self.bot.number+1
        self.bot = self.bot.next
    def remove(self):
        if self.isempty():
            print(self.top.content*fib(self.top.number))
            self.top = self.top.next
        else:
            print("empty queue!")
    def isempty(self):
        if self.top.content is None:
            return str('this is empty')
        else:
            return str('this not empty')
    def clear(self):
        self = fibq()
a=fibq()
x=1
while x != -1:
    x=int(input("please input numbers to insert:   "))
    a.insert(x)
n= int(input("please remove numbers:   "))

if n>a.bot.number:
    print("the size of queue is not enough")
    for i in range(a.bot.number+1):
        a.remove()
else:
    for i in range(n):
        a.remove()
''' 
question2
'''
class Node:
    def __init__(self, content=None, priority = 1,next=None,number=1):
        self.content = content
        self.number = number
        self.next = next
        self.priority = priority
class PQueue:
    def __init__(self, top=Node(), i=Node(),bot=Node()):
        self.top = top
        self.i = i
        self.bot = bot
        self.bot = self.top
        self.i = self.top

    def isempty(self):
        if self.top.content is None:
            return 0
        else:
            return 1
    def insert(self, content, priority):
        self.bot.content = content
        self.bot.priority=priority
        self.bot.next = Node()
        self.bot.next.number=self.bot.number+1
        self.bot = self.bot.next
    def remove(self):
        if self.isempty()!=0:
            priority=self.top.priority
            while self.i.content is not None:      
                priority = min(priority,self.i.priority)
                self.i=self.i.next
            self.i=self.top
            if self.top.priority == priority:  
                print(self.top.content)
                self.top = self.top.next
                self.i=self.top
            else:
                while self.i.next.priority != priority:
                    self.i = self.i.next
                else: 
                    print(self.i.next.content)
                    temp = Node()
                    temp = self.i
                    self.i = self.i.next  
                    if self.i.next is Node: 
                        self.bot = Node()
                        temp.next = self.bot
                    else:
                        temp.next = self.i.next  
                        self.i = self.top
        else:
            print("empty queue!")
    def clear(self):
        self = PQueue()
x=PQueue()

n=0
while n != -1:
    n = int(input("please input numbers to insert:  "))
    if n == -1:
        r = int(input("please remove:   "))
        break
    p = int(input("please input priority to insert:  "))
    x.insert(n,p)
if r > x.bot.number-1:
    pass
else:
    for i in range(r):
        x.remove()


#quetion3