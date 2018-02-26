class Node:
    def __init__(self, content=None, next=None):
        self.content = content
        self.next  = next

class Queue:
    def __init__(self):
        self.length = 0
        self.head = None

    def is_empty(self):
        return self.length == 0

    def clear(self):
        self.length = 0
        self.head = None
        
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

    def remove(self):
        content = self.head.content
        self.head = self.head.next
        self.length = self.length - 1
        return content

test = Queue();

test.insert(5);
test.insert(15);

test.remove();

test.insert(20);

test.insert(25);

print(test.remove());
print(test.remove());
print(test.remove());
