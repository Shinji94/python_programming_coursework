# -*- coding: utf-8 -*-
"""
Created on Mon Nov 13 09:59:53 2017
student id :32026312
@author: wang xinji
"""

#question 1  FIBONACCI 
x = int(input("please input a number you want in fibonacci:   "))
def printfib(x):
    

    fib = [0,1]
    if x == 0:
        print("Error ,please input a number bigger than 0")
    else:    
        for i in range(x):
            fib.append(fib[-2]+fib[-1])
    print ('the nth number in fibonacci is :   ' + str(fib[x-1]))
  
printfib(x)
'''
I Create a list to store the number of fibonacci ,every time the 3rd number is calculated 
store it into the list 
finally print the xth number
'''

      
#question 2     
x = int(input("please inpu a number:   "))
def prime(x):

    prime = []
    prime.append(x)
    d = 2

    while d<=x/2:
        if x % d == 0:
            prime.append(d)
        d +=1
    print(prime)
prime(x)
'''
because remainder of the number x could not bigger than x/2
so each time when the remainder is ,add that number to the list 
finally print the list
'''
print('=============end of code===================')

#question 3 
'''
there are two main reasons
“ make the correspondence between the program (spread out in text space) and the process (spread out in time) ”
“the go to statement as it stands is just too primitive; it is too much an invitation to make a mess of one's program.”
the statement will change the program flow without limitation and is not understandable for other readers.
'''