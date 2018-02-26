## FibonacciQueue example using Linked Lists
## By Leandro Soriano Marcolino
## If you find any bugs, let me know :)
## "Optimized" for clarity. This version does not test for overflows.

class Node:
    def __init__(self, content=None, next=None):
        self.content = content
        self.next  = next

class FibonacciQueue:
    def __init__(self):
        self.length = 0
        self.head = None

        ## For keeping track of Fibonacci Sequence:
        self.previous = 1
        self.secondPrevious = 0
        self.numRemoved = 0

    def is_empty(self):
        return self.length == 0

    ## In this solution I will assume that we reset FibonacciQueue when the queue is cleared
    def clear(self):
        self.length = 0
        self.head = None
        
        ## For keeping track of Fibonacci Sequence:
        self.previous = 1
        self.secondPrevious = 0
        self.numRemoved = 0

        
    ## You can change the numbers either when inserting or removing.
    ## In this solution I will change when removing
    def insert(self, content):
        node = Node(content)
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

    ## We must multiply by the correct number before we return the item to the user    
    def remove(self):
        content = self.head.content
        self.head = self.head.next
        self.length = self.length - 1

        ## Here we must modify the number

        if (self.numRemoved == 0):
            self.numRemoved = self.numRemoved + 1
            return 0 * content
        
        if (self.numRemoved == 1):
            self.numRemoved = self.numRemoved + 1
            return 1 * content

        ## From here on, we must keep track of the Fibonacci Sequence
        if (self.numRemoved > 1):
            
            tmp = self.previous + self.secondPrevious
            self.secondPrevious = self.previous
            self.previous = tmp

            return tmp*content
            
        ## We should never reach here. If we return -999, then something is wrong
        return -999

## Now we test FibonacciQueue in the main application. I will hard code the tests instead of getting user input.

queue = FibonacciQueue()

## Test 1 of handout:

queue.insert(5)
queue.insert(2)
queue.insert(3)
queue.insert(4)

print("Test 1 result: ")
for n in range(3):
    print(queue.remove())

queue.clear();

## Test 2 of handout:
queue.insert(10)
queue.insert(5)
queue.insert(3)
queue.insert(7)
queue.insert(5)
queue.insert(3)

print("Test 2 result: ")
for n in range(5):
    print(queue.remove())

queue.clear()


## Test 3 of handout
queue.insert(6)
queue.insert(25)
queue.insert(6)
queue.insert(3)
queue.insert(4)
queue.insert(2)

print("Test 3 result: ")
for n in range(6):
    print(queue.remove())

queue.clear()
