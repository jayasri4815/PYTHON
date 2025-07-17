#function.py
#"function is a block of code it is executed when it is called in python to create function def keyword is used"
#"def is nothing but different"
"""
 syntax:def functionname():
           statements /functon body
        function calling()
"""
def jayasri():# functiondefinition
    print("good morning")
jayasri()
"""note : the value that was passed into function definition is called parameters
   # the value that was passed intofunction caling is called arguments
   #passing parameter and arguments to a function"""
def function(a):#fundametal
    print("this is value:",a) 
function(100)#function calling
#singe parameter function:passing a single or one parameter to a function is called single parameter
def function2(c):#parameter
    print(c)
function(100)
#multiple parameter function: passing a mutliple values to a function is called multiple parameter function
def function3(a,b):
    print("the result:",a+b)
function3(4,5)    
""" task:perform a float division operation using functionname it is multiple
2.write a program to wish a person using the python fuction given """
#1
def function4(c,s):#parameter
    print("the result",c+s)
function4(21.5,23)    
#2
def arjun():# functiondefiniition
    print("icon star") 
arjun() 
#arbitary argument():arbitary argument is an argument which is denoted by (*) 
# which takes multiple argument for a single parameter
#return the result in the form of tuple
def function(a):
    print(a)
function(10,15,20)