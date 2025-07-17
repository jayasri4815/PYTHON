#creation of dictionary 
#empty dictionary
c1={}
print(type(c1))
#key values
mydict={1:"sunny",2:"rjy"}
print(type(mydict))
#accesing the elements n dictionary:using the keys we can get values of dictionary
d2={100:"jaya",200:"sai","phone":"9014901995","place":"rjy"}
print(d2[100])#jaya
print(d2["place"])#rjy
print(d2[200])
#updating the dictionary():uing the keys we can update the dictionary
d2[100]="sunny"
print(d2)
#dictionary method:to access the method the syntax is variable name.methodname()
#1.get()returns the values of a specified key 
a={"name":"ram","sno":"1","place":"hyd"}
print(a)
print(a.get("name"))
print(a.get("sno"))
#keys: this method is used to get only keys in a dictionary
print(a.keys())
#values(): this method is used to retrive the values in a dictionary
print(a.values())
#items():this method is used get all the elements
print(a.items())

#in this particular senrio by converting the dictionary into list we ca retrive 
#update the dictionary into list[]
print(list(a))
#update method():to update any new key value pairs for an existing dictionary we use this update function
a.update({"food":"biryani"})
print(a)
#pop(): this method is used to delete the keys in a dictionary
a.pop("sno")
print(a)