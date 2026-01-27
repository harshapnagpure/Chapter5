#Creating an empty st
b = set()
print(type(b))
#Adding values to an empty set
b.add(4)
b.add(5)
b.add(5)#Adding a value repeatedly does not change a set
#b.add([4,5,6])#set ke ander list ko add nhi kr skte hai and kyuki set ko hum change kr skte hai
b.add(( 4, 5, 6))

#Accessing Elements
#b.add({4:5})# dictionary also not add because it is changeable
print(b)

#length of the set
print(len(b))#Prints the length of this set

#Removal of an Items
b.remove(5)#Removes 5 from the set b
#b.remove(15)#throws an error while trying to remove 15(which does not present in the set)
print(b)

print(b.pop())
print(b)
