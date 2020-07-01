# -*- coding: utf-8 -*-
"""
Created on Wed Jul  1 14:29:25 2020

@author: dan
"""

def recur(num):
    if num > 0:
        num = num - 1
        print(num)
        recur(num)
    else:
        return
    

def fibonacci(n):
    if n <= 1:
        return n
    else:
        return(fibonacci(n - 1) + fibonacci(n - 2))
        

def fibcall5(nterm):
    print("fib seq by 5")
    for i in range(nterm + 1):
        if i % 5 == 0:
            print(fibonacci(i))
            
def fibcall(nterm):
    for i in range(nterm + 1):
        print(fibonacci(i))