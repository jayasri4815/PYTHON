list1=["Edinburgh","scotland","london"]
print(list1)
list1.append("bhrihingam")
print(list1)
#extend: this method is used to add the element at the end but
#  as a sublist
list1.extend(("paris","malta","aus"))
print(list1) 
#count: This method counts the number of  repeated elements in a list
flowers=["rose","hibiscus","tulips"]
print(flowers.count("rose"))
#mutability
mylist4=["hello","Ece",123,34,56,56+78j]
print(mylist4)
mylist4[2]="agri"
print(mylist4)
#pop--remove the elements using index
mylist5=[12,34,565,78,9,34+56j,"hello"]
print(mylist5)
mylist5.pop(2)
print(mylist5)
#remove--remove the element directly
mylist5.remove(34)
print(mylist5)
#count--it counts the number of occurance
#of a item in a list
mylist6=[22,33,33,22,55,22,44,67,56,22]
print(mylist6.count(22))
"""Note:It will take atmost only one argument
"""
#insert--it just insert the elements into the list
#using the index
mylist7=[22,33,44,77,88]
print(mylist7)
mylist7.insert(1,"hello")
print(mylist7)
"Note: In insert the method no element is removed"
"they just replace the position"
#index--this method tells the 
#index of first occurance when an element is reapted
mylist8=[22,44,55,55,44,66,67,89]
print(mylist8.index(44))#1
print(mylist8.index(55))#2
#reverse--it jusst reverse the elements
mylist8.reverse()
print(mylist8)
#copy--it just copy the elements in a list
#one list to other
mylist9=[22,33,44,55,66,77]
print(mylist9)
mylist10=mylist9.copy()
print(mylist10)
#clear--it clears the elements in a list 
print(mylist10.clear())
print(mylist10)
#sort-- it just arranges the element in a sorting way
mylist11=[22,11,77,9,89,0]
mylist11.sort()
print(mylist11)
mylist12=["m","a","k","b","c","s","k","j"]
mylist12.sort()
print(mylist12)
mylist13=[12,123,"hello"]
mylist13.sort()
print(mylist13)
#accessing the tuples in a list 
#using the index we can acces this
#elements in a tuple
#index syntax(start:stop)
mytuple8=(11,22,44,55,77,(78,89),"hello")
print(type(mytuple8))
print(mytuple8[0:5])
print(mytuple8[0:3])
mytuple=([12,13,14],[89,90,78])
print(mytuple[1])
#tuple can access in two ways either index or slicing
#slicng:
#it is used to retrive the elements
#from a particular range the
#syntax (start:stop:skip)s^3
mytuple10=(11,12,33,44,55,77,88,99,"hello","agri","ece")
print(mytuple10[3:9:3])
mytuple11=(22,33,44,66,77,88,99,10,24,45,67,45,78)
print(mytuple11[4:10:5])
mytuple12=("hello",123,456,34,45,56+78j,"ists","agri","ece",345.9,"dept",12,23,34,56,67,90)
print(mytuple12[-1])
print(mytuple12[7:-2:2])