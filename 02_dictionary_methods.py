#Nexted dictionary
myDict = {
    "fast": "In a  Quick Manner",
    "harsha": "A Student",
    "marks": [1,2,5],
    "anotherdict":{'Harsha':'Player'},
    1: 2
}

#Dictionary Methods
# print(myDict.keys())
# print(list(myDict.keys()))#print the keys of dictionary
# print(myDict.values())# print the value of dictionary
#print(myDict.items()) # prints the (key, value) for all contents  of the dictionary
print(myDict)
updateDict = {
    "Lovish": "Friends",
    "Trisha": "Friends",
    "Divya": "Friends",
     "harsha": "A Coder"
}
myDict.update(updateDict) #Updates the dictionary by adding key-value pairs from updateDict
print(myDict)

print(myDict.get("harsha"))# prints value associated with key "harsha"
print(myDict["harsha"])#print value associated with key "harsha"

#The difference between .get and [] syntax in Dictionaries
print(myDict.get("harsha2"))#Returns None as harsha2 is not present in the dictionary
print(myDict["harsha2"])#throws an   error as harsha2 is not present in the dictionary
