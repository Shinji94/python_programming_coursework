## Priority Queue example with Linked Lists
## By Leandro Soriano Marcolino
## "Optimized" for clarity. This is not the most efficient implementation
## If you find any bugs, let me know :)

class Node:
    ## First, we need extra information at the node, in order to store its priority
    def __init__(self, content=None, priority=None, next=None):
        self.content = content
        self.priority = priority
        self.next  = next

class PriorityQueue:
    def __init__(self):
        self.length = 0
        self.head = None

    def is_empty(self):
        return self.length == 0

    def clear(self):
        self.length = 0
        self.head = None

    ## You could modify either the insert or the remove
    ## In this implementation, I will modify the remove
    ## However, I will make a small modification in insert 
    ## to allow me to insert the priority of a node
    def insert(self, content, priority):
        node = Node(content,priority)
        if self.head is None:
             #If list is empty the new node goes first
            self.head = node
        else:
             #Find the last node in the list
            last = self.head
            while last.next:
                last = last.next
             #Append the new node
            last.next = node
        self.length = self.length + 1

        
    def remove(self):
        ## First I will go over the queue, in order to discover the current highest priority
        ## 1 is the highest. 2 is lower than 1.
        ## I assume that no item would have "0" or negative priority.
        
        ## Obs 1: It should be possible to modify the insert method, so that this step is not necessary.
        ## Obs 2: It should also be possible to already find the correct node at this step. However,
        ## I will go over the list two times for the code to be clear
        
        currentNode = self.head
        highestPriorityFound = self.head.priority
        
        while (currentNode != None):
            if (currentNode.priority < highestPriorityFound):
                highestPriorityFound = currentNode.priority;
            currentNode = currentNode.next

        ## So now the highestPriorityFound holds the highest priority that exists in the queue.
        ## Hence, now I just need to find the first node (since the Queue is in order of arrival)
        ## which holds that priority

        currentNode = self.head
        previousNode = None
        found = False

        ## This could actually be a while (True).
        while (found == False):
            if (currentNode.priority == highestPriorityFound):
                ## I found the node. Hence, I must now remove it from the Queue and break the loop
                content = currentNode.content

                if (previousNode == None):
                    ## If I have no previous node, then I am the head of the Queue
                    self.head = self.head.next
                else:
                    ## If I have previous node, then I must link it to my next neighbor
                    previousNode.next = currentNode.next

                self.length = self.length - 1

                return content

            ## Prepare for next iteration
            previousNode = currentNode
            currentNode = currentNode.next

        ## I should never reach here. If I return -999, something is wrong
        return -999
                

## Now we test the PriorityQueue in the main application. I will hard code the tests instead of getting user input

queue = PriorityQueue()

## Test 1 of Handout:

queue.insert(5,1)
queue.insert(7,3)
queue.insert(8,2)
queue.insert(4,3)

print("Test 1:")
for n in range(4):
    print(queue.remove())

queue.clear()

## Test 2 of Handout:

queue.insert(9,2)
queue.insert(7,2)
queue.insert(5,2)
queue.insert(10,1)

print("Test 2:")
for n in range(3):
    print(queue.remove())

queue.clear()

## Test 3 of Handout:

queue.insert(5,10)
queue.insert(4,20)
queue.insert(3,1)
queue.insert(7,50)

print("Test 3:")
for n in range(2):
    print(queue.remove())

queue.clear()
