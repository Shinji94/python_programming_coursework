class Stack:
     def __init__(self):
         self.items = 10*[0];
         self.position = 0;

     def push(self, item):
          if (self.position < 10):
              self.items[self.position] = item;
              self.position = self.position + 1;
              return True;
          else:
              return False;

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


s = Stack();

s.push(5);
s.push(10);
s.push(11);

s.pop();

print(s.pop());

s.push(15);

print(s.pop());
print(s.pop());
print(s.pop());
print(s.pop());
