class GrowingStack:
    
    def __init__(self, numItems = 2):
        self.items = numItems*[0];
        self.position = 0;
        self.stackSize = numItems;
        
    
    def push(self, item):
          if (self.position < self.stackSize):
              self.items[self.position] = item;
              self.position = self.position + 1;
              return True;
          else:
              newItems = (self.stackSize + 10)*[0];
              
              for x in range(self.stackSize):
                  newItems[x] = self.items[x];
              
              self.items = newItems;
              
              self.stackSize = self.stackSize + 10;
              
              return self.push(item);
            
    def pop(self):
         if (self.position <= 0):
            return False;
         else:
            self.position = self.position - 1;
            return self.items[self.position];

    def empty(self):
         self.position = 0;

    def is_empty(self):
         return (self.position == 0)

s = GrowingStack();

for x in range(100):
    s.push(x);
    
for x in range(100):
    print(s.pop());