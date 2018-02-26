# -*- coding: utf-8 -*-
"""
Created on Sat Dec  2 20:19:52 2017

@author: wangxinji
"""
training_data = [
    [1.5,0,0],
    [5.75,0,0],
    [9.5,0,1],
    [1.5,1,1],
    [5.75,1,1],
    [9.5,1,0],
    [1.5,2,1],
    [5.75,2,1],
    [5.75,2,1],
    [9.5,2,0]
]

test_data = [[1, 2, 0], [3.75, 1, 0], [7.87, 0, 1]]

# Column labels.
header = ['fist feature','second feature','label']

def unique_vals(rows, col):
    """Find the unique values for a column in a dataset.
    so we can better calculate the mean of sepearte point"""
    return set([row[col] for row in rows])
x = unique_vals(training_data,0)

def uniquecounts(rows):
    """Counts the number of each type of example in a dataset."""
    results = {}
    for row in rows:
        r = row[len(row)-1]
        if r not in results:results[r] = 0
        results[r]+=1
    return results

uniquecounts(training_data)

def split_points(rows,cols):
    '''
    thie function calculate all the split points 
    in order to calculate gini index
    '''
    unique = list(unique_vals(rows,cols))
    split_points = []
    for i in range(len(unique)):
        for j in range(len(unique)):
            if j <=i:
                pass
            else:
                split_points.append((unique[i]+unique[j])/2)
    return split_points
split_points(training_data,0)
split_points(training_data,1)
def gini(rows):
    total = len(rows)
    counts = uniquecounts(rows)
    gini_index = 0
    for k1 in counts.keys():
        p1 = float(counts[k1])/total
        gini_index+= p1*(1-p1)
    return gini_index
gini(training_data)

class node:
    def __init__(self,col = -1,value = None,results = None,fb = None,tb = None):
        '''while value is False ===>left
           while value is True  ===>right
        '''
        self.col = col
        self.value = value
        self.results = results
        self.tb = tb
        self.fb = fb
    
def divideset(rows,column,value):
    '''
    judge whether it match the value and divide into 2 subset
    '''
    split_function = None
    if isinstance(value,int) or isinstance(value,float):
        split_function = lambda row:row[column] >= value
    else:
        split_function = lambda row:row[column]==value
    set1 = [row for row in rows if split_function(row)]
    set2 = [row for row in rows if not split_function(row)]
    return(set1,set2)
        
class decisionnode:
    def __init__(self,col = -1,value = None, results = None, tb = None,fb = None):
        self.col = col   
        self.value = value
        self.results = results 
        self.tb = tb 
        self.fb = fb 
(set1,set2) = divideset(training_data,0,4)
gini(set1)
def buildtree(rows):
    if len(rows)==0 : return decisionnode()
    current_score = gini(rows)
    best_gain = 0.0
    best_criteria = None
    best_sets = None
    
    column_count = len(rows[0]) - 1# count = 3 here
    for col in range(0,column_count):
        column_values = {}
        for row in rows:
            column_values[row[col]] = 1 # initialize
        for value in split_points(rows,col):
            (set1,set2) = divideset(rows,col,value)
            # infogain
            p = float(len(set1))/len(rows)
            gain = current_score - p*gini(set1) - (1-p)*gini(set2)
            if gain>best_gain and len(set1)>0 and len(set2)>0:
                best_gain = gain
                best_criteria = (col,value)
                best_sets = (set1,set2)
    #branch
    if best_gain>0:
        trueBranch = buildtree(best_sets[0])  #recurssion
        falseBranch = buildtree(best_sets[1])
        return decisionnode(col = best_criteria[0],value = best_criteria[1],
                            tb = trueBranch,fb = falseBranch)
    else:
        return decisionnode(results = uniquecounts(rows))
def print_tree(tree,indent = ' '):
    if tree.results != None:
        print(str(tree.results))
    else:
        print (str(tree.col)+":"+str(tree.value)+"? ")
        print (indent+"T->",
        print_tree(tree.tb,indent+" "))
        print (indent+"F->",
        print_tree(tree.fb,indent+" "))

x = buildtree(training_data)
print_tree(x)


#question 2 
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
class queue:
    def __init__(self, top=Node(), bot=Node()):
        self.top = bot
        self.bot = bot
        self.bot = self.top
    def insert(self, content):
        self.bot.content = content
        self.bot.next = Node()
        self.bot.next.number=self.bot.number+1
        self.bot = self.bot.next
    def isempty(self):
        if self.top.content is None:
            return str('this is empty')
        else:
            return str('this not empty')
    def clear(self):
        self =queue()
class fibq(queue):
        def remove(self):
            if self.isempty():
                print(self.top.content*fib(self.top.number))
                self.top = self.top.next
            else:
                print("empty queue!")
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

class PQueue(queue):
    def __init__(self, top=Node(), i=Node(),bot=Node()):
        self.top = top
        self.i = i
        self.bot = bot
        self.bot = self.top
        self.i = self.top
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
    print('please enter a number small than'+x.bot.number )
    p = int(input("please input priority to insert:  "))
    for i in range(r):
        x.remove()
else:
    for i in range(r):
        x.remove()
        
