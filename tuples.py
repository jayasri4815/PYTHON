""""
tuples is a collection of items /values/elements
they are enclosed within the parenthesis or 
open brackets () seperated by (,)
As Tuples are immutable it mean we cant change
so when the data is fixed we can go with tuples...
"""
#eg1:
mytuple=(13,12,11)
print(type(mytuple))#<class tuple>
mytuple2=()#empty tuple
print(type(mytuple2))#<class tuple>
mytuple3=(10)
print(type(mytuple3))#<class int>
"""
note: when you wanna create a tuplewith single value 
it should be sepersted by so that the compiler 
treats as tuple or else it  just treats as integer 
"""
#creation of tuple
#syntax:tuplevariable=(val1,val2,val3..valn)
mytuple5=(12,23,45,34+78j,[12,34,45], "hello",(123,"ece"))
print(mytuple5)
#creating a tuple with a single  element 
mytuple6=(45,)
print(type(mytuple6))
#creating a tuple with a list
t=[23,45,56,"jj"]
print(t)
k=tuple(t)
print(k)
#creating the tuple with "tuple" predefined word
t=tuple()#it consder as empty tuple 
print(t)